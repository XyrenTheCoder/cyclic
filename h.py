import os, sysfrom grepfunc import grep

                result, count = search(tar, flag)
            print(f"{count} results found:\n"+"\n".join(result))
        except TypeError: pass
        except MissingRequiredArgument: print("Search: MissingRequiredArgument: Missing 1 or more arguments.")
    elif trim == "clear": clear()
    elif trim == "exit": exit()
    elif trim == "cwd": print(os.getcwd())
    elif trim == "history":
        d = -1
        e = history()
        for g in e:
            d += 1
            print(f"{d}{(6 - len(str(d))) * ' '} {g.strip()}")
    elif trim == "uptime":
        uh, um, us = uptime()
        print(f"{uh}h {um}m {us}s")
    elif trim == "debug":
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
        c += 1
        print(f"{c}-{uptime()}")
        c += 1
        print(f"{c}-{history()}")
    else: print(f"System: Invalid command: {trim}")
