import os
from dotenv import load_dotenv

from typing import Annotated, Literal
from typing_extensions import TypedDict
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama
from langchain.tools.render import render_text_description
#from tools import current_datetime
from tools import retrieve_current_date, retrieve_current_time, document_obsidian_topic, amend_daily_file, save_local_files

tools = [retrieve_current_date, retrieve_current_time, document_obsidian_topic, amend_daily_file, save_local_files]
llm = ChatOllama(
    model="llama3.2",
).bind_tools(tools)


def expert(state: MessagesState):
    rendered_tools = render_text_description(tools)
    system_prompt = f"""
    You are a conversational assistant named "obsi" that has access to the following set of tools.
    Here are the names and descriptions for each tool:
    
    {rendered_tools}

    Given the user input, either discuss with the user or call the right tool to use.
    """
    
    messages = state["messages"]
    response = llm.invoke([system_prompt] + messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)

def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state['messages']
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END


graph = StateGraph(MessagesState)

graph.add_node("expert", expert)
graph.add_node("tools", tool_node)

graph.add_edge(START, "expert")
graph.add_conditional_edges("expert", should_continue)
graph.add_edge("tools", "expert")

checkpointer = MemorySaver()

app = graph.compile(checkpointer=checkpointer)

while True:
    user_input = input(">> ")
    if user_input.lower() in ["quit", "exit"]:
        print("Exiting...")
        break

    response = app.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config={"configurable": {"thread_id": 21}}
    )

    print(response["messages"][-1].content)
