def findMagicalNumber(n: int, x: int) -> str:
    # Write your code here.
    if n and x:
        b = (10**n)+x
        b=str(b)
        print(b)
    return b

n = 3
x = 1
findMagicalNumber(n,x)
