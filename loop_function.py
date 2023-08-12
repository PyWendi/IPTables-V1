"""

Function settiing here are designed to handle option loop inside selected option

"""

from functions import *


""" First option handled """

def FirtsOperation():
    print("Please select one of the options below : ")
    print("1 - Add a rule\n2 - Delete a rule\n3 - Add a specific rule\n4 - Listing rules with existing chains\n5 - Listing all general rules\n6 - Save rules in a file\n7 - Load rules from a file\n0 - Return to the main menu")
    choice = input("\nYour choice : ")
    
    if (choice.isdigit() and (int(choice) in range(0,8))):
        choice = int(choice)
        
        if (choice == 0):
            return True
        
        elif choice == 1:
            print("__Adding rules__")
            chains = ["INPUT", "OUTPUT", "FORWARD"]
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            rule = input("Write your rule")
            if (chain.isdigit() and (chain in range(1,4))):
                chain = chains[int(chain) - 1]
                
                # Calling main function
                add_iptables_rule(chain, rule)
            else:
                print("Wrong input!!")
            
        elif choice == 2:
            print("__Deleting rule__")    
            chains = ["INPUT", "OUTPUT", "FORWARD"]
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            rule = input("Write your rule : ")
            
            if (chain.isdigit() and (int(chain) in range(1,4))):
                chain = chains[int(chain) - 1]
                
                # Calling main function
                delete_iptables_rule(chain, rule)
            else:
                print("Wrong input!!")
        
        elif choice == 3:
            print("__Adding custom iptables__")
            chains = ["INPUT", "OUTPUT", "FORWARD"]
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            if chain.isdigit() and (int(chain) in range(1,4)):
                chain = chains[int(chain) - 1]
            else :
                chain = chains[0]
            protocol = input("Please select a protocol : ").lower()
            port = input("enter a port of your choice : ")
            target = input("Enter a target (like ACCEPT, DROP, REJECT,...) : ")
            
            # Calling main function
            iptable_custom_rule(chain, protocol, port, target)
        
        elif choice == 4:
            print("__Listing Rules with a specific chain")
            chain = input("Enter the chain : ").upper()
            list_iptables_rules(chain)
        
        elif choice == 5:
            list_general_rule()
            
        elif choice == 6:
            filename = input("Enter the name of the file to save rules : ")
            SaveRulesInAFile(filename)
            
        elif choice == 7:
            filename = input("Enter the name of the file to load stored rules : ")
            restoreRulesInAFile(filename)
        
        # Trigger the loop one more time
        return False
        
        
    else :
        print("Incorrect input, please choose a number between 0 and 7")
    
def SecondOperation():
    print("Please select one of the options below : ")
    print("1 - Add or Block packets from a specific IP adress\n2 - Add or Block packets from a specific PORT\n3 - Add or block packets from a specifi PORT and IP adress\n0 - Return to the main menu")
    choice = input("\nYour choice : ")
    chains = ["INPUT", "OUTPUT", "FORWARD"]
    targets = ["ACCEPT,", "DROP"]
    
    if (choice.isdigit() and (int(choice) in range(0,4))):
        choice = int(choice)
        
        if (choice == 0):
            return True
        
        elif choice == 1:
            print("__Managing I/O traffic from an IP adress__")
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            protocol = input("Enter aa protocol : ")
            ipSource = input("Enter the IP Adress : ")
            target = input("Select the target, 1-ACCEPT, 2-DROP : ")
            if (chain.isdigit() and (chain in range(1,4))):
                if target.isdigit() and int(target) in range(1,3):
                    chain = chains[int(chain) - 1]
                    target = targets[int(target) - 1]
                else:
                    print("Wrong input!!")    
                    return False
            else:
                print("Wrong input!!")
                return False
            
            # Calling main function
            AllowOrBlockFromSpecificIp(chain, protocol, ipSource, target)
        
        elif choice == 2:
            print("__Managing I/O traffic from an PORT__")
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            protocol = input("Enter aa protocol : ")
            port = input("Enter the PORT : ")
            target = input("Select the target, 1-ACCEPT, 2-DROP : ")
            if (chain.isdigit() and (chain in range(1,4))):
                if target.isdigit() and int(target) in range(1,3):
                    chain = chains[int(chain) - 1]
                    target = targets[int(target) - 1]
                else:
                    print("Wrong input!!")    
                    return False
            else:
                print("Wrong input!!")
                return False
            
            # Calling main function
            AllowOrBlockFromSpecificPort(chain, protocol, port, target)
        
        elif choice == 3:
            print("__Managing I/O traffic from an IP Adress and a PORT__")
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            protocol = input("Enter aa protocol : ")
            ipSource = input("Enter the IP Adress : ")
            port = input("Enter the PORT : ")
            target = input("Select the target, 1-ACCEPT, 2-DROP : ")
            if (chain.isdigit() and (chain in range(1,4))):
                if target.isdigit() and int(target) in range(1,3):
                    chain = chains[int(chain) - 1]
                    target = targets[int(target) - 1]
                else:
                    print("Wrong input!!")    
                    return False
            else:
                print("Wrong input!!")
                return False
            
            # Calling main function
            AllowPacketFromSpecificIpAndPort(chain, protocol, ipSource, port, target)
            
        # Trigger the loop one more time
        return False
        
    else :
        print("Incorrect input, please choose a number between 0 and 3")
    
def ThirdOperation():
    print("Please select one of the options below : ")
    print("1 - Manage Outbounding traffic\n2 - Manage Forwarding traffic\n0 - Return to the main menu")
    choice = input("\nYour choice : ")
    
    if (choice.isdigit() and (int(choice) in range(0,3))):
        choice = int(choice)
        
        if (choice == 0):
            return True
        
        elif choice == 1:
            print("__Managing outbounding traffic with NAT__")
            out_interface = input("Enter the output interface : ")
            
            # Calling main function
            EnableNATForOutboundTraffic(out_interface)
        
        elif choice == 2:
            print("__Managing forwarding traffic with NAT__")
            in_interface = input("Enter the input interface : ")
            protocol = input("Enter a protocol : ")
            external_port = input("Enter the external PORT : ")
            internal_port = input("Enter the internal PORT : ")
            internal_ip = input("Enter the internal IP adress : ")

            if external_port.isdigit() and internal_port.isdigit():
               
                # Calling main function 
                EnableNATForPortForwardTraffic(in_interface, protocol, external_port, internal_ip, internal_port)
            else:
                print("Wrong input!!")
                return False
            
        # Trigger the loop one more time
        return False
        
    else :
        print("Incorrect input, please choose a number between 0 and 2")
    
def FourthOperation():
    print("Please select one of the options below : ")
    print("1 - Creation of custom chain\n2 - Bind a rule with a custom chain\n3 - Connection limitation\n4 - IP Spoofing protection\n5 - ICMP (ping) limitation\n0 - Return to the main menu")
    choice = input("\nYour choice : ")
    chains = ["INPUT", "OUTPUT", "FORWARD"]
    
    if (choice.isdigit() and (int(choice) in range(0,6))):
        choice = int(choice)
        
        if (choice == 0):
            return True
        
        elif choice == 1:
            print("__Creation of a custom chain__")
            chain_name = input("Enter the custom chain name(in upper case) : ").upper()
            
            if (chain_name.digit() or chain_name.isalnum()):
                print("Please enter only alphabetical character !!")
            else:
                # Calling main function
                create_chain(chain_name)
        
        elif choice == 2:
            print("__Creation of rule which is binded with a custom chain__")
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            custom_chain = input("Please enter the custom chain name : ")
            
            if (chain.isdigit() and (chain in range(1,4))) and custom_chain.isalpha():
                chain = chains[int(chain) - 1]
                
                # Calling main function
                rule_with_custom_chain(chain, custom_chain)
            else:
                print("Wrong input!!")
                
                
        elif choice == 3:
            print("__Connection limitation__")
            chain = input("Please select a chain : 1-INPUT, 2-OUTPUT, 3-FORWARD : ")
            protocol = input("Enter a protocol : ")
            port = input("Enter a port : ")
            seconds = input("Enter the number of seconds to update connection : ")
            hitcount = input("Enter the number of hitcount to update connection : ")
            
            if (chain.isdigit() and (chain in range(1,4))) and port.isdigit() and seconds.isdigit() and hitcount.isdigit():
                chain = chains[int(chain) - 1]
                # Calling main function
                connection_limitation(chain, protocol, port, seconds, hitcount)
            else:
                print("Wrong input!!")
            
        elif choice == 4:
            print("__IP Spoofing protection__")
            interface = input("Enter the interface to block incomming packet : ")
            ipsource = input("Enter the IP/Network masked Adress to prevent spoofing (like 192.0.0.0/8) : ")
            
            if interface.isalnum():
                ip_spoofing_protection(interface, ipsource)
            else:
                print("Wrong input")
        
        
        elif choice == 5:
            print("__PING limitation__")
            rate_per_seconds = input("Enter the rate per second of incomming ICMP packet : ")
            
            if rate_per_seconds.isdigit():
                ping_limitation(rate_per_seconds)
            else:
                print("Wrong input")
                
            
        # Trigger the loop one more time
        return False
        
    else :
        print("Incorrect input, please choose a number between 0 and 5")