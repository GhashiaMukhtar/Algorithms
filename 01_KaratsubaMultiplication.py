def karatsuba(x,y):
    if x<10 or y<10:
        return x*y

    x_len, y_len = len(str(x)), len(str(y))
    n = max(x_len,y_len)
    m = n//2

    a = x//10**m
    b = x%10**m
    c = y//10**m
    d = y%10**m
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    middle_value = karatsuba(a+b, c+d) - ac - bd

    return (10**(2 * m)*ac) + (10 ** m * middle_value) + bd

x = int(input("Enter first number for multiplication:\n"))
y = int(input("Enter second number for multiplication:\n"))
result = karatsuba(x,y)
print("The result is:",result)

