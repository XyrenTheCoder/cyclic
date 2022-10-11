from datetime import datetime

initial = datetime.now()

global starttime, starth, startm, starts

starttime = initial.strftime("%H:%M:%S")
starth = int(initial.strftime("%H"))
startm = int(initial.strftime("%M"))
starts = int(initial.strftime("%S"))

def uptime():
    getnow = datetime.now()
    t = getnow.strftime("%H:%M:%S")
    return t
    
def welcome():
    if starth >= 12:
        return f"Good afternoon, {user}!"
    else:
        return f"Good morning, {user}!"

def ...
