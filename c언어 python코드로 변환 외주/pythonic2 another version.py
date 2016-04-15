ch=''
errflag=0

def error():
    global errflag
    if not errflag:
        print("FAIL")
        errflag=1

def pa(chIndex):
    global ch
    if ch[chIndex]=='a':
        return chIndex+1
    else:
        error()
        return chIndex

def pb(chIndex):
    global ch
    if ch[chIndex]=='b':
        return chIndex+1
    else:
        error()
        return chIndex

def pS(chIndex):
    global ch
    if ch[chIndex] == 'a':
        chIndex=pa(chIndex)
        chIndex=pA(chIndex)
        chIndex=pb(chIndex)
        return chIndex
    else:
        error()


def pA(chIndex):
    global ch
    if ch[chIndex]=='a':
        chIndex=pa(chIndex)
        chIndex=pS(chIndex)
        return chIndex
    elif ch[chIndex]=='b':
        chIndex=pb(chIndex)
        return chIndex
    else:
        error()



ch=raw_input()
chIndex=pS(0)
if not errflag and ch[chIndex]=='$':
    print("OK")
else:
    error()
