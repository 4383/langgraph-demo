from datetime import datetime
from typing import Optional, Literal
from langchain_core.tools import tool
from langchain.tools import Tool

from modules.date import DateTimeRequest, DateRequest


@tool
def document_obsidian_topic(topic):
    """
    document a given topic into obsidian
    """
    print(f"document: {content}")
    return topic


@tool
def amend_daily_file(topic):
    """
    amend content into the daily file
    """
    print(f"daily note: {content}")
    return topic


@tool
def save_local_files():
    """
    save local files
    """
    print("saving")
    return content


@tool
def retrieve_current_date():
    """
    retrieve the current date
    """
    print("retrieve date")
    return datetime.now().strftime("%Y-%m-%d")

@tool
def retrieve_current_time():
    """
    retrieve the current time
    """
    print("retrieve time")
    return datetime.now().strftime("%H:%M:%S")

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
