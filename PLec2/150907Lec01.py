Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = ['a', 'b', 'c', ['abcd', 'efg']]
>>> print(data[0])
a
>>> print(data[2][0])
c
>>> print(data[3][0])
abcd
>>> guests=['a','b','c','d']
>>> score=[78,85,62,49,98]
>>> print(guests[-3])
b
>>> a=[]
>>> b=[1,2,3]
>>> c=['Life','is','too','short']
>>> d=[1,2,'Life','is']
>>> e=[1,2,['Life','is']]
>>> b+c
[1, 2, 3, 'Life', 'is', 'too', 'short']
>>> b*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> guests[1:2]=['greenjoa1','greenjoa2']
>>> print(guests)
['a', 'greenjoa1', 'greenjoa2', 'c', 'd']
>>> guests[1:2]=['b','c']
>>> guests[1]=['greenjoa1','greenjoa2']
>>> print[guests]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print[guests]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(guests)
['a', ['greenjoa1', 'greenjoa2'], 'c', 'greenjoa2', 'c', 'd']
>>> print(guests.index('c'))
2
>>> print(guests.index('h'))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(guests.index('h'))
ValueError: 'h' is not in list
>>> guests.remove('c')
>>> print(guests)
['a', ['greenjoa1', 'greenjoa2'], 'greenjoa2', 'c', 'd']
>>> id=['wldus','qor','qorwldus']
>>> id.insert(1,1234)
>>> id.insert(3,5678)
>>> id.insert(5,1357)
>>> print(id)
['wldus', 1234, 'qor', 5678, 'qorwldus', 1357]
>>> id.insert(2,['Jiyeon','010-1234-5678'])
>>> print(id)
['wldus', 1234, ['Jiyeon', '010-1234-5678'], 'qor', 5678, 'qorwldus', 1357]
>>> id.insert(5,['Soyeon','010-1111-2222'])
>>> id.append(['JY','010-2222-3333'])
>>> print(od)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(od)
NameError: name 'od' is not defined
>>> print(id)
['wldus', 1234, ['Jiyeon', '010-1234-5678'], 'qor', 5678, ['Soyeon', '010-1111-2222'], 'qorwldus', 1357, ['JY', '010-2222-3333']]
>>> for steps in range(4):
	print(geusts[steps])

	
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    print(geusts[steps])
NameError: name 'geusts' is not defined
>>> for steps in range(4):
	print(guests[steps])

	
a
['greenjoa1', 'greenjoa2']
greenjoa2
c
>>> for guests in guests:
	print(guests)

	
a
['greenjoa1', 'greenjoa2']
greenjoa2
c
d
>>> guests=['a','b','c','d']
>>> nEntries=len(guests)
>>> for steps in range(nEntries):
	print(guests[steps])

	
a
b
c
d
>>> scores=[85,62,63,45,90]
>>> scores.sort()
>>> print(scores)
[45, 62, 63, 85, 90]
>>> scores.reverse()
>>> print(scores)
[90, 85, 63, 62, 45]
>>> #range는 인덱스로 많이 쓴다
>>> top3=[]
>>> for steps in range(3):
	top[steps]=scores[steps]

	
Traceback (most recent call last):
  File "<pyshell#59>", line 2, in <module>
    top[steps]=scores[steps]
NameError: name 'top' is not defined
>>> for steps in range(3):
	top3[steps]=scores[steps]

	
Traceback (most recent call last):
  File "<pyshell#62>", line 2, in <module>
    top3[steps]=scores[steps]
IndexError: list assignment index out of range
>>> top3=[1,2,3]
>>> for steps in range(3):
	top3[steps]=scores[steps]

	
>>> print(top3)
[90, 85, 63]
>>> is instance
SyntaxError: invalid syntax
>>> data=['a',['Hi','Hello'],'b']
>>> for steps in range(3):
	if isinstance(list)
	
SyntaxError: invalid syntax
>>> for steps in data(3):
	if isinstance(steps,list):
		for step in steps:
			print(step)
	else:
		print(steps)

		
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    for steps in data(3):
TypeError: 'list' object is not callable
>>> print(data)
['a', ['Hi', 'Hello'], 'b']
>>> for steps in data:
	if isinstance(steps,list):
		for step in steps:
			print(step)
	else:
		print(steps)

		
a
Hi
Hello
b
>>> scores=[85,63,63,45,90]
>>> scores.extend([50,60])
>>> print(scores)
[85, 63, 63, 45, 90, 50, 60]
>>> scores.append([10,20])
>>> print(scores)
[85, 63, 63, 45, 90, 50, 60, [10, 20]]
>>> scores.append(10,20)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    scores.append(10,20)
TypeError: append() takes exactly one argument (2 given)
>>> ssssssssss
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    ssssssssss
NameError: name 'ssssssssss' is not defined
>>> data
['a', ['Hi', 'Hello'], 'b']
>>> t1=()
>>> t2=(1,)
>>> t3=(1,2,3)
>>> t4=1,2,3
>>> t5=('a','b',('ab','cd'))
>>> t1
()
>>> t2
(1,)
>>> t3
(1, 2, 3)
>>> t4
(1, 2, 3)
>>> t5
('a', 'b', ('ab', 'cd'))
>>> 
