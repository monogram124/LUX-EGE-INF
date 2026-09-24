def to_sys(N, base):
    if N == 0:
        return "0"
    
    sys_N = ""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while N > 0:
        remainder = N % base
        
        sys_N = digits[remainder] + sys_N
        N //= base
    
    return sys_N

print(to_sys(149, 4))