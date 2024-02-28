import os
from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

# Loading directory parameters
retrieved_log_file_sharing_path = config.get('DIRECTORY_PATHS', 'RETRIEVED_LOG_FILE_SHARING_PATH')

def createDir(jira_id):
    print(f"INFO: Creating the {jira_id} directory on {retrieved_log_file_sharing_path}.")
    log_store_directory_path = f"{retrieved_log_file_sharing_path}/{jira_id}"
    try:
        if not os.path.exists(log_store_directory_path):
            os.makedirs(log_store_directory_path)
        else:
            print(f"WARNING: {jira_id} directory is already exists.")
    except:
        print(f"\nError: Failed to create {log_store_directory_path} directory.\n")
        exit()