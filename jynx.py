import platform
import os
import time
logo = (""" \u001b[37m
     ██╗██╗   ██╗███╗   ██╗██╗  ██╗
     ██║╚██╗ ██╔╝████╗  ██║╚██╗██╔╝
     ██║ ╚████╔╝ ██╔██╗ ██║ ╚███╔╝ 
██   ██║  ╚██╔╝  ██║╚██╗██║ ██╔██╗ 
╚█████╔╝   ██║   ██║ ╚████║██╔╝ ██╗
 ╚════╝    ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝\x1b[38;5;196mv0.1\u001b[37m""")
def linex():
     print('===========================================')
def clear():
  os.system('clear')
  print(logo)
clear()
linex()
print('\n\x1b[1;37m\033[1;32;40m>>\x1b[1;97m CHECKING FOR UPDATES \x1b[1;37m')
bit = platform.architecture()[0]
if bit == '64bit': print('\x1b[1;37m\033[1;32;40m>>\x1b[1;97m 64 BIT FOUND \x1b[1;37m')
if bit == '32bit':
  print('\x1b[1;37m\033[1;32;40m>>\x1b[1;97m 32 BIT FOUND \x1b[1;37m')
if bit == '16 bit': 
  print('\x1b[1;37m\033[1;32;40m>>\x1b[1;97m 16 BIT FOUND \x1b[1;37m')
  print('\x1b[1;96m>>\x1b[1;97m STARTING JYNX GREEN \x1b[1;37m')
  time.sleep(3)
os.system('git pull --quiet')
os.system('python jynapi.so')

login()
