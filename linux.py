import subprocess
import argparse
import re 


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i" , "--interface" , dest="interface" , help = "Specify interface name")

    options = parser.parse_args()

    if not options.interface:
        parser.error("[-] Specify interface name")
    
    return options.interface

def change_mac(interface , new_mac):
    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw" , "ether" , new_mac])
    subprocess.call(["ifconfig" , interface , "up"])
    result = subprocess.check_output(["ifconfig" , interface]).decode()
    print(result)


if __name__ == "__main__":
    interface = get_arguments()
    change_mac(interface , "aa:aa:aa:aa:aa:aa")