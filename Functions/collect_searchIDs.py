import re

print(f"INFO: Searching for Booking IDs, Basket IDs and Session IDs.")

def checkString(single_string):
    
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


def collectIDs(jira_description, jira_comments):

    collected_ID_List = []

    total_string_list = jira_description + jira_comments

    for single_string in total_string_list:
        search_id = checkString(single_string)
        if search_id is not None:
            collected_ID_List.append(search_id)
    print(f"INFO: Searching for Booking IDs, Basket IDs and Session IDs has been completed.")
    if len(collected_ID_List) == 0:
        print("Warning: Unable to find Booking IDs, Basket IDs and Session IDs from {jira_id}.")
        exit()
    else:
        return collected_ID_List