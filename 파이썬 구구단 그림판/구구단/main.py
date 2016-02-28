inputData=input()
if inputData.find('*')!=-1:    # 만약에 *가 있으면
    inputData=inputData.split("*")  #*을 기준으로 숫자 두개를 잘라낸다.
else:  #  *이 없다면
    inputData=inputData.split(" ")  # 스페이스를 기준으로 두 숫자를 잘라낸다.

result=int(inputData[0])*int(inputData[1])    #스트링 타입으로 들어온 값을 인트값으로 각각 변환후에 곱하여 result에 대입

print (inputData[0]+"*"+inputData[1]+"="+str(result))    # 결과값을 출력
