
#task1,print a list of all interface names associated with VLAN IDs

fin = open("config.txt")
lines = fin.readlines()
for i in range(len(lines)):
    wordlist = lines[i].split()
    for word in wordlist:
        if "vlan" == word:
            print(lines[i])
            print(lines[i+1])
    
#task2,replaces IP addresses

import os
def sed(pattern_string,replacment_string,f1,f2):
    f_1 = open(f1)
    f_2 = open(f2,'w')

    for line in f_1:
        if pattern_string in line:
            newline = line.replace(pattern_string,replacement_string)
            f_2.write(newline)
        else:
            f_2.write(line)
    return f_2


pattern_string = "172"
replacement_string = "192"
f1="config.txt"
f2="new_configtxt"

print(sed(pattern_string,replacement_string,f1,f2))

#task3,Create a Python dictionary of all access lists configured in the firewall
access_name=["transit_access","global_access","xcompany-lan_access_","management2_access_","sharedresource_access_","SomeProducts_access_","fw-management_access_","WirelessHotspot_access_","voicevlan_access_","WirelessClients_access_"]

def accesslist(filename):
    d = {}
    fin = open(filename)
    for line in fin:
        wordlist = line.strip()
        for item in access_name:
            if item in wordlist:
                d[item] = [line]
    return d

print(accesslist("config.txt"))                  
