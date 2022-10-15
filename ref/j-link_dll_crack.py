import os
from win32api import GetFileVersionInfo, LOWORD, HIWORD

def get_version_number (filename):
  info = GetFileVersionInfo (filename, "\\")
  ms = info['FileVersionMS']
  ls = info['FileVersionLS']
  return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)

DLL_FILE = "JLinkARM.dll"
DLL_FILE_OUTPUT = "JLinkARM_CV.dll"
byte_list = []

with open(DLL_FILE, "rb") as f1:
    byte_list = list(f1.read())
    for i in range(len(byte_list)):
        if 0x88 == byte_list[i]:
            if 0x13 == byte_list[i+1]:
                if 0x85 == byte_list[i-17]:
                    if 0xC0 == byte_list[i-16]:
                        if 0x75 == byte_list[i-15]:
                            if 0x6A == byte_list[i-13]:
                                if 0x01 == byte_list[i-12]:
                                    print("find 5s dialog limit!!!")
                                    print(f'magic byte locate at {i-15}')
                                    byte_list[i-15] = 0xEB
                                    print(f'crack magic byte to {byte_list[i-15]}')

    for i in range(len(byte_list)):
        if 0x30 == byte_list[i]:
            if 0x75 == byte_list[i+1]:
                if 0x85 == byte_list[i-17]:
                    if 0xC0 == byte_list[i-16]:
                        if 0x75 == byte_list[i-15]:
                            if 0x6A == byte_list[i-13]:
                                if 0x01 == byte_list[i-12]:
                                    print("find 30s debug limit!!!")
                                    print(f'magic byte locate at {i-15}')
                                    byte_list[i-15] = 0xEB
                                    print(f'crack magic byte to {byte_list[i-15]}')

ver_str = ".".join ([str (i) for i in get_version_number (DLL_FILE)])
#print(ver_str)
name, ext = os.path.splitext(DLL_FILE)
DLL_FILE_OUTPUT = name + '_v' + ver_str + ext
#print(DLL_FILE_OUTPUT)

if os.path.isfile(DLL_FILE_OUTPUT):
    print('file exist!')
    os.remove(DLL_FILE_OUTPUT)
    print('del file!')

with open(DLL_FILE_OUTPUT,"wb+") as f2:
    f2.write(bytearray(byte_list))
    print(f'{DLL_FILE_OUTPUT} new file ok!')


