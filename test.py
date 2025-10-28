nums =[3,2,3]
target = 6
k=len(nums)-1
for i in nums:
    for j in range(len(nums)-1):
        if i+nums[k]==target:
                print(nums.index(i),k)
        k=k-1

