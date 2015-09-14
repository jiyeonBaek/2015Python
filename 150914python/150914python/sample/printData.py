def printData(data,level=0):
    for item in data:
        if isinstance(item,list):#item�� list�̸�
            printData(item,level+1)
        else:
            for steps in range(level):
                print("\t",end="")
            print(item)