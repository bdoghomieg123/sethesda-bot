import time
import random
import os
import platform

#Clears output of terminal or command prompt depending on your Operating System.
def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
        time.sleep(1)
