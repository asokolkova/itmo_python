import os
names=os.listdir('.') #текущая папка
print(names)
file2=open('result.txt','w')
sum_n=0
for name in names:
    f=open(name)
    s=f.read()
    f.close()
    if (s.count('python')) != 0:
        print(name)
        n=s.count('python')
        sum_n=sum_n+n
        print(n)
        file2.write(name+'\t'+str(n)+'\n')
    else:
        file2.write(name+'\t'+str(0)+'\n')
print(sum_n) #общее кол-во слов python
file2.close()
        
    
    

        
