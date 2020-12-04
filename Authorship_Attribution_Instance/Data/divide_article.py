import os



fh = open('data_somashekar.txt','r')


txt = fh.readlines()
count=1
for k in range(len(txt)):
    if(txt[k].__contains__('a')):
        f = open(str(count)+'.txt','w')
        for j in range(k+1,len(txt)):
            if(txt[j].__contains__('a')):
                break
            
            print(txt[j])
            f.write(txt[j])
            
        f.close()
        count+=1

            


print(txt[1])

fh.close()
