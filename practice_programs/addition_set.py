l=[1,2,3,5,6,6,7,8,15]

def decorate(func):
    def wrapper_func(x1):
        print("Starting")
        func(x1)
        print("Ending")
    return wrapper_func

def decorate_func(func):
    def wrapper_func(x1):
        print("Starting the function.")
        func(x1)
        print("Ending the function.")
    return wrapper_func


@decorate
@decorate_func
def sum_inList(l):
    i=0
    while i < len(l)-1:
        sum=l[i]+l[i+1]
        if sum in l:
            print(l[i],",",l[i+1],",",sum)
        i+=1

sum_inList(l)

        
