import requests
import base64
import re

def read_jira(jira_id, jira_url, jira_username, jira_api_key):

    url = f"{jira_url}/{jira_id}"
    
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64.b64encode(f'{jira_username}:{jira_api_key}'.encode()).decode()}"
        }
    )

    if response.status_code == 200:
        issue_data = response.json()
        description = issue_data["fields"]["description"].strip("\n").split()
        comment = issue_data["fields"]["comment"]["comments"][0]["body"]
        print(comment)
        exit()

    else:
        print(f"ERROR: JIRA cannot not be found. Status code: {response.status_code}")
        exit()

    return description

def collecting_ids(single_string):
    
    search_id =  None
    splitted_single_string_size_list = [8, 4, 4, 4, 12]

    if len(single_string) == 6:
        if single_string.isdigit():
            search_id = single_string
    elif len(single_string) == 22:
        if bool(re.match('^[A-Z0-9]+$', single_string)):
            search_id = single_string        
    elif len(single_string) == 36:
        if bool(re.match('^[a-z0-9-]+$', single_string)):
            splitted_single_string = single_string.split("-")
            if len(splitted_single_string) == 5:
                for single_splitted_single_string in splitted_single_string:
                    if len(single_splitted_single_string) != splitted_single_string_size_list[splitted_single_string.index(single_splitted_single_string)]:
                        break
                    search_id = single_string

    return search_id