l1=[1,3,0,0,4,0,5,2,0,6,0,7]
# expected_output=[5,4,0,0,3,0,2,1,0] 
for i in range (0,len(l1)):
    for j in range(0,i):
        if l1[i]>l1[j]:
            if l1[i]==0 or l1[j]==0:
                continue
            # flag=l1[i]
            # l1[i]=l1[j]
            # l1[j]=flag
            l1[i],l1[j]=l1[j],l1[i]
# if l1==expected_output:
print("Pass ",l1)
