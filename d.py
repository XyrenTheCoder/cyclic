import os, sys
from grepfunc import grep
from datetime import datetime

cwd = os.getcwd()
dirs = os.listdir(cwd)
initial = datetime.now()

#global starttime, starth, startm, starts, user
starttime = initial.strftime("%H:%M:%S")
starth = int(initial.strftime("%H"))
startm = int(initial.strftime("%M"))
starts = int(initial.strftime("%S"))
user = "test0"

def ctime():
    getnow = datetime.now()
    t = getnow.strftime("%H:%M:%S")
    return t
    
def welcome():
    if starth >= 12:
        return f"Good afternoon, {user}!"
    else:
        return f"Good morning, {user}!"

def check():
    result = grep(dirs, "Plugins", w=True)
    return result
    
def main(): ...
    
    
