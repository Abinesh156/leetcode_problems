digits = [1,2,3]
# a="".join(map(str, digits))
# a=int(a)+1
# a = [int(d) for d in str(a)]  

# print(a)

if len(digits)<=1:
    digits=digits[0]+1
    print(digits)