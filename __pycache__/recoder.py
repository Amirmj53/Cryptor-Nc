
import design
from colorama import Fore as color
from time import sleep
import os
import sys

#######################
bold = '\033[1m'
unbold = '\033[0m'
#######################




# try:
#     os.system("clear")
#     design.rec_menu()
#     option = int(input(bold+color.RED+"\n[*] " + color.LIGHTMAGENTA_EX +
#                      " NC.cryptor" + color.WHITE + "/Decoder/" + color.RED + "⇒  "))
#     if option == 1:
#         os.system("clear")
#         design.banner()
#         print(bold + color.RED + "Enter the Base64 to text : ")
#         user_inp = input(bold+color.RED+"[*] " + color.LIGHTMAGENTA_EX +
#                          "NC.cryptor" + color.LIGHTWHITE_EX + "/Decoder/Base64" + color.RED + "⇒  ")
#         print(bold+color.WHITE + "Text :  :\n ")
#         os.system(f"echo {user_inp} | base64 -b ")
#         input(bold + color.LIGHTGREEN_EX + "Press Any Key ...")
        

# except:
#     pass





def decoder_menu(user_inp):
    if user_inp == 1 :
        os.system("clear")
        design.banner()
        print(bold + color.RED + "Enter the Base64 to text : ")
        user_option = input(bold+color.RED+"[*] " + color.LIGHTMAGENTA_EX +
                            "NC.cryptor" + color.LIGHTWHITE_EX + "/Decoder/Base64/" + color.RED + " → ")
        print(bold+color.WHITE + "Encrypted :\n ")
        os.system(f"echo {user_option} | base64 -d")
        input(bold + color.LIGHTGREEN_EX + "Press Any Key ..." +unbold)
        
    elif user_inp == 2 :
        os.system("clear")
        design.banner()
        print(bold + color.RED + "Enter the Hex to text : ")
        user_option = input(bold+color.RED+"[*] " + color.LIGHTMAGENTA_EX +
                            "NC.cryptor" + color.LIGHTWHITE_EX + "/Decoder/Hex/" + color.RED + " → ")
        print(bold+color.WHITE + "Encrypted :\n ")
        os.system(f"echo {user_option} | xxd -p -r")
        input(bold + color.LIGHTGREEN_EX + "Press Any Key ..." +unbold)
    
    elif user_inp == 0 :
        pass
    else:
        print (bold+color.RED+ "Bad input ...")
        sleep(2)
        sys.exit();os.system("clear")