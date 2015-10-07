#list1=[1,2,3,4]
#list2=[0]
#list3=[""]
#list4=[]
#list5=[1]
#print(dir(list1))
#print(any(list1))
#print(any(list2))
#print(any(list3)) #0은 false
#print(any(list4))
#print(any(list5))

####

#def positive(l):
#    return l%2==0

#print(list(filter(lambda a:a%2==0,[1,-3,2,-4,0,6])))

#####

#a=3
#print(id(3))
#print(id(a)) #같은아이디

#####

#a=[1,2,3]
#b=list(a)
#c=a
#print(b)
#print(id(a))
#print(id(b))
#print(id(c))

####
#def two_times(x): return x*2

#print(map(two_times,[1,2,3,4]))
#print(list(map(two_times,[1,2,3,4])))

####


#print(eval(repr("hi".upper())))
##eval(str("hi".upper())) 오류

#####

#listA=[5,6,87,10,12]
#data=list.sort(listA)
#print(data) 
#print(sorted(listA)) #원본데이터순서는바뀌지안흠

#####

#listB=list(zip("abc","def"))
#print(listB)

###

data={"홍길동" : [80,70,60,92],
      "김길동" : [24,35,18,10],
      "고길동" : [10,20,8,5]
      }
for i in data.values():
    list.sort(i)

print(data["고길동"])

#listA=[]
#n=0
#for j in data.keys():
#    listA[n]=j
#    n+=1
#list.sort(listA)

#for i in sorted(data):
#    print(i.values())