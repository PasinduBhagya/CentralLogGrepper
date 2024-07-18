# Archived Log File Analyzing Tool

## About the Tool
I have developed a Python tool designed to analyze log files and extract log entries based on predefined patterns sourced from JIRA tickets. By specifying a JIRA ID, the tool can identify and gather relevant log entries efficiently. To utilize this functionality, execute the main.py script with the --jira-id argument as demonstrated below.

`python3 main.py --jira-id <JIRA ID>`

This tool was developed to identify few predfiende patterns digit numbers but new patterns can be added by updating the **collect_searchIDs.py**.

## Required Configurations
Additionally, there is a configuration file named configuration.cfg. Ensure that the necessary information is added to this file to enable the tool to function correctly.

| Parameter Name      | Description |
| --------- | -----:|
| ARCHIVED_LOG_FILE_PATH  | Absoulte path of the Arachvied Log files located  |
| RETRIEVED_LOG_FILE_PATH     |   Absoulte to a directory which will be used to store collected log files from JIRA |
| GOOGLE_CHAT_API_KEY      |    Google Chat Group to notify once the process is completed |
|JIRA_URL| URL of the JIRA API Service|
|JIRA_USERNAME| Username to login to the JIRA API Service|
|JIRA_API_KEY| JIRA API Key to login to JIRA API Service|

The **RETRIEVED_LOG_FILE_PATH** in the configuration file should be set to a directory on a Samba share. Once the retrieval process is completed, a new folder named after the JIRA ID will be created within this directory. This folder can later be accessed by developers, who can mount the Samba share on their laptops to review the log entries.
