import os

from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')


# Loading directory parameters
archived_log_file_path = config.get('DIRECTORY_PATHS', 'ARCHIVED_LOG_FILE_PATH')
archived_log_file_names = config.get('PROJECT_PARAMETERS', 'PROJECT_LOG_ARCHIVED_DIRECTORY_NAMES')

# List what are the existing folders in the archived_log_file_path
# Check for archived_log_file_names
# 

# def getCompressedLogFile(req_log_date):
#     # final_archived_log_file_name = None
#     # prefix_archived_log_file_name = "catalina.out_" + req_log_date.replace("-", "_")

def getCompressedLogFile(req_log_date):

    final_archived_log_file_name = None

    prefix_archived_log_file_name = "catalina.out_" + req_log_date.replace("-", "_")
    # 
    archived_log_file_names = os.listdir(archived_log_file_path)

    for archived_log_file_name in archived_log_file_names:
        if prefix_archived_log_file_name in archived_log_file_name:
            print("INFO: Archived log file was found - " + archived_log_file_name)
            final_archived_log_file_name = archived_log_file_name

    if final_archived_log_file_name is None:
        print(f"\nError: Unable to find the logs on {req_log_date}\n")
        exit()
    
    if final_archived_log_file_name is not None:
        return archived_log_file_path