import time
class MidTest:
    id=""
    name=""
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def question1(self):
        print("1) 학번 : {0}, 이름 : {1}".format(self.id,self.name))
    def question2(self,list1,count):
        zerolist=[0]
        list2=zerolist*count
        x=sorted(list1.values())
        print(x)
        for j in range(0,count):
            print(j)
            for i in list1.keys():
                if list1[i]==x[-1-j]:
                    print(x[-1-j])
                    print(i,list1[i])
                    dic={}
                    dic[i]=list1[i]
                    list2[j]=dic
        print("2) ",list2)
    #def question3(self,fileName):

    #    fileName1="1.txt"
    #    fileName2="2.txt"
    #    with open(fileName, "wb") as myFile :
    #        with open(fileName1, "r") as myFile1 :

    @classmethod
    def question5(self):
        t1=time.strftime("%Y.%m.%d %X",time.localtime())
        print("5) ",t1)

        



greenjoa=MidTest("201311216","백지연")
greenjoa.question1()
data={"명량":4.5, "베테랑":4.0,"암살":4.6,"마션":4.3}
greenjoa.question2(data,3)
MidTest.question5()
