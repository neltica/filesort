ch=''    #문자열을 저장하는 글로벌 변수입니다.
errflag=0      # 과제에 있던 errFlag

def error():
    global errflag          #글로벌로 변수를 사용하려면 선언해야합니다.
    if not errflag:         #만약 errflag가 true면 FAIL을 출력하고
        print("FAIL")
        errflag=1            #errfalg=1을 대입합니다.

def pa(chIndex):            #ch는 문자열이기 때문에 몇번째 인덱스를 참조하는지 알기위해선 인자값으로 chIndex를 가져야합니다.
    global ch                 #마찬가지 글로벌 변수 선언
    if ch[chIndex]=='a':            #현재인덱스가 a이면
        return chIndex+1             #인덱스+1를 리턴합니다.
    else:
        error()                  #ch 현재 인덱스가 a가 아니면 에러를 출력한다.
        return chIndex           #chIndex를 +1없이 리턴한다.

def pb(chIndex):                  # pa함수와 마찬가지입니다. 단지 a가 b로 변경되기만 했습니다.
    global ch
    if ch[chIndex]=='b':
        return chIndex+1
    else:
        error()
        return chIndex

def pS(chIndex):
    global ch
    if ch[chIndex] == 'a':
        chIndex=pa(chIndex)         #현재인덱스가 a이면 pa함수를 호출합니다.(현재인덱스를 넘겨줘야합니다.)    pa가 호출된후에 chIndex를 리턴해줍니다.
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



ch=input()            #입력값을 받습니다. 파이썬 기본 입력함수인 input()은 문자열을 기본으로 합니다. (파이썬 기본 타입에 char타입이 없는걸로 압니다.)
chIndex=pS(0)             #ch의 인덱스 0부터 참조를 시작하도록 하여 pS()함수를 호출합니다.
if not errflag and ch[chIndex]=='$':                     #만약 errflag가 False이고 pS()함수를 거친 ch의 마지막 인덱스 값이 $이면 OK를 리턴합니다.
    print("OK")
else:
    error()                                #충족이 안되면 error()를 호출합니다.
