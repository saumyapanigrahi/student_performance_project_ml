import sys
import logging # checking if the code executed correctly or not - the test code is at the end

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    )

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# testing the code with one example...
if __name__=="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)





#---------------------------------------------------------------- Code Explanation ----------------------------
# Part 1 — The Function error_message_detail
# Think of this function as a detective 🕵️
# When an error happens, it investigates and finds:

# Which file had the error?
# Which line number?
# What was the error?

# import sys

# Importing sys — it's a Python built-in tool that gives us info about what's happening inside the program right now.


# def error_message_detail(error, error_detail:sys):

# Creating a function that takes 2 things:

# error → the actual error that happened
# error_detail → the sys module to dig deeper into the error



# _,_,exc_tb = error_detail.exc_info()

# exc_info() returns 3 things about the error:

# type of error
# error value
# traceback (where exactly it happened)

# We don't care about first 2, so we use _ to ignore them.
# We only keep exc_tb (traceback) because that tells us where the error happened.


# file_name = exc_tb.tb_frame.f_code.co_filename

# From the traceback, we dig in and find the exact file name where the error happened.
# Like detective finding — "the crime happened in data_ingestion.py!"


# error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
#     file_name, exc_tb.tb_lineno, str(error)
# )

# Building a clear error message with 3 details:

# {0} → file name (data_ingestion.py)
# {1} → line number (45)
# {2} → what the error was (Column 'age' not found)

# Final message looks like:
# Error occurred in script [data_ingestion.py] line number [45] error message [Column 'age' not found]


# return error_message

# Send this detailed message back to whoever called this function.


# Part 2 — The Class CustomException
# Think of this as a custom alarm system 🚨
# Normal Python alarms are basic. This one gives you full details.

# class CustomException(Exception):

# Creating our own custom exception class.
# (Exception) means it inherits from Python's built-in Exception — so it behaves like a normal exception but with extra features.


# def __init__(self, error_message, error_detail:sys):

# This runs automatically when an error is raised.
# Takes 2 things:

# error_message → the basic error
# error_detail → sys module to get more details



# super().__init__(error_message)

# Calling the parent class (Python's built-in Exception) and passing the error message to it.
# Like telling your manager about the error before handling it yourself.


# self.error_message = error_message_detail(error_message, error_detail=error_detail)

# Calling our detective function from Part 1 to get the full detailed error message and storing it.


# def __str__(self):
#     return self.error_message

# __str__ means — "when someone prints this exception, what should they see?"
# We return our detailed error message instead of the basic one.


# Full Picture in Simple Story
# ❌ Error happens somewhere in your code
#         ↓
# 🚨 CustomException is raised
#         ↓
# 🕵️ error_message_detail investigates:
#    - Which file? data_ingestion.py
#    - Which line? 45
#    - What error? Column 'age' not found
#         ↓
# 📋 Returns full detailed message
#         ↓
# ✅ You know exactly where to fix it!

# How You Will Use It in Other Files
# # in data_ingestion.py
# try:
#     # some code that might fail
#     df = pd.read_csv('data.csv')

# except Exception as e:
#     raise CustomException(e, sys)  
#     # ↑ this will print exactly which file and line failed!
# Does this make sense now? 😊