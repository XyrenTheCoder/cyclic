import os, sys
from grepfunc import grep
from datetime import datetime

idir = os.getcwd()
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

#def check():
#    result = grep(dirs, "Plugins", w=True, x=True)
#    return result
    
def search(arg):
    result = grep(dirs, arg, w=True, x=True)
    count = grep(dirs, arg, w=True, x=True, c=True)
    return result, count

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def inc(): c += 1
     
def main():
    global a
    a = input(">>> ")
    return a, main()
   
while True:
    if a == "time": print(ctime())
    elif a == "search":
        b = input("Search for: ")
        print(search(b))
    elif a == "clear": clear()
    elif a == "cwd": print(os.getcwd())
    elif a == "debug":
        c = 0
        print(f"{c}-{ctime()}")
        inc()
        print(f"{c}-{search(sys.argv[0])}")
        inc()
        print(f"{c}-{idir}")
        inc()
        print(f"{c}-{dirs}")
        inc()
        print(f"{c}-{starttime}")
        inc()
        print(f"{c}-{a}")
        #inc()
    else: print(f"System: Invalid command: {a}")
