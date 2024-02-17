import sys
from configparser import ConfigParser

from command_verification import command_verification
arguments = sys.argv
search_method = command_verification(arguments)

log_file_date = arguments[arguments.index("--date")+1]

from read_JIRA import read_jira, collecting_ids
from retrieveLogs import retrieveLogs
from notify_google_chat import sendNotification
from getComLogFile import getCompressedLogFile

config = ConfigParser()
config.read('./configurations.cfg')

# Loading directory parameters
archived_log_file_path = config.get('DIRECTORY_PATHS', 'ARCHIVED_LOG_FILE_PATH')

# Loading JIRA parameters
jira_url = config.get('JIRA_PARAMETERS', 'JIRA_URL')
jira_username = config.get('JIRA_PARAMETERS', 'JIRA_USERNAME')
jira_api_key = config.get('JIRA_PARAMETERS', 'JIRA_API_KEY')

id_list = []

getCompressedLogFile(log_file_date, archived_log_file_path)


# Try to add Comment in here as well
def getFromJIRA(jira_id):
    print(f"INFO: Reading {jira_id} JIRA.")
    description = read_jira(jira_id, jira_url, jira_username, jira_api_key)
    print("INFO: Getting booking_id and session_id.")

    for single_string in description:
        search_id = collecting_ids(single_string)
        if search_id is not None:
            id_list.append(search_id)
            print(f"INFO: Identified ID - \t {search_id}")
            print(f"INFO: Collecting {search_id} from the Log File.")
            folder_name = retrieveLogs(search_id, archived_log_file_path)
        
    print("INFO: Sending notification to the space.")
    sendNotification(folder_name)

def getFromString(search_string):
    print(f"INFO: Searching for the {search_string} in the Archived Logs.")

    folder_name = retrieveLogs(search_string, archived_log_file_path)
        
    print("INFO: Sending notification to the space.")
    sendNotification(folder_name)

if "--jira-id" in arguments:
    jira_id = arguments[arguments.index("--jira-id")+1]
    if "--comment-id" in arguments:
        jira_comment_id = arguments[arguments.index("--comment-id")+1]
        print(jira_comment_id)

    getFromJIRA(jira_id)

elif "--string" in arguments:
    search_string = arguments[arguments.index("--string")+1]
    getFromString(search_string)
    