binary=0
i=0
number=0
while binary>0:
    number=number+binary%10*2**i
    i+=1
    binary=binary//10
print(number)