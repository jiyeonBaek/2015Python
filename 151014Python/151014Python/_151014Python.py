import re

#pattern = re.compile("d")
#result = pattern.search("dog")
##result = pattern.search("dog",1)

#print(result)

#print(re.search("\\\\","C:\\test"))

#str= '''sample1.
#sample2.
#sample3.'''

##p=re.compile("^.*",re.S) #ó������, �ƹ��ų� �����ִ�
#p=re.compile(".*$") #�������� �ش�
#print(p.search(str).group());


#pattern = re.compile("o[gh]")
#result = pattern.fullmatch("dog")
#print(result)
#result = pattern.fullmatch("ogre")
#print(result)
#result = pattern.fullmatch("dohgie",1,3)#�ε�����0����, 3�� �ȵ��ٴ¶�
#print(result)

pattern1 = re.compile("\W+") # ���ڰ� �ƴѰ͵�
result=pattern1.split('words, words, words.')
print(result)
result=pattern1.split('words, words, words.',1)
print(result)

pattern2 = re.compile("x*")
result = pattern2.split("axbc")
print(result)

result = re.sub('r\W','','a:b:c,d.')
print(result)

str = '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*)">', str)
print(result.group(1))