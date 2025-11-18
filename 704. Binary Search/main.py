nums = [-1,0,3,5,9,12]
target = 9
l=0
r=len(nums)-1
while l<=r:
    m=(l+r)//2
    if target==nums[m]:
        print(m)
        break
    elif target<nums[m]:
        r=m-1
    elif target>nums[m]:
        l=m+1
print(-1)
    