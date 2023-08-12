import subprocess


"""
Managing Iptables Rules (simple rules)

"""

# Adding iptable rule
def add_iptables_rule(chain, rule):
    command = ['sudo', 'iptables', '-A', chain] + rule.split()
    try:
        output = subprocess.run(command, check=True)
        print(output)
        print("Rule added successfully :)")
    except subprocess.CalledProcessError as e:
        print("Error : ",e)

# Deleting iptable rule
def delete_iptables_rule(chain, rule):
    command = ['sudo', 'iptables', '-D', chain] + rule.split()
    try:
        output = subprocess.run(command, check=True)
        print(output)
        print("Rule deleted successfully :)")
    except subprocess.CalledProcessError as e:
        print("Error : ",e)

# Adding rule with a specific port
def iptable_custom_rule(chain, protocol, port, target):
    command = ["sudo", "iptables", "-A", chain, "-p", protocol, "--dport", port, "-j", target]
    output = subprocess.run(command, check=True)
    print(output)
    print("Custom rule added successfully :)")

# Listing all rules with a specific (INPUT, OUTPUT, FORWARD,...)
def list_iptables_rules(chain):
    command = ['sudo', 'iptables', '-L', chain, '-n', '-v']
    output = subprocess.check_output(command, universal_newlines=True)
    print(output,"\n")

# Listing all rules regardless of chains
def list_general_rule():
    cmd = ["sudo", "iptables", "-L"]
    output = subprocess.run(cmd, check=True)
    print(output,"\n")


"""

Managing incomming and outgoing trafic through a specific
IP adress

Chain : INPUT, OUTPUT, FORWARD

"""

BASE_COMMAND = ["sudo", "iptables"]

# Creatig rule with specific parameter (here ipsource)
# @chain, protocol, ipsource, target
def AllowOrBlockFromSpecificIp(chain, protocol, ipSource, target):
    cmd = BASE_COMMAND + ["-A", chain, "-p", protocol, "-s", ipSource, "-j", target]
    output = subprocess.run(cmd, check=True)
    print("Specific rule with IP Adress Added")
    print(output)
    
# Adding a rule with specific parameters (here port)
# @chain, protocol, port, target
def AllowOrBlockFromSpecificPort(chain, protocol, port, target):
    cmd = BASE_COMMAND + ["-A", chain, "-p", protocol, "--dport", port, "-j", target]
    output = subprocess.run(cmd, check=True)
    print("Specific rule with PORT Added")
    print(output)

# Adding a rule with specific IP and Port
# @chain, protocol, ipsource, port, target
def AllowPacketFromSpecificIpAndPort(chain, protocol, ipSource, port, target):
    command = ["sudo", "iptables", "-A", chain, "-p", protocol, "--dport", port, "-j", target]
    output = subprocess.run(command, check=True)
    print("Specific rule with IP Adress AND PORT Added")
    print(output)
    

""" 

Managing NAT system
NAT is used to map private IP addresses to a public IP address when packets leave your internal network. This is commonly done for internet access.

"""

# To enable NAT for outbound traffic
# @out_interface : output interface such as eth0,...
def EnableNATForOutboundTraffic(out_interface):
    cmd = BASE_COMMAND + ["-t","nat","-A", "POSTROUTING", "-o", out_interface, "-j", "MASQUERADE"]
    output = subprocess.run(cmd, check=True)
    print("NAT Outbounding traffic enable")
    print(output)

# To forward incoming traffic on a specific port to a machine within your internal network
# @in_interface, protocol, external_port, internal_port
def EnableNATForPortForwardTraffic(in_interface, protocol, external_port, internal_ip, internal_port):
    try:
        cmd = BASE_COMMAND + ["-t", "nat", "-A", "PREROUTING", "-o", in_interface, "-p", protocol, "-dport", external_port, "-j", "DNAT", "--to-destination", internal_ip+":"+internal_port]
        output = subprocess.run(cmd, check=True)
        print("NAT Outbounding traffic enable")
        print(output)
    except subprocess.CalledProcessError as e:
        print("Error : ", e)


"""

Saving rules configution

"""

def SaveRulesInAFile(filename):
    cmd = ["sudo", "iptables-save", ">", filename]
    output = subprocess.run(cmd, check=True)
    print(f"Rules saved inside '{filename}' file.")
    print(output)
    
def restoreRulesInAFile(filename):
    cmd = ["sudo", "iptables-restore", "<", filename]
    output = subprocess.run(cmd, check=True)
    print(f"Rules Restored from '{filename}' file.")
    print(output)



""" 

Advanced command

"""

# Create a custom chain
# @chain_name
def create_chain(chain_name):
    cmd = BASE_COMMAND + ["-N", chain_name]
    subprocess.run(cmd, check=True)
    print("Chain created !")
    
# To add a rule that references the custom chain
# @chain, custom_chain
def rule_with_custom_chain(chain, custom_chain):
    try:
        cmd = BASE_COMMAND + ["-A", chain, "-j", custom_chain]
        subprocess.run(cmd, check=True)
        print("Rule added with custom chain.")
    except subprcess.CalledProcessError as e:
        print("Error : ",e)
        
# connection limitation limiting 
# @ chain ,protocol, port, seconds, hitcount
def connection_limitation(chain ,protocol, port, seconds, hitcount):
    cmd1 = BASE_COMMAND + ["-A", chain, "-p", protocol, "--dport", port, "-m", "state", "--state", "NEW", "-m", "recent", "--update", "--seconds", seconds, "--hitcount", hitcount, "-j", "DROP"]
    cmd2 = BASE_COMMAND + ["-A", chain, "-p", protocol, "--dport", port, "-m", "state", "--state", "NEW", "-m", "recent", "--set","-j", "ACCEPT"]
    output1 = subprocess.run(cmd1, check=True)
    output2 = subprocess.run(cmd2, check=True)
    print("Connection rate limitation set.")
    
# To prevent source IP address spoofing by blocking packets from reserved private address ranges
# @interface, ipsource (with mask, tag form like 192.0.0.0/16)
def ip_spoofing_protection(interface, ipsource):
    cmd = BASE_COMMAND + ["-A", "INPUT", "-i", interface, "-s", ipsource, "-j", "DROP"]
    output = subprocess.run(cmd, check=True)
    print("IP Spoofing Protection set !")
    
# To limit the rate of incoming ICMP requests (ping)
# @rate_per_seconds
def ping_limitation(rate_per_seconds):
    cmd = BASE_COMMAND + ["-A", "INPUT", "-p", "icmp", "--icmp-type", "echo-request", "-m", "limit", "--limit", rate_per_seconds+"/second", "-j", "ACCEPT"]
    ouptut = subprocess.run(cmd, check=True)
    print("ICMP request(ping) rate limitation set.")
