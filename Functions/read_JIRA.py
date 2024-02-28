import requests
import base64
from configparser import ConfigParser

config = ConfigParser()
config.read('./configurations.cfg')

# Loading JIRA parameters
jira_url = config.get('JIRA_PARAMETERS', 'JIRA_URL')
jira_username = config.get('JIRA_PARAMETERS', 'JIRA_USERNAME')
jira_api_key = config.get('JIRA_PARAMETERS', 'JIRA_API_KEY')


def read_jira(jira_id):

    comment_id=0
    comments = []
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
        print(issue_data["fields"]["description"])
        description=[]
        try:
            description = issue_data["fields"]["description"].strip("\n").split()
        except:
            print(f"Error: Nothing found on the description on {jira_id}")
        while True:
            try:
                comment = issue_data["fields"]["comment"]["comments"][comment_id]["body"]
                comments.append(comment)
            except:
                break
            comment_id += 1
    else:
        print(f"ERROR: JIRA cannot not be found. Status code: {response.status_code}")
        exit()
    print(f"INFO: JIRA Reading completed.")
    return description, comments