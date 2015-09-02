#print("Here are the num! {0:d},{1:4d}. ".format(7,8))
#ctrl+kc : 주석처리 ku : 주석해제

#salary=int(input("Please enter your salary : "))
#bonus =int(input("Please enter your bonus : "))
#paycheck = salary + bonus
#paycheck2=float(salary) + float(bonus)
#print(paycheck)
#print(paycheck2)
#print(type(paycheck))

#num=5.67
#print(round(num,0))

#print("""HHH rrr fff""")

name = "greenjoa"
print(name[0],name[-2]) 
#-2는 뒤에서부터 두번째
print(name[0:6])

info = "201311216greenjoa"
sid=info[:9]
sname = info[9:]
print(sid+" "+sname)

a1="I eat %10s apples."%"five"
a2="I eat %-10s apples."%"five"
print(a1,a2)

exit=input("종료할까요? : " ).lower()
print(exit)