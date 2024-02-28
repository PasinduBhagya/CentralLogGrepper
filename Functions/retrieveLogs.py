import subprocess
from datetime import datetime
import os
from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

# Loading Directory Parameters
retrieved_log_file_sharing_path = config.get('DIRECTORY_PATHS', 'RETRIEVED_LOG_FILE_SHARING_PATH')
archived_log_file_names = config.get('PROJECT_PARAMETERS', 'PROJECT_LOG_ARCHIVED_DIRECTORY_NAMES')

def retrieveLogs(string_to_search, archived_log_file_path, jira_id):
    try:
        app_name = archived_log_file_path.split("/")[-2]
        extracted_log_file_name = f"{retrieved_log_file_sharing_path}/{jira_id}/{string_to_search}_{app_name}.log"
        if not os.path.exists(extracted_log_file_name):
            command = f"zgrep -a {string_to_search} {archived_log_file_path} > {extracted_log_file_name}"
            subprocess.run(command, shell=True, check=True)
            print(f"INFO: File was saved to {string_to_search}_{app_name}.log")
        else:
            print(f"WARNING: String {string_to_search} already grepped.")
    except subprocess.CalledProcessError:
        print(f"Warning: No records of {string_to_search} found in {archived_log_file_path}.")
    except:
        print(f"Error: Failed to retrieve data due to unknow error.")


def getSearchString(collected_ID_List, jira_id, available_log_archive_files):
    for search_to_string in collected_ID_List:
        for archived_log_file_path in available_log_archive_files:
            print(f"INFO: Searching for {search_to_string} in {archived_log_file_path}.")
            retrieveLogs(search_to_string, archived_log_file_path, jira_id)
