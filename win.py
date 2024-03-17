import winreg as wrg
import subprocess
import win32api
import ctypes

template = "SYSTEM\\CurrentControlSet\\Control\\Class\\{4D36E972-E325-11CE-BFC1-08002BE10318}"

def enum_subkeys(open_key):
    i = 0
    res = []
    while True:
        try:
            curr_sub_key = wrg.EnumKey(open_key , i)
            res.append(curr_sub_key)
            i += 1
        except OSError:
            break
    return res

def change_mac(interface , new_mac):
    location = wrg.OpenKeyEx(wrg.HKEY_LOCAL_MACHINE , template)
    sub_keys = enum_subkeys(location)

    find_sub_key_handle = 0

    for sub_key in sub_keys:
            
        sub_key_handle = wrg.OpenKeyEx(location , sub_key , access= 131097 | wrg.KEY_SET_VALUE)
        interface_name = wrg.QueryValueEx(sub_key_handle , "DriverDesc")[0]

        if (interface_name == interface):
            find_sub_key_handle = sub_key_handle
            break

        wrg.CloseKey(sub_key_handle)
    

    if find_sub_key_handle == 0:
        raise Exception("No interface with such name found error")
    
    wrg.SetValueEx(find_sub_key_handle , "NetworkAddress" , 0 , wrg.REG_SZ , new_mac)
    wrg.CloseKey(find_sub_key_handle)


    ctypes.windll.user32.MessageBoxW(0 , "Success. Need to restart computer to aply changes" , 0 , 1)






