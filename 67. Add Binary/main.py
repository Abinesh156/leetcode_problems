
def bintodec(binary):
    decimal = 0
    for bit in binary:
        decimal = (decimal << 1) | int(bit)
    return decimal


def contobin(n):
    ans=[]
    while n!=0:
        ans.append(str(n%2))
        n = n//2
    return "".join(reversed(ans))

a = "11"
b = "1"

a=bintodec(a)
b=bintodec(b)
print(a,b)
d=a+b

if d==0:
    print(0)
print(contobin(d))
