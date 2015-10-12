import sys
import os
import pickle
import shutil
#os.system("python test.py 1 2 3")
#print(sys.path)

#class student:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def show(self):
#        print(self.name," : ", self.age)

#s1=student("학생1",23)
#s1.show()
#f=open("file1.txt",'wb')
#pickle.dump(s1,f)
#f.close

#f=open("file1.txt",'rb')
#data=pickle.load(f)
#print(data)
#data.show()


#print(os.getcwd())


##현재디렉토리에샘플디렉토리 / 하위디렉토리파일중txt파일 샘플에 복사ㄴ
##os.mkdir('sample1')
#list1=list(os.walk("."))
#list2=[]
#n=0
#for i in list1 :
#    print(i)
#    for j in i:
#       print(j)
#        # list2[n]=j
#       # n+=1
#print(list2)

#    #if list2[1]=='txt':
#    #   shutil.copy(i,i)

os.path.dirname('.')