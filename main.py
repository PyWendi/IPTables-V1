# from functions import *
from loop_function import *

    
""" 
1 - Rule management
2 - Incomming and outgoing traffic management
3 - NAT management
4 - Advanced command

I - RULE MANAGEMENT
_1-Adding iptable rule
_2-Delete iptable rule
_3-Adding specific rule 
_4-Listing rules with existing chains
_5-Listing all general rules
_6-Save rules
_7-Load rules

II - I/O TRAFFIC MANAGEMENT
_1-A/B specific IP
_2-A/B specific Port
_2-A/B specific IP and Port

III - NAT MANAGEMENT
_1-Outbound traffic
_2-Forward traffic

IV - ADVANCED COMMAND
_1-Chain creation
_2-Rule with custom chain
_3-Connection limitation
_4-Ip Spoofing protection
_5-ICMP limitation
"""

""" -------MAIN PROGRAM------- """

print("-------IPTABLE CLI V1--------")

running = True

while(running):
    print("Here are the available commands : ")
    print("1 - Rule management\n2 - Incomming and outgoing traffic management\n3 - NAT Management\n4 - Advanced Command\n\n0 - To leave the application")
    selection = input("\nPlease select one of the above options : ")
    
    if (selection.isdigit()) and (int(selection) in range(0,5)):
        selection = int(selection)
        if selection == 0:
            print("\nClosing the application...")
            break
        
        # Handling first option
        elif selection == 1: 
            print("\n--RULE MANAGEMENT--")
            while True:
                if FirtsOperation():
                    break
                    
        # Handling second option
        elif selection == 2:
            print("\n--INCOMING AND OUTGOING TRAFFIC MANAGEMENT--")
            while True:
                if SecondOperation():
                    break
        
        # handling third option
        elif selection == 3:
            print("\n--NAT MANAGEMENT--")
            while True:
                if ThirdOperation():
                    break
        
        # handling the fourth option
        elif selection == 4:
            print("\n--ADVANCED COMMAND--")
            while True:
                if FourthOperation():
                    break
    else:
        print("Incorrect value, please insert the number specified above !!\n")

