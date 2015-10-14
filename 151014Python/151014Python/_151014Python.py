import re

#pattern = re.compile("d")
#result = pattern.search("dog")
##result = pattern.search("dog",1)

#print(result)

#print(re.search("\\\\","C:\\test"))

#str= '''sample1.
#sample2.
#sample3.'''

##p=re.compile("^.*",re.S) #처음부터, 아무거나 들어갈수있다
#p=re.compile(".*$") #마지막에 해당
#print(p.search(str).group());


#pattern = re.compile("o[gh]")
#result = pattern.fullmatch("dog")
#print(result)
#result = pattern.fullmatch("ogre")
#print(result)
#result = pattern.fullmatch("dohgie",1,3)#인덱스는0부터, 3은 안들어간다는뜻
#print(result)

pattern1 = re.compile("\W+") # 문자가 아닌것들
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