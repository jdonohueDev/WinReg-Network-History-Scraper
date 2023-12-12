# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:35:36 2023

@author: James
"""
#printNets

#windows key + r key => regedit for directory reference

import winreg
aReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
aKey = winreg.OpenKey(aReg, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged')
print(r"*** Reading from %s ***" % aKey)
print('[*] Networks You Have Joined.')

for i in range(1024):
    try:
        aValue_name = winreg.EnumKey(aKey, i)
        oKey = winreg.OpenKey(aKey, aValue_name)
        sValue = winreg.QueryValueEx(oKey, "FirstNetwork")
        mValue = winreg.QueryValueEx(oKey, "ProfileGuid")
        print('[+] ' + sValue[0] + ' \t\t\t\t\t\t\t' + mValue[0])
    except EnvironmentError:
        break