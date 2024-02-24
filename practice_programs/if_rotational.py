str1="abcde" 
str2="eabcd"
flag=True
for i in str1:
    if i not in str2:
        flag=False
        break
if flag==True:
    index=str2.index(str1[0])
    if str2[index:]+str2[:index]==str1:
        print("It's a rotational string")
    else:
        print("Letters are same but Not a rotational string")
else:
    print("The letters are different in both the strings")