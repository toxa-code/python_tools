#Subdomain Enumeration with Python
#on Linux use "pyinstaller" , convert an Windows exe with "py2exe"

import os,requests,sys

'''file = f"{sys.argv[1]}" #use it if you have a path
path=os.getcwd() + file
'''

sub_list = open("subdomains.txt").read() #repleace it with filename in sa directory

subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" #change to [2] whe path
try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)
