import os
import sys
import glob, os.path
import tempfile
import time
import calendar
import random
import webbrowser

#��� ���������������ϵ� ���
#ndir=nfile=0
#def traverse(dir,depth):
#    global ndir, nfile
#    for obj in glob.glob(dir+'/*'):
#        if depth == 0 :
#            prefix='|--'
#        else:
#            prefix='|'+' '*depth+'|--'

#        if os.path.isdir(obj):
#            ndir+=1
#            print(prefix+os.path.basename(obj))
#            traverse(obj,depth+1)
#        elif os.path.isfile(obj):
#            nfile+=1
#            print(prefix+os.path.basename(obj))
#        else:
#            print(prefix+'unknown object:',obj)

#if __name__=='__main__':
#    traverse('..',0)
#    print('\n',ndir,'directories','nfile','files')

#�ӽ����ϸ���� �������������Ÿ�  False�� �ϸ� ��
#with tempfile.TemporaryFile('w+',delete=True) as fp:
#    fp.writelines('Hello world!')
#    fp.seek(0)
#    data=fp.read()
#    print(data)

#�ð����� ���ϴ� ���·� �����Ͽ� ����ؾ��Ѵ�
#t1=time.strftime("%B %dth %A %I:%M",time.localtime())
#print(t1)
#time1=time.ctime(1234567)
#t=time.strptime(time1)
#print(t)
#print(t.tm_mon)
#for i in t:
#    print(i)

#Ķ����
#print(calendar.weekday(2015,10,12))
#print(calendar.monthrange(2015,10))

##����
#list1=[1,2,3,4,5,6,7,8,9,10]
#random.shuffle(list1)
#print(random.choice(list1))

#data=[('Red',3),('Blue',1),('Green',4),('Yellow',2)]
#datalist= []
#for val, cnt in data:
#    for i in range(cnt):
#        datalist.append(val)
#random.shuffle(datalist)
#print(datalist)

url='http://google.com'
webbrowser.open_new_tab(url)