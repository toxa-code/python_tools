#a simple ICMP Port Scanner in Python
#use carefully

import sys
import socket

print ("Scanning Ports...")

ip = f"{sys.argv[1]}" 
open_ports =[] 

ports = range(1,65535) #feel free to change range


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports: ") 
  print (sorted(open_ports)) 
else: 
  print ("Seems like no Ports are open, try harder! :(")
