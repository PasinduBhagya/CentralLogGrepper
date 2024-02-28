import os

from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

def getCompressedLogFile(req_log_date):

    # Loading directory parameters
    archived_log_file_path = config.get('DIRECTORY_PATHS', 'ARCHIVED_LOG_FILE_PATH')
    archived_log_file_names = config.get('PROJECT_PARAMETERS', 'PROJECT_LOG_ARCHIVED_DIRECTORY_NAMES')

    available_log_archive_files = []

    available_archived_log_files_names = os.listdir(archived_log_file_path)
    
    for log_direcory_name in archived_log_file_names.split(","):
        if log_direcory_name not in available_archived_log_files_names:
            print(f"Error: {log_direcory_name} is not found in {archived_log_file_path} directory.")
            exit()
        else:
            final_archived_log_file_name = None

            prefix_archived_log_file_name = "catalina.out_" + req_log_date.replace("-", "_")

            archived_log_file_names = os.listdir(archived_log_file_path + "/" + log_direcory_name)
            print(archived_log_file_path + "/" + log_direcory_name)
            
            for archived_log_file_name in archived_log_file_names:
                if prefix_archived_log_file_name in archived_log_file_name:
                    print(f"INFO: Archived {archived_log_file_name} file was found in {log_direcory_name} directory.")
                    final_archived_log_file_name = archived_log_file_name
                    available_log_archive_files.append(archived_log_file_path + "/" + log_direcory_name + "/" + final_archived_log_file_name)
                    # print(archived_log_file_names)

            if final_archived_log_file_name is None:
                print(f"Error: Unable to find the logs on {req_log_date} in {log_direcory_name} directory.")
            
    if len(available_log_archive_files) == 0:
        print(f"ERROR: No Logs were found for requested date - {req_log_date}")
        exit()
    else:
        # print(available_log_archive_files)
        # exit()
        return available_log_archive_files
        
    