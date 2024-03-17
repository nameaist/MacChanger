import argparse
import random
from sys import platform
import pyuac
import win 
import linux

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" , "--interface" , dest="interface" , help = "Specify interface name")

    options = parser.parse_args()

    if not options.interface:
        print("[-] Specify interface name")
        
        return ""
     
    return options.interface

def gen_random_mac():
    res = ""
    for i in range(5):
        res += hex(random.randint(0x10 , 0xff))[2:] + ":"
    res += hex(random.randint(0x10 , 0xff))[2:]

    return res


if __name__ == "__main__":
    interface = get_arguments()
    if interface == "":
        exit(0)

    new_mac = gen_random_mac()

    if platform == "linux" or platform == "linux2":
        linux.change_mac(interface , new_mac)

    elif platform == "win32":
        new_mac = new_mac.replace(":" , "")

        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
        else:
            win.change_mac(interface , new_mac)

    else:
        print("[-] Unsupported platform")
