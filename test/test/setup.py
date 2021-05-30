#!/usr/bin/python3

import os
import pip
import distro

os.system("mkdir /usr/bin/passman")

def install_pkg(package):
    if hasattr(pip , 'main'):
        pip.main(['install' , package])
    else:
        pip._internal.main(['install', package])


install_pkg('pyfiglet')
install_pkg('cryptography')

dist = distro.id()

if dist == "arch":
    os.system("pacman -S sqlite")

elif dist == "ubuntu":
    os.system("apt-get install sqlite3 libsqlite-dev")

elif dist == "debian":
    os.system("apt-get install sqlite3")



