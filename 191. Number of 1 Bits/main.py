n = 11


def binary(num):
    binary=""
    while num!=0:
        rem=num%2
        binary=str(rem)+binary
        num=num//2
    return binary

def suma(bin):
    k=0
    for i in bin:
        k=k+int(i)
    return k

bin=binary(n)
print(bin)