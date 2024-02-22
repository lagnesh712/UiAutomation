string="Lagnesh is writing the board"
split_list=string.split()
new_list=[]
for i in split_list:
    if not i[-1].isalpha():
        pass
    elif i[-1].isupper():
        pass
    else:
        new_list.append(i.replace(i[-1],i[-1].capitalize()))
string2=" ".join(new_list)
print(string2)

#swap case
#capitalize vs upper
#