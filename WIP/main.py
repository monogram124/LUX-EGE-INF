def algo(n):
    if n <= 41:
        return 0 

    if n == 73:
        return 0
    
    if n == 12:
        return 1 
    
    return algo(n-3) + algo(n - 8) + algo(n // 2)


print(algo(76))