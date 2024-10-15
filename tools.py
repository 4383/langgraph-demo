from datetime import datetime
from typing import Optional, Literal
from langchain_core.tools import tool
from langchain.tools import Tool

from modules.date import DateTimeRequest, DateRequest


@tool
def take_notes(content):
    """
    take note for user
    """
    print("prise de note")
    return content


def get_date_part(part: str):
    now = datetime.now()

    if part == "day_number":
        return now.strftime("%d")  # Numéro du jour
    elif part == "day_name":
        return now.strftime("%A")  # Nom du jour (Lundi, Mardi, etc.)
    elif part == "month_number":
        return now.strftime("%m")  # Numéro du mois
    elif part == "month_name":
        return now.strftime("%B")  # Nom du mois (Janvier, Février, etc.)
    elif part == "year":
        return now.strftime("%Y")  # Année
    else:
        return "Invalid part requested"

# Créer un outil pour LangChain
def date_tool_func(request: DateRequest):
    print("retrieve date")
    return get_date_part(request.part)

date_tool = Tool(
    name="Date Tool",
    description="""
    The Date Tool allows users to retrieve specific components of the current date. 
    It can answer queries about isolated parts of the date, such as the day number, day name, month number, month name, or year. The tool is designed to respond flexibly to user requests by providing exactly the requested date component.
    
    This tool is especially useful for cases where a user may ask questions like:
    - "What day is it today?"
    - "What is the current month's number?"
    - "Which year are we in?"
    - "What is the current month's name?"
    
    The tool processes the user's request, validates it, and returns the requested date component based on the current day.
    
    Input Parameters:
    - `part` (str): This parameter defines the specific part of the current date the user wants to retrieve. It must be one of the following:
      - `"day_number"`: Returns the current day of the month as a number (e.g., "15").
      - `"day_name"`: Returns the full name of the current day (e.g., "Monday").
      - `"month_number"`: Returns the current month as a number (e.g., "10" for October).
      - `"month_name"`: Returns the full name of the current month (e.g., "October").
      - `"year"`: Returns the current year (e.g., "2024").
    
    Output:
    - The tool will return the specific component of the current date as requested by the user.
      
    Example Usage:
    - To get the current day of the week:
      result = date_tool_func(DateRequest(part="day_name"))  # Returns "Monday"
      
    - To get the current month number:
      result = date_tool_func(DateRequest(part="month_number"))  # Returns "10"
      
    Error Handling:
    - If the input parameter `part` does not match one of the accepted values, 
      a ValueError will be raised with a message indicating the allowed options.
    """,
    func=date_tool_func
)


#def retrieve_datetime(part="both"):
#    print("ici")
#    now = datetime.now()
#    
#    if part == "date":
#        return now.strftime("%Y-%m-%d")
#    elif part == "time":
#        return now.strftime("%H:%M:%S")
#    elif part == "day":
#        return now.strftime("%d")
#    elif part == "month":
#        return now.strftime("%m")
#    elif part == "year":
#        return now.strftime("%Y")
#    elif part == "hour":
#        return now.strftime("%H")
#    elif part == "minute":
#        return now.strftime("%M")
#    elif part == "second":
#        return now.strftime("%S")
#    else:  # Default case for "both"
#        return now.strftime("%Y-%m-%d %H:%M:%S")
#
#@tool
#def current_datetime(request: DateTimeRequest):
#    """
#    Fetches the current date and/or time depending on the user's request.
#
#    This function handles requests for specific parts of the current date and time, such as the full date, full time, or individual components like the year, month, day, hour, minute, or second. 
#
#    Parameters:
#    - part (str): Specifies which part of the datetime to return. 
#                  Accepted values are:
#                  - "date": Returns only the date (format: 'YYYY-MM-DD').
#                  - "time": Returns only the time (format: 'HH:MM:SS').
#                  - "day": Returns only the day of the month.
#                  - "month": Returns only the month.
#                  - "year": Returns only the year.
#                  - "hour": Returns only the hour.
#                  - "minute": Returns only the minutes.
#                  - "second": Returns only the seconds.
#                  - "both" (default): Returns both the date and time (format: 'YYYY-MM-DD HH:MM:SS').
#
#    Example usage:
#    - To get the current hour: 
#      get_datetime(part="hour")
#    - To get the current date and time:
#      get_datetime(part="both")
#
#    This tool is useful when the user queries for specific parts of the current datetime.
#    For example, "What time is it now?" will fetch the current hour, minute, and second.
#    
#    Make sure to pass one of the valid options to avoid errors. 
#    If an invalid part is requested, a ValueError will be raised.
#    """
#    print("la")
#    return retrieve_datetime(request.part)
