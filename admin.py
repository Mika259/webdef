import os
import time

os.system("clear")
os.system("apt install figlet");os.system("clear");os.system("figlet Enter Code")

time.sleep(1)
print("Login to Use Tool (CTRL+Z) for stopped")
time.sleep(0.5)

#username/password here
user = "user123"
passwd = "pass123"


username = input("[+] Username :")
os.system("clear");os.system("figlet Enter Code")
print("..searching username..")
time.sleep(1)
if username == user:
    print("Founded !")
    time.sleep(0.5)
    os.system("clear");os.system("figlet Enter Code")
    password = input("[+] Password :")
    time.sleep(0.5)

topping = """
                    <W><E><B>_<D><E><F>
                       Author : Mika259
                       Github : https://github.com/Mika259/webdef
               
*Disclaimer!,These tools can only be used on webdav websitesdo not use this tool to do evil and illegal activities...

[1] start
[0] Exit
"""    
    
if username != user:
    print("no name found")
    os.system("python3 admin.py")
    
    
if password == passwd:
    print("Success Login")
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print(topping)
    time.sleep(1)
    run = input("[+] Enter :")
    if run == '1':
        time.sleep(0.5)
        os.system("python2 webdef.py")
    if run != '1':
        exit()
    
if password != passwd:
    print("Password Failed Login")
    print ("try again later")
    time.sleep(1)
    os.system("python3 admin.py")