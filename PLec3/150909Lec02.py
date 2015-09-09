Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dic1={}
>>> dic2=dict()
>>> dic={'name':'pey','phone':'01011112222','birth':'1214'}
>>> a={1:'hi'}
>>> b={'a',[1,2,3]}
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b={'a',[1,2,3]}
TypeError: unhashable type: 'list'
>>> b={'a':[1,2,3]}
>>> print(dic['name']_
      
SyntaxError: invalid syntax
>>> print(dic['name'])
pey
>>> del a['name']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    del a['name']
KeyError: 'name'
>>> a[2]='b'
>>> a['name']='pey'
>>> a[3]=[1,2,3]
>>> del a['name']
>>> a={'name':'pey','phone':'01012341234','birth':'1212'}
>>> b=a.keys()
>>> print(b)
dict_keys(['birth', 'name', 'phone'])
>>> b=list(a.keys())
>>> print(b)
['birth', 'name', 'phone']
>>> b=a.items()
>>> print(b)
dict_items([('birth', '1212'), ('name', 'pey'), ('phone', '01012341234')])
>>> a.get('name')
'pey'
>>> movie={'홍길동':{'베테랑':5.0,'암살':4.5},'고길동':{'베테랑':4.0,'암살':5.0},'둘리':{'밀양':4.5,'베테랑':4.5}}
>>> a.get('홍길동')
>>> print(a.get('홍길동'))
None
>>> print(movie.get('홍길동'))
{'암살': 4.5, '베테랑': 5.0}
>>> mname=movie.get('홍길동')
>>> print(mname)
{'암살': 4.5, '베테랑': 5.0}
>>> print(mname.get('암살'))
4.5
>>> movie('홍길동')('암살')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    movie('홍길동')('암살')
TypeError: 'dict' object is not callable
>>> movie['홍길동']['암살']
4.5
>>> answer=input("Would you like express shipping?")
Would you like express shipping?yes
>>> if answer=="yes":
	print("That will be an extra $10")

	
That will be an extra $10
>>> answer=answer.lower()
>>> if answer=="yes"
SyntaxError: invalid syntax
>>> if answer=="yes":
	print("ppp")

	
ppp
>>> a=[(1,2),(3,4),(5,6)]
>>> for (first,last)in a:
	print(first+last)

	
3
7
11
>>> for i in range (2,9):
	for j in range(1,9):
		print(i*j,end=" ")
	print(")
	      
SyntaxError: EOL while scanning string literal
>>> i=2
>>> j=3
>>> print(i,j)
2 3
>>> print(i,j,end= i*j)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(i,j,end= i*j)
TypeError: end must be None or a string, not int
>>> print(i,j)
2 3
>>> print(i,j,end=)
SyntaxError: invalid syntax
>>> print(i,j,end="")
2 3
>>> for i in range(2,9):
	fir j in range(1,9):
		
SyntaxError: invalid syntax
>>>  for i in range(2,9):
	for j in range(1,9):
		
SyntaxError: unexpected indent
>>> for i in range(2,9):
	for j in range(1,9):
		print('%d * %d = %d'%(i,j,i*j))

		
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
>>> for i in range(2,9):
	for j in range(1,9):
		print('%d * %d = %d'%(i,j,i*j),end=" ")

		
2 * 1 = 2 2 * 2 = 4 2 * 3 = 6 2 * 4 = 8 2 * 5 = 10 2 * 6 = 12 2 * 7 = 14 2 * 8 = 16 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 3 * 4 = 12 3 * 5 = 15 3 * 6 = 18 3 * 7 = 21 3 * 8 = 24 4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 4 * 5 = 20 4 * 6 = 24 4 * 7 = 28 4 * 8 = 32 5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 5 * 6 = 30 5 * 7 = 35 5 * 8 = 40 6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 6 * 7 = 42 6 * 8 = 48 7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 7 * 8 = 56 8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 
>>> for i in range(2,9):
	for j in range(1,9):
		print('%d * %d = %d'%(i,j,i*j),end=" ")
	print("")

	
2 * 1 = 2 2 * 2 = 4 2 * 3 = 6 2 * 4 = 8 2 * 5 = 10 2 * 6 = 12 2 * 7 = 14 2 * 8 = 16 
3 * 1 = 3 3 * 2 = 6 3 * 3 = 9 3 * 4 = 12 3 * 5 = 15 3 * 6 = 18 3 * 7 = 21 3 * 8 = 24 
4 * 1 = 4 4 * 2 = 8 4 * 3 = 12 4 * 4 = 16 4 * 5 = 20 4 * 6 = 24 4 * 7 = 28 4 * 8 = 32 
5 * 1 = 5 5 * 2 = 10 5 * 3 = 15 5 * 4 = 20 5 * 5 = 25 5 * 6 = 30 5 * 7 = 35 5 * 8 = 40 
6 * 1 = 6 6 * 2 = 12 6 * 3 = 18 6 * 4 = 24 6 * 5 = 30 6 * 6 = 36 6 * 7 = 42 6 * 8 = 48 
7 * 1 = 7 7 * 2 = 14 7 * 3 = 21 7 * 4 = 28 7 * 5 = 35 7 * 6 = 42 7 * 7 = 49 7 * 8 = 56 
8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64 
>>> a=[1,2,3,4]
>>> result=[]
>>> result=[num*3 for num in a if num%2==0]
>>> print(result)
[6, 12]
>>> result=[x*y for x in range(2,10)
	for y in range(1,10)]
>>> print(result)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
>>> import turtle
>>> for steps in range(4):
	turtle.forward(100)
	turtle.right(90)

	
>>> for steps in range(5):
	turtle.forward(100)
	turtle.right(90)

	
>>> for steps in range(5):
	turtle.forward(100)

	
>>> for steps in range(5):
	turtle.right(90)

	
>>> for steps in range(4):
	turtle.forward(100)
	turtle.right(90)
	for moresteps in range(4)
	
SyntaxError: invalid syntax
>>> for steps in range(4):
	turtle.forward(100)
	turtle.right(90)
	for moresteps in range(4):
		turtle.forward(50)
		turtle.right(90)

		



>>> for steps in range(4):
	turtle.forward(100)
	turtle.right(90)
	for moresteps in range(4):
		turtle.forward(50)
		turtle.right(90)

		
>>> nSides=5
>>> for steps in range(nSides):
	turtle.forward(100)
	turtle.right(360/nSides)
	for moresteps in range(nSides):
		turtle.forward(50)
		turtle.right(360/nSides)

		
>>> for steps in range(nSides):
	turtle.forward(100)
	turtle.right(360/nSides)

	
>>> for steps in ['red','blue','green','black']:
	turtle.color(steps)
	turtle.forward(100)
	turtle.right(90)

	
>>> prompt="""
1.Add
2.Del
3.List
4.Quit

Enter number : """
>>> number=0
>>> while number!=4:
	print(prompt, end="")
	number = int(input())

	

1.Add
2.Del
3.List
4.Quit

Enter number : 0

1.Add
2.Del
3.List
4.Quit

Enter number : 1

1.Add
2.Del
3.List
4.Quit

Enter number : 2

1.Add
2.Del
3.List
4.Quit

Enter number : 3

1.Add
2.Del
3.List
4.Quit

Enter number : 4
>>> 
