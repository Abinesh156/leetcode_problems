nums = [1,2,2,4]
ans=[]
for num in nums:
    if nums.count(num) >1:
        ans.append(num)
        ans.append(num+1)
        break