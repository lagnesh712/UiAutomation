string="aaaabbbdddccaa"
# output - > 4a3b3d2c2a
outstring=""
index=0
i=0
while index < len(string):
    flag=0
    string2=string[i:]
    for j in string2:
        if string[i]==j:
            flag+=1
            index+=1
        else:
            break
    i=index
    outstring=outstring+str(flag)+string[i-1]
print(outstring)

