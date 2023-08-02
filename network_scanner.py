


import argparse
from tabnanny import verbose
import scapy.all as scapy

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Target IP")
    options = parser.parse_args()
    if not options.target:
        parser.error("Type the target")
    return options

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combo = broadcast/arp_req
    ans = scapy.srp(combo, timeout=1 , verbose= False)[0]  #two ans [0] specifies the required answer
    
    client_list =[]
    for element in ans:
        client_dict={"ip":element[1].psrc, "mac":element[1].hwsrc}         #dictionary 2nd element from ans
        client_list.append(client_dict)
    return client_list

def print_result(results_list):
     print("IP\t\t\tMAC Address\n-------------------------------------------------")
     for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])

options=get_args()
scan_result=scan(options.target)
print_result(scan_result)
