#This i an web app directory scanner

import requests 
import sys #important!

sub_list = open("wordlist.txt").read() #wordlist in the same directory 
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,dir_enum)
