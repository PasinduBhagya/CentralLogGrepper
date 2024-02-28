import sys
from configparser import ConfigParser

from Functions.command_verification import command_verification
arguments = sys.argv
search_method = command_verification(arguments)

log_requested_date = arguments[arguments.index("--date")+1]

config = ConfigParser()
config.read('./configurations.cfg')

jira_id = arguments[arguments.index("--jira-id")+1]
print(f"INFO: Reading JIRA ID - {jira_id}.")

# Reading the Entire JIRA
from Functions.read_JIRA import read_jira
jira_description, jira_comments = read_jira(jira_id)

# Checking for Archived log File path on the requested date
from Functions.getComLogFile import getCompressedLogFile

req_log_date = arguments[arguments.index("--date")+1]
available_log_archive_files = getCompressedLogFile(req_log_date) 

# Checking Each String of the comment to check Booking_IDs, Session_IDs and Basket IDs
from Functions.collect_searchIDs import collectIDs
collected_ID_List = collectIDs(jira_description, jira_comments)

# Creating for the Directory for the JIRA
from Functions.createDir import createDir
createDir(jira_id)

# Searching the Log files for specific strings
from Functions.retrieveLogs import getSearchString
getSearchString(collected_ID_List, jira_id, available_log_archive_files)

# Send the Notification to via the Google Space
from Functions.notify_google_chat import sendNotification
sendNotification(jira_id)

print("\nINFO: Log grepping process is completed")