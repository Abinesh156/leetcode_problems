nums = [-1,-2,-3,-4,3,2,1]
product = 1

for n in nums:
    product *= n
print(product)
def signFunc(n):
    if n<0:
        return -1
    if n>0:
        return 1
    if n==0:
        return 0
    
print(signFunc(product))