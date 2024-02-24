l=[1,2,3,5,6,6,7,8,15]
i=0
while i < len(l)-1:
    sum=l[i]+l[i+1]
    if sum in l:
        print(l[i],",",l[i+1],",",sum)
    i+=1


        
