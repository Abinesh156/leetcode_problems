nums =[3,2]
k = 6

def sumofarr(nums):
    k=0
    for i in nums:
        k+=i
    return k

print(sumofarr(nums)%k)




