#none, 빈부분은 모두 false로 인식
import pickle
filename="파일입출력예제1.txt"
with open(filename,"r") as myfile:
    #myfile.write("201311216 백지연\n")
    #myfile.write("201311217 홍길동\n")
    #myfile.write("201311218 고길동\n")
    #myfile.write("201311219 김길동\n")
    with open("Monica.txt","wb") as file2:
        roles=[]    
        for content in myfile:
            (role,etc)=content.strip().split(":",1)
            #if role=="Monica":
            #    file2.write(etc)
            #    file2.write("\n")
            roles.append(role)
    
        pickle.dump(roles,file2)
    with open("Monica.txt","rb") as file2:
        result=pickle.load(file2)
        print(result)