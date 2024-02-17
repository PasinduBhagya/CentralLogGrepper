import os

def getCompressedLogFile(logged_date, archived_log_file_path):

    final_archived_log_file_name = None

    prefix_archived_log_file_name = "catalina.out_" + logged_date.replace("-", "_")
    archived_log_file_names = os.listdir(archived_log_file_path)

    for archived_log_file_name in archived_log_file_names:
        
        if prefix_archived_log_file_name in archived_log_file_name:
            print("INFO: Archived log file was found - " + archived_log_file_name)
            final_archived_log_file_name = archived_log_file_name

    if final_archived_log_file_name is None:
        print(f"\nError: Unable to find the logs on {logged_date}\n")
        exit()