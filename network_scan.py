#arp scan, use carefull
#install scapy when error : apt install python3-scapy

from scapy.all import * 

interface = "eth0" 
ip_range = "192.168.0.1/24" #replace it with your IP and CIDR
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))     
