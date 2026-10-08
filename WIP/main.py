count = 1

def f(a, b):
    global count
    if a / b == 29 / 41:
        return a, b, count
    
    print(a, b)

    count += 1

    return f(a+b, b+2*a)

print(f(2, 3))