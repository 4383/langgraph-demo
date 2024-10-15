import os
from dotenv import load_dotenv

from typing import Annotated, Literal
from typing_extensions import TypedDict
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama
#from tools import current_datetime
from tools import date_tool, take_notes

tools = [date_tool, take_notes]
llm = ChatOllama(
    model="llama3.2",
).bind_tools(tools)


def expert(state: MessagesState):
    system_message = """
    Vous êtes un assistant conversationnel intelligent, poli, et efficace, conçu pour discuter de manière naturelle avec l'utilisateur tout en lui offrant une assistance personnalisée. Lorsque l'utilisateur exprime un besoin de prise de notes, vous utilisez automatiquement les outils à votre disposition pour répondre efficacement à ses demandes, sans qu'il ait besoin de préciser l'outil à utiliser. 

    Votre objectif est de fluidifier la conversation, de faciliter les tâches et d'offrir un support proactif, tout en anticipant et en répondant aux besoins de l'utilisateur au fur et à mesure qu'ils émergent.
    """
    #system_message = """
    #    You are a conversional agent.
    #    You are tasked with discussing with the user and
    #    resume based on a job description.
    #    You can access the resume and job data using the provided tools.

    #    You must NEVER provide information that the user does not have.
    #    These include, skills or experiences that are not in the resume.
    #    Do not make things up.
    #"""
    messages = state["messages"]
    response = llm.invoke([system_message] + messages)
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
        config={"configurable": {"thread_id": 9}}
    )

    print(response["messages"][-1].content)
