# hacking simulator game
# made by: Omar Ashraf
#------------------------

# packages:
import time

# vars:
cmdsls = '''
    "help": "Lists you some commands to try.",
    "servers": "lists you how many server you can acsess.",
    "networks": "lists you how many networks you can acsess.",
    "sniff": "tells you packets data in a network. (must be used in a network)",
    "level": "tells you what level you are for now.",
    "hackn":"hack a network.",
    "hacks": "hack a server.",
    "buy": "buy an amount of nodes to generate money. syntax: $buy [amount]",
    "nodes": "shows you details about your nodes.",
    "clear": "cleans the terminal.",
    "connect": "connects you to a server or a network.",
    "home": "get back to the home directory"
'''
directory = '\033[32m[home /] $\033[0m'
nodes = 0
level = 1
endss = False
networks = ["mywifi", "homewifi", "wifi4family"]
servers = ["boblox", "n00dles", "yugiduelsmaster", "fortnight", "pizz@"]
loading = "{----------}\n LOADING...\n{----------}"
# functions:
def clear():
    print("\n" * 50)

# main:
print(" /\/\/\/\/\/\/ \n ============= \n terminal.exe \n ============= \n enter 'help' for a list of commands.")

while endss == False:
    commandreq = input("{}".format(directory))
    #cls
    if commandreq.lower() == "clear" or commandreq.lower() == "cls":
        clear()
        print(" /\/\/\/\/\/\/ \n ============= \n terminal.exe \n ============= \n enter 'help' for a list of commands.")
    elif commandreq.lower() == "networks":
        if len(networks) != 0:
            print("\033[32mnetworks:\033[0m \n {}".format(networks))
        else:
            print("there are no networks for now, to acsess.")
    #servers
    elif commandreq.lower() == "servers":
        if len(servers) != 0:
            print("\033[32mservers:\033[0m \n {}".format(servers))
        else:
            print("there are no servers for now, to acsess.")
    #hacks
    elif "hacks" in commandreq.lower() and len(commandreq.split()) > 1:
        server_target = commandreq.split()[1]
        if server_target in servers:
            if directory == "\u001b[32m[{} /] $\u001b[0m".format(server_target):
                op = input("are you sure that you want to hack this server? Y/N: ")
                if op.lower() == "y":
                    print(loading)
                else:
                    pass     
            else:
                print("please connect to that server so you can hack it...")
        else:
            print("this server does not exist...")
    #help
    elif commandreq.lower() == "help":
        print('\033[32m{}\033[0m'.format(cmdsls))
    #connect
    elif "connect" in commandreq.lower() and len(commandreq.split()) > 1:
            if any(server in directory for server in servers):
                print("please, disconnect from the server you are connected to.")
            else:
                if any(server in commandreq for server in servers):
                    directory = "\u001b[32m[{} /] $\u001b[0m".format(commandreq.split()[1])
                else:
                    print("this server does not exist...")
    elif commandreq.lower() == "connect":
        print("please, enter the server name that you would like to connect...")
    elif len(commandreq.lower().split()) > 1 and commandreq.lower().split()[1] not in str(servers):
        print("please, enter a vaild server name to connect...")
    #home
    elif commandreq.lower():
        if directory != '\033[32m[home /] $\033[0m':
            directory = '\033[32m[home /] $\033[0m'
        else:
            print('\033[32myou are already in the home directory...\033[0m')
    #error handle
    else:
        if commandreq != "":
            print('\033[31mcommand {} not found\033[0m'.format(commandreq))
