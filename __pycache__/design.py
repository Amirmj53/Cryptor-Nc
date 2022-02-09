from colorama import Fore as color
from time import sleep

bold = '\033[1m'
unbold = '\033[0m'


def banner():
    print(bold+color.RED+"""
  _   _  ____   ____                  _             
 | \ | |/ ___| / ___|_ __ _   _ _ __ | |_ ___  _ __ 
 |  \| | |    | |   | '__| | | | '_ \| __/ _ \| '__|
 | |\  | |___ | |___| |  | |_| | |_) | || (_) | |   
 |_| \_|\____(_)____|_|   \__, | .__/ \__\___/|_|   
                          |___/|_|                v1.01
                                     Hex | Base64         
    """+unbold)
    print(bold+color.WHITE+"""
-------------------------
| Developer : Mmd        |
| Ig : _.mjko._          |
| Tm : @NebulouR         |
--------------------------
    """+unbold)
    sleep(0.5)


def menu():
    print(bold+color.YELLOW+"[01]" +bold+color.LIGHTGREEN_EX+ " Base64")
    print(color.CYAN+"****************")
    sleep(0.1)
    print(bold+color.YELLOW+"[02]" +bold+color.LIGHTGREEN_EX+ " Hex")
    print(color.CYAN+"****************")
    sleep(0.1)
    print(bold+color.YELLOW+"[03]" +bold+color.LIGHTGREEN_EX+ " Decoder")
    print(color.CYAN+"****************")
    sleep(0.1)
    print(bold+color.YELLOW+"[0]" +bold+color.LIGHTGREEN_EX+ " Exit" +unbold)
    

# banner()    
# menu()


def rec_menu():
    print(bold+color.YELLOW+"[01]" +bold+color.LIGHTGREEN_EX+ " Base64")
    print(color.CYAN+"****************")
    sleep(0.1)
    print(bold+color.YELLOW+"[02]" +bold+color.LIGHTGREEN_EX+ " Hex")
    print(color.CYAN+"****************")
    sleep(0.1)
    print(bold+color.YELLOW+"[0]" +bold+color.LIGHTGREEN_EX+ " Back" +unbold)
    