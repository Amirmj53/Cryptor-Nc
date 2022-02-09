import os
import sys
import design
import recoder
from colorama import Fore as color
from time import sleep

#####################################

bold = '\033[1m'
unbold = '\033[0m'

try:
    from colorama import Fore
except:
    print("install the colorama library")


while True:
    try:
        os.system("clear")
        design.banner()
        design.menu()
        option = int(input(bold+color.RED+"\n[*] " + color.LIGHTMAGENTA_EX +
                    " NC.cryptor" + color.WHITE + "/Home/" + color.RED + "⇒  "))
        if option == 1:
            os.system("clear")
            design.banner()
            print(bold + color.RED + "Enter the text : ")
            user_inp = input(bold+color.RED+"[*] " + color.LIGHTMAGENTA_EX +
                            "NC.cryptor" + color.LIGHTWHITE_EX + "/Home/Base64/" + color.RED + " → ")
            print(bold+color.WHITE + "Encrypted :\n ")
            os.system(f"echo {user_inp} | base64")
            input(bold + color.LIGHTGREEN_EX + "Press Any Key ...")
            continue
        elif option == 2:
            os.system("clear")
            design.banner()
            print(bold + color.RED + "Enter the text : ")
            user_inp = input(bold+color.RED+"[*] " + color.LIGHTMAGENTA_EX +
                            "NC.cryptor" + color.LIGHTWHITE_EX + "/Home/Hex/" + color.RED + " → ")
            print(bold+color.WHITE + "Encrypted :\n ")
            os.system(f"echo {user_inp} | xxd -p")
            input(bold + color.LIGHTGREEN_EX + "Press Any Key ...")
            continue
        elif option == 3:
            os.system("clear")
            design.banner()
            design.rec_menu()
            user_inp = int(input(bold+color.RED+"\n[*] " + color.LIGHTMAGENTA_EX +
                    " NC.cryptor" + color.WHITE + "/Decoder/" + color.RED + " → "))
            recoder.decoder_menu(user_inp)
            continue
        else:
            sleep(2)
            sys.exit()
    except:
        os.system("clear")
        sys.exit()