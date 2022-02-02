

def math_operations(*args,**kwargs):
    count = 1
    numbers = list(args)
    for number in numbers :
        if count ==1:
            kwargs["a"] += number
            count +=1
        elif count == 2:
            kwargs["s"] -= number
            count +=1
        elif count ==3:
            try:
                kwargs["d"] /= number
                count +=1
            except ZeroDivisionError:
                count+=1
        elif count == 4:
            kwargs['m'] *=number
            count =1
    return kwargs

print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))