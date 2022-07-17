import os
os.system('clear')
os.system('pip install colorama')
os.system('clear')
os.system('apt update && apt upgrade')
from colorama import init
from colorama import Back,Fore,Style
init()
os.system('clear')

print(Fore.RED + '''
        mmmm                 #      m
        #   "m  mmm    m mm  #   m  #
        #    # "   #   #"  " # m"   #                              #    # m"""#   #     #"#    #
        #mmm"  "mm"#   #     #  "m  #mmmmm
             gui by agent
''' + Fore.WHITE)
print('''
        0.vim(code editor)
        1.php
        2.rust
        3.c
        4.c++
        5.java
    ''')

q = int(input('>'))

if q == 0:
    os.system('clear')
    os.system('pkg install vim')
if q == 1:
    os.system('clear')
    os.system('pkg install php')
if q == 2:
    os.system('clear')
    os.system('pkg install php')
if q == 3:
    os.system('clear')
    os.syatem('pkg install gcc')
if q == 4:
    os.system('clear')
    os.syatem('pkg install clang')
if q == 5:
    os.system('clear')
    os.system('pkg install wget && wget https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava')
