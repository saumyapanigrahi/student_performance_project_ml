import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

# Check if logger is working correctly (remove the # tags in the below code and run)
# if __name__=="__main__":
#     logging.info("Logging has started")

#--------------------- Code Explanation ---------------------
# Let me break it down line by line simply! 😊

# What is this file doing overall?
# Think of it as setting up a diary 📔

# Creating a diary file with today's date and time as name
# Deciding where to keep the diary
# Setting up the format of how each entry is written


# Line by Line
# import logging

# Importing Python's built-in diary/logging tool


# import os

# Importing os — helps us work with folders and file paths


# from datetime import datetime

# Importing datetime — helps us get current date and time


# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating the diary file name using current date and time
# datetime.now() → gets current time
# strftime('%m_%d_%Y_%H_%M_%S') → formats it nicely
# Result looks like:
# 05_07_2026_11_30_45.log
# Every time you run your project, a new log file is created with that exact time! ✅


# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Creating the full path where the log file will live
# os.getcwd() → your current project folder
# "logs" → inside a folder called logs
# LOG_FILE → the file name we just created
# Result looks like:
# /ml_heart_disease_prediction/logs/05_07_2026_11_30_45.log


# os.makedirs(logs_path, exist_ok=True)

# Creates the logs folder if it doesn't already exist
# exist_ok=True → don't throw error if folder already exists


# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Storing the complete file path in a variable so we can use it below


# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# Setting up the diary rules:
# filename → save logs in this file
# format → how each log line should look:
# [ 2026-05-07 11:30:45 ] 45 root - INFO - Data loaded successfully
#    ↑ time              ↑line  ↑who  ↑level  ↑your message
# level=logging.INFO → record everything that is INFO level or above:

# LevelWhen to useINFONormal things happening ✅WARNINGSomething seems off ⚠️ERRORSomething went wrong ❌CRITICALSomething very serious 🚨

# Full Picture as a Story
# 🏃 You run your project
#         ↓
# 📅 Logger creates a new file
#    "05_07_2026_11_30_45.log"
#         ↓
# 📁 Saves it inside /logs/ folder
#         ↓
# 📝 Every time something happens
#    in your code it writes:
#    [2026-05-07 11:30:45] 45 root - INFO - Data loaded successfully
#    [2026-05-07 11:31:00] 67 root - ERROR - File not found
#         ↓
# ✅ You can check this file anytime
#    to see what happened and when!

# How You Use it in Other Files
# import logging

# logging.info("Data ingestion started")        # normal info
# logging.warning("Missing values found")       # warning
# logging.error("File not found")               # error
# Each line gets saved automatically to your .log file! 😊