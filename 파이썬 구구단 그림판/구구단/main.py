inputData=input()
if inputData.find('*')!=-1:    # ���࿡ *�� ������
    inputData=inputData.split("*")  #*�� �������� ���� �ΰ��� �߶󳽴�.
else:  #  *�� ���ٸ�
    inputData=inputData.split(" ")  # �����̽��� �������� �� ���ڸ� �߶󳽴�.

result=int(inputData[0])*int(inputData[1])    #��Ʈ�� Ÿ������ ���� ���� ��Ʈ������ ���� ��ȯ�Ŀ� ���Ͽ� result�� ����

print (inputData[0]+"*"+inputData[1]+"="+str(result))    # ������� ���
