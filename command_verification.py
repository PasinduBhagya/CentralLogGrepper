argument_rules = []

def command_verification(arguments):
  
  if "--help" in arguments:
    print('''Usage: This tool can be use to collect logs from from compressed log files and share it with the Developers. 

  Options and arguments.

    --help\t: Print this help message and exit.
    --jira-id\t: ID of the JIRA. Only use if the search strings are given in the description. 
    --comment-id\t: ID of the comment. Use when the search strings are given in a comment. Must specify the jira_id option as well.
    --date\t: Date that developers requesting Logs. 
    --string\t: Use if you required to search a string randomly. 

  If you need any other support, please contact Pasindu Bhagya - pasindub@codegen.net.
  ''')
    exit()

  for single_argv in arguments:
    if single_argv[0] and single_argv[1] == "-":
      argument_rules.append(single_argv)

  if any(element not in ["--help", "--jira-id", "--comment-id", "--date", "--string"] for element in argument_rules):
    print('''\nError: Invalid arguments provided.\n''')
    exit()

  if "--date" not in arguments:
    print("ERROR: Please mention the --date parameter.")
    exit()
  else:
    if "--jira-id" not in arguments and "--string" not in arguments:
      print(arguments)
      print("ERROR: Please mention --jira-id or --string parameters.")
      exit()
    else:
      if "--comment-id" in arguments and "--jira-id" not in arguments:
        print("ERROR: Please mention the --jira-id parameter with --comment-id")
        exit()
