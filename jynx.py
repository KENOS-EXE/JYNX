import os, platform, time, sys
os.system('xdg-open https://www.facebook.com/profile.php?id=100084565670977')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('\033[1;91m[\033[1;32;40m-\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet ')
bit = platform.architecture()[0]
if bit == "64bit":
 print('\033[1;91m[\033[1;32;40m✓\033[1;91m] \033[1;97m64Bit Found')
 from jynapi import login
 login()
 
 
 
elif bit == "32bit":
 print('\033[1;91m[\033[1;32;40m✓\033[1;91m] \033[1;97m32Bit Found')
 from jynapi import login
 login()
