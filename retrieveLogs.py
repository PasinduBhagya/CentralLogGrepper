import subprocess
from pytz import timezone
from datetime import datetime
import os
import time
from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

# Loading Directory Parameters
retrieved_log_file_path = config.get('DIRECTORY_PATHS', 'RETRIEVED_LOG_FILE_PATH')

folder_name = datetime.now(timezone("Asia/Kolkata")).strftime('%Y%m%d%H%M%S')

def creteDir(retrieved_log_file_path):
    log_store_directory_path = f"{retrieved_log_file_path}/{folder_name}"
    try:
        if not os.path.exists(log_store_directory_path):
            os.makedirs(log_store_directory_path)
        else:
            time.sleep(1)
            if not os.path.exists(log_store_directory_path):
                os.makedirs(log_store_directory_path)
    except:
        print(f"\nError: Failed to create {log_store_directory_path} directory.\n")
        exit()
    
    return log_store_directory_path

log_store_directory_path = creteDir(retrieved_log_file_path)

def retrieveLogs(string_to_search, file_path):
    
    try:
        extracted_log_file_name = f"{log_store_directory_path}/{string_to_search}.log"
        command = f"zgrep -a {string_to_search} {file_path} > {extracted_log_file_name}"
        subprocess.run(command, shell=True, check=True)
        print(f"INFO: File was saved to {string_to_search}.log")
    except subprocess.CalledProcessError:
        print(f"Warning: No records are avalible for {string_to_search}.")
    except:
        print(f"Error: Failed to retrieve data due to unknow error.")

    return folder_name