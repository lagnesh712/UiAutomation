number=-1
binary=""
reminder=0
try:
    if number>=0:
        if number==0:
            binary=0
        while number>0:
            reminder=number%2
            binary=str(reminder)+binary
            number=number//2
        print(int(binary))
except ValueError:
    print("Please enter a positive integer")