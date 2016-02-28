__author__ = 'Nelician'

"""
python 3.x
"""

inputData=input()
if inputData.find('*')!=-1:
    inputData=inputData.split("*")
else:
    inputData=inputData.split(" ")

result=int(inputData[0])*int(inputData[1])

print str(inputData[0])+"*"+str(inputData[1])+"="+str(result)
