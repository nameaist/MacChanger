import subprocess

def change_mac(interface , new_mac):
    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw" , "ether" , new_mac])
    subprocess.call(["ifconfig" , interface , "up"])
    result = subprocess.check_output(["ifconfig" , interface]).decode()
    print(result)

