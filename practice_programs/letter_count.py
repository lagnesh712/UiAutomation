string="hello world"
for i in range(0,len(string)-1):
    i1=string[i]
    i2=string[i+1]
    if i1=="l" and i2=="l":
        print(i,i+1)