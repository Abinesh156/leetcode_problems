n = 43261596

def contobin(n):
    ans=[]
    while n!=0:
        ans.append(n%2)
        n = n//2
    return ans


def check_if_32bit(valinbin):
    if len(valinbin)!=32:
        d=32-len(valinbin)
        for i in range(d):
            valinbin.append(0)
    return valinbin

def bintodec(binary):
    decimal = 0
    for bit in binary:
        decimal = (decimal << 1) | int(bit)
    return decimal

valinbin=contobin(n)
valinbin=check_if_32bit(valinbin)
print(valinbin)
decimal = 0
for bit in valinbin:
    decimal = (decimal << 1) | bit

print(decimal)



