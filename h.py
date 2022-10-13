import os, sys
from grepfunc import grep
from datetime import datetime

class FlagError(Exception): pass
class MissingRequiredArgument(Exception): pass
class ArgumentError(Exception): pass
    
idir = os.getcwd()
dirs = os.listdir(idir)
initial = datetime.now()

global starttime, starth, startm, starts
starttime = initial.strftime("%H:%M:%S")
starth = int(initial.strftime("%H"))
startm = int(initial.strftime("%M"))
starts = int(initial.strftime("%S"))

def ctime():
    global getnow
    getnow = datetime.now()
    t = getnow.strftime("%H:%M:%S")
    return t
