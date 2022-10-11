import os, sys
from grepfunc import grep
from datetime import datetime

class FlagError(Exception): pass
class MissingRequiredArgument(Exception): pass
class ArgumentError(Exception): pass
    
idir = os.getcwd()
dirs = os.listdir(idir)
initial = datetime.now()

#global starttime, starth, startm, starts
starttime = initial.strftime("%H:%M:%S")
starth = int(initial.strftime("%H"))
startm = int(initial.strftime("%M"))
starts = int(initial.strftime("%S"))

def ctime():
    getnow = datetime.now()
    t = getnow.strftime("%H:%M:%S")
    return t

def search(arg, flag=None):
    try:
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
            result = grep(dirs, arg, w=True, i=True)
            count = grep(dirs, arg, w=True, i=True, c=True)
        elif flag == "wx" or flag == "xw":
            result = grep(dirs, arg, w=True, x=True)
            count = grep(dirs, arg, w=True, x=True, c=True)
        elif len(flag) > 2:
            raise ArgumentError
        else:
            raise FlagError
        return result, count
    except ArgumentError: print("Search: ArgumentError: Too many flags.")
    except FlagError: print("Search: FlagError: No such flag(s).")
    
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def history():
    f = open("history.txt", "r")
    lines = f.readlines()
    e = []
    for i in lines:
        e.append(i)
    return e
    
def main():
    global a
    a = input(">>> ")
    f = open("history.txt", "a")
    f.write(f"{a}\n")
    f.close()
    return a

while True:
    main()
    if a == "time": print(ctime())
    elif "search" in a:
        try:
            s = a.split()
            if len(s) < 2: raise MissingRequiredArgument
            elif len(s) < 3:
                tar = s[1]
                result, count = search(tar)
            else:
                tar = s[1]
                flag = s[2]
                result, count = search(tar, flag)
            print(f"{count} results found:\n"+"\n".join(result))
        except TypeError: pass
        except MissingRequiredArgument: print("Search: MissingRequiredArgument: Missing 1 or more arguments.")
    elif a == "clear": clear()
    elif a == "cwd": print(os.getcwd())
    elif a == "history":
        d = -1
        e = history()
        for g in e:
            d += 1
            print(f"{d}    {g.strip()}")
    elif a == "debug":
        global c
        c = 0
        print(f"{c}-{ctime()}")
        c += 1
        print(f"{c}-{search(sys.argv[0])}")
        c += 1
        print(f"{c}-{idir}")
        c += 1
        print(f"{c}-{dirs}")
        c += 1
        print(f"{c}-{starttime}")
        c += 1
        print(f"{c}-{a}")
    else: print(f"System: Invalid command: {a}")
