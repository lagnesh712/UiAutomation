x=int(input())

try:
    if x>10:
        print(x)
    else:
        raise NameError("invalid value")
except NameError:
    raise