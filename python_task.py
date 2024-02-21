string="Lagnesh is writing the board"
split_list=string.split()
new_list=[]
for i in split_list:
    new_list.append(i.replace(i[-1],i[-1].capitalize()))
string2=" ".join(new_list)
print(string2)