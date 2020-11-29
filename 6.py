def sortStringByChar(myData):
    myData.sort(reverse=True, key=len)
    return myData
myData = ['apel', 'rambutan', 'jeruk']
print(sortStringByChar(myData))
