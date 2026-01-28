nums = [2,2,-1,3,-2,2,1,1,1,0,-1]

a=float('inf')
for i in range(0,len(nums),2):
    if a>nums[i]+nums[i+1]:
        a=nums[i]+nums[i+1]
print(a)
    