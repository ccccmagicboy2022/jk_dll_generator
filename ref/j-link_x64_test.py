#!d:\cccc2020\TOOL\python-3.9.1-embed-amd64\python.exe

import sys
sys.path.append('test')
sys.path.append('pylink')

import os
from test import ABC
import jlink

print(sys.path)

def init_jlink(dllname: str):
    #jlink initial

    dllpath = os.path.join(os.getcwd(), dllname)
    print(dllpath)

    jlk = jlink.JLink(lib=jlink.library.Library(dllpath=dllpath))
    jlk.open()
    print(jlk.product_name)
    print(jlk.connected())
    print(jlk.target_connected())
    jlk.set_tif(jlink.enums.JLinkInterfaces.SWD)
    jlk.connect(chip_name='STM32F103CB', speed=4000)
    print(jlk.target_connected())
    print(jlk.version)

def main():
    init_jlink('JLink_x64_v4.92.0.0.dll')
    #init_jlink('JLink_x64_v6.32.0.0.dll')
    init_jlink('JLink_x64_v7.0.0.0.dll')
    init_jlink('JLink_x64_v7.58.5.0.dll')
    init_jlink('JLink_x64_v7.60.5.0.dll')
    init_jlink('JLink_x64_v7.60.8.0.dll')

if __name__ == '__main__':
    print('bingo')
    main()


