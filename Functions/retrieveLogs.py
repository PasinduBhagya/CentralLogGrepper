import subprocess
from datetime import datetime
import os
from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

# Loading Directory Parameters
retrieved_log_file_sharing_path = config.get('DIRECTORY_PATHS', 'RETRIEVED_LOG_FILE_SHARING_PATH')
#
# if not os.path.exists(log_store_directory_path):


def retrieveLogs(string_to_search, archived_log_file_path,jira_id):
    try:
        extracted_log_file_name = f"{retrieved_log_file_sharing_path}/{jira_id}/{string_to_search}.log"
        if not os.path.exists(extracted_log_file_name):
            command = f"zgrep -a {string_to_search} {archived_log_file_path} > {extracted_log_file_name}"
            subprocess.run(command, shell=True, check=True)
            print(f"INFO: File was saved to {string_to_search}.log")
        else:
            print(f"WARNING: String {string_to_search} already grepped.")
    except subprocess.CalledProcessError:
        print(f"Warning: Records for {string_to_search} is not found.")
    except:
        print(f"Error: Failed to retrieve data due to unknow error.")


def getSearchString(collected_ID_List, archived_log_file_path, jira_id):
    for search_to_string in collected_ID_List:
        print(f"INFO: Searching for {search_to_string}.")
        retrieveLogs(search_to_string, archived_log_file_path, jira_id)
