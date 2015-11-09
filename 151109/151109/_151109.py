import sqlite3
from werkzeug import check_password_hash, generate_password_hash

#con = sqlite3.connect("test.db")
#cur = con.cursor()
#con.isolation_level = None
##dropsql = '''drop table if exists phonebook;'''
##cur.execute(dropsql)
##sql = '''create table if not exists phonebook(name text, phoneNum text);'''
##cur.execute(sql)

##insertsql = '''insert into phonebook values('greenjoa1','010-1111-2222');'''
##cur.execute(insertsql)
##name = 'greenjoa2'
##phoneNumber = '010-3333-4444'
##insertsql = '''insert into phonebook values(?,?);'''
##cur.execute(insertsql,(name,phoneNumber))

###cur.fetchone() : �ϳ� �������� �״����� �� ȣ��� �� ���� ���ڵ� ��ȸ

##name='greenjoa3'
##phoneNumber='010-3333-3333'
##insertsql='''insert into phonebook values(:inputName, :inputNum);'''
##cur.execute(insertsql,{"inputNum":phoneNumber, "inputName":name})

##insertsql = '''insert into phonebook values(?,?);'''
##datalist = (('greenjoa4','010-4444-4444'),('greenjoa5','010-5555-5555'))
##cur.executemany(insertsql,datalist)

##def dataGenerator():
##    datalist = (('greenjoa6','010-6666-6666'),('greenjoa7','010-7777-7777'))
##    for item in datalist:
##        yield item
##cur.executemany(insertsql,dataGenerator())

##insertsql = '''insert into phonebook values('Greenjoa55','010-1111-2222');'''
##cur.execute(insertsql)
##insertsql = '''insert into phonebook(phoneNum) values('010-9999-9999');'''
##cur.execute(insertsql)
##con.commit()

#def OrderFunc(str1,str2):
#    s1=str1.upper()
#    s2=str2.upper()
#    return (s1>s2)-(s1<s2)
#con.create_collation('myordering',OrderFunc)
#checksql = '''select * from phonebook order by name collate myordering;'''
#cur.execute(checksql)

#for row in cur:
#   # print(cur.fetchone())
#    print(row)
#    print(row[0])

#cur.execute('select count(*) from phonebook')
#print(cur.fetchone()[0]) #Ʃ�ð���
#cur.execute('select count(name) from phonebook')
#print(cur.fetchone()[0])

#sql = '''create table if not exists user(name text, age int);'''
#cur.execute(sql)
#insertsql = '''insert into user values(?,?);'''
#datalist = (('abc',22),('def',25),('gjijk',30))
#cur.executemany(insertsql,datalist)

#checksql = '''select max(age) from user;'''
#cur.execute(checksql)
#print(cur.fetchone()[0])

#class Average:
#    def __init__(self):
#        self.sum=0
#        self.cnt=0
#    def step(self,value):
#        self.sum+=value
#        self.cnt+=1
#    def finalize(self):
#        return self.sum/self.cnt

#con.create_aggregate("avg",1,Average)

#checksql = '''select avg(age) from user;'''
#cur.execute(checksql)
#print(cur.fetchone()[0])


########register, login

def init_db():
    #db=get_db()
    #with open('schema.sql') as f :
    #    db.cursor().executescript(f.read())
    #    db.commit()
    db = sqlite3.connect("test.db")
    cur = db.cursor()

    dropsql = '''drop table if exists user;'''
    cur.execute(dropsql)
    sql = '''create table user(
user_no integer primary key autoincrement,
userid string not null,
username string not null,
userpw string not null
);'''
    cur.execute(sql)

def get_db():
    db = sqlite3.connect("test.db")
    return db;

def register():
    init_db()

    print("******회원가입******")
    print("user ID : ",end="")
    userid = input()
    print("user name: ",end="")
    username = input()
    print("user passwd : ",end="")
    userpasswd = input()

    db=get_db()
    cur = db.cursor()
    checksql = '''select * from user where userid=(?);'''
    cur.execute(checksql,[userid])

    if cur.fetchone() != None :
        print("아이디존재")
    else :
        userpasswd = generate_password_hash(userpasswd)
        insertsql = '''insert into user(userid, username, userpw) values(?,?,?);'''
        cur.execute(insertsql,[userid, username, userpasswd])
        print("회원가입 완료\n")
        checksql = '''select * from user where userid=?;'''
        cur.execute(checksql,[userid])
        print(cur.fetchall())

    db.commit()


def login():
    print("******로그인******")
    print("user ID : ",end="")
    userid = input()
    print("user passwd : ",end="")
    userpasswd = input()
    userpasswd = generate_password_hash(userpasswd)
    db=get_db()
    cur = db.cursor()

    checksql = '''select * from user where userid=?;'''
    cur.execute(checksql,[userid])
    
    if cur.fetchone() == None:
        print("아이디 존재하지 않음")
    else :
        checksql = '''select userpw from user where userid=?;'''
        cur.execute(checksql,[userid])
        if cur.fetchone() == userpasswd :######################need to modify
            print(cur.fetchone())
            print(userpasswd)
            print("로그인성공")
        else :
            print(cur.fetchone())
            print(userpasswd)
            print("로그인실패")
    
    db.commit()
    db.close()


           
def main():


    register()
    login()

main()
    