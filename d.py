import os, sys
from grepfunc import grep
from datetime import datetime

idir = os.getcwd()
dirs = os.listdir(idir)
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

#def check():
#    result = grep(dirs, "Plugins", w=True, x=True)
#    return result
    
def searchx(arg):
    result = grep(dirs, arg, w=True, x=True)
    count = grep(dirs, arg, w=True, x=True, c=True)
    return result, count

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")
     
def main():
    global a
    a = input(">>> ")
    return a
   
while True:
    main()
    if a == "time": print(ctime())
    elif a == "searchx":
        b = input("Search for: ")
        result, count = searchx(b)
        print(f"{count} results found:\n{result}")
    elif a == "clear": clear()
    elif a == "cwd": print(os.getcwd())
    elif a == "debug":
        global c
        c = 0
        print(f"{c}-{ctime()}")
        c += 1
        print(f"{c}-{searchx(sys.argv[0])}")
        c += 1
        print(f"{c}-{idir}")
        c += 1
        print(f"{c}-{dirs}")
        c += 1
        print(f"{c}-{starttime}")
        c += 1
        print(f"{c}-{a}")
    else: print(f"System: Invalid command: {a}")
