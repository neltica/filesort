chStr=''
ch=''
chIndex=0
errflag=0

def error():
    global errflag
    if not errflag:
        print("FAIL")
        errflag=1

def pa():
    global chStr
    global chIndex
    global ch
    if ch=='a':
        ch=chStr[chIndex]
        chIndex+=1
    else:
        error()

def pb():
    global chStr
    global chIndex
    global ch
    if ch=='b':
        ch=chStr[chIndex]
        chIndex+=1
    else:
        error()

def pS():
    global ch
    if ch == 'a':
        pa()
        pA()
        pb()
    else:
        error()


def pA():
    global ch
    def aMethod():
        pa()
        pS()

    def bMethod():
        pb()
    switch={'a':aMethod,'b':bMethod}
    try:
        switch[ch]()
    except KeyError as msg:
        error()


def main():
    global chStr
    global chIndex
    global ch
    global errflag
    chStr=input()
    ch=chStr[chIndex]
    chIndex+=1
    pS()
    if not errflag and ch=='$':
        print("OK")
    else:
        error()

if __name__ == '__main__':
     main()
