from json import dumps
from httplib2 import Http

# Copy the webhook URL from the Chat space where the webhook is registered.
# The values for SPACE_ID, KEY, and TOKEN are set by Chat, and are included
# when you copy the webhook URL.

from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

# Loading Directory Parameters
retrieved_log_file_sharing_path = config.get('DIRECTORY_PATHS', 'RETRIEVED_LOG_FILE_SHARING_PATH')

def sendNotification(jira_id):
    """Google Chat incoming webhook quickstart."""
    url = "https://chat.googleapis.com/v1/spaces/AAAAopTT5tk/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=8bjADeLFjGKgH5UGPGuGQzMP-aC9PD4y4K4kttY-gME"
    app_message = {"text": f"You log files can be collected from {jira_id} directory located at {retrieved_log_file_sharing_path}\n\nDesigned and Developed by Pasindu Bhagya"}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
