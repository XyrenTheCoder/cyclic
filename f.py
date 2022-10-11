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

def search(arg, flag=None):
    if flag == None:
        result = grep(dirs, arg)
        count = grep(dirs, arg, c=True)
    elif flag == "w":
        result = grep(dirs, arg, w=True)
        count = grep(dirs, arg, w=True, c=True)
    elif flag == "i": #ignore case
        result = grep(dirs, arg, w=True, i=True)
        count = grep(dirs, arg, w=True, i=True, c=True)
    elif flag == "x": #exact searching
        result = grep(dirs, arg, w=True, x=True)
        count = grep(dirs, arg, w=True, x=True, c=True)
    elif flag == "ix" or flag == "xi":
        result = grep(dirs, arg, x=True, i=True)
        count = grep(dirs, arg, x=True, i=True, c=True)
    elif flag == "iw" or flag == "wi":
        result = grep(dirs, arg, w=True, =True, i=True)
        count = grep(dirs, arg, w=True, i=True, c=True)
    elif flag == "wx" or flag == "xw":
        result = grep(dirs, arg, w=True, x=True)
        count = grep(dirs, arg, w=True, x=True, c=True)
    elif len(flag) > 2:
        result = "Search: FlagError: Too many flags."
        count = "No"
    else:
        result = "Search: FlagError: No such flag(s)."
        count = "No"
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
    elif a == "seek":
        b = input("Seek for: ")
        result, count = searchx(b)
        if count == 1: print(f"{count} result found:\n{result}")
        else: print(f"{count} results found:\n"+"\n".join(result))
    elif "search" in a:
        s = a.split()
        tar = s[1]
        if len(s) < 3: flag = None
        else: flag = s[2]
        result, count = search(tar, flag)
        print(f"{count} results found:\n"+"\n".join(result))
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
