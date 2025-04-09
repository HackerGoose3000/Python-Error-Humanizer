
# Welcome to A.M.B.E.R your "Assistant for Managing Bugs, Errors, and Responses"

#Importing necessary libraries Json for the big json file, logging for logging errors, and traceback for getting the specific error message
import json
import logging
import os 

errorListFile=os.path.join(os.path.dirname(__file__), 'humanizedErrors.json')

# open the json file with the error messages
try:
    with open(errorListFile, 'r', encoding='utf-8' ) as file:
        humanized_errors = json.load(file)
except Exception as e:
    print(f"⚠️ Amber could not load the error messages: {e}")
    humanized_errors = {}

# Fuction to get a logger
logger = logging.getLogger(__name__)

# Check if the logger has handlers, if not, add a default handler
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.ERROR)

def humanize_error(error_type: str) -> str:
    return humanized_errors.get(error_type, "An unknown error occurred.")

def developer_code():
    # Dev pastes their code inside this function
    x = 1 / 0  # Example error

#  Amber’s main error-catching system
try:
    developer_code()

except Exception as e:
    error_type = type(e).__name__
    explanation = humanize_error(error_type)
    
    logger.error(f"{explanation}", exc_info=True)
    print(f"You have an error: {explanation}")


