import re
import os
import glob
import urllib.request

str='''Window
Unix
Linux
Solaris'''
p = re.compile('^.+') #^: ó������ .:�ٹٲ��������� ��繮��, +: �ϳ��̻�
print(p.findall(str))
p = re.compile('^.+',re.M) 
print(p.findall(str))
p=re.compile('^.+',re.S) #M��������?
print(p.search(str))

m=re.match(r"(?P<first>\w+) (?P<last>\w+)","Malcolm Reynolds")
print(m.group('first','last'))
print(m.groups)

m=re.match(r"(\d+)\.?(\d+)?","24")
print(m.groups())
print(m.group(0))
print(m.groups(0)) #����Ʈ��

m=re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcolm Reynolds")
print(m.groupdict())

p=re.compile(".+:") #:�տ� �ϳ� �̻� �ƹ��ų� �ü��ִ�
m=p.search("http://google.com")
print(m.group()) # http:

p=re.compile(".+(?=:)")
m=p.search("http://google.com")
print(m.group()) #http

os.chdir("c:\\")
p=re.compile('.*[.](?!bat$|exe$).*$')
#print(p.search(glob.glob("*.*")))

p=re.compile("(?<=abc)def")
m=p.search("abcdef")
print(m.group())

m=re.search('(?<=-)\w+','spam-egg')
print(m.group())

email="tony@tiremove_thisger.net"
m=re.search("remove_this",email)
result=email[:m.start()]+email[m.end():]
print(m.start(),m.end())#r�� start, s�� end
print(result)

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' %(match.group(), match.groups())
valid = re.compile(r"^[a2-9tjqk]{5}$") # �ټ����� []���� ������ �������Ѵ�displaymatch(valid.match("akt5q"))
displaymatch(valid.match("akt5e"))
displaymatch(valid.match("akt"))
displaymatch(valid.match("727ak")) 

with urllib.request.urlopen('http://www.python.org/')as f:
    #print(f.read())
    #print(f.read(300))
    #print(f.read(300).decode("utf-8"))
    p=re.compile("(?<=<title>).*(?=</title>)")
    m=p.search(f.read().decode("utf-8"))
    print(m)