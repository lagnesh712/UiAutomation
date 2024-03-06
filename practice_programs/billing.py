import json
from addition_set import decorate_func

item_list=["lime juice 100","BANANA FRIES 12","POTATO CHIPS 30","APPLE JUICE 10","CANDY 5","APPLE JUICE 10","CANDY 5","CANDY 5","CANDY 5","POTATO CHIPS 30"]

def decorate(func):
    def wrapper_func(x1):
        print("Starting")
        func(x1)
        print("Ending")
    return wrapper_func
@decorate_func
@decorate
def billing(l):
    set_list=set(l)
    item_dict={}
    for i in set_list:
        string_list=i.split()
        for j in string_list:
            if j.isdigit():
                item_dict[" ".join(string_list[:2])]=int(j)*item_list.count(i)

    print(item_dict)
    with open("./json_dict.json","w") as f:
        f.write(json.dumps(item_dict))
        f.close()

billing(item_list)