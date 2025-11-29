nums = [2,7,11,15]
target = 9
nums1 = nums
ans=[]
for i,num in enumerate(nums):
    nums.remove(num)
    n=target-num
    if n in nums:
        ans.append(i)
        ans.append(nums1.index(n))
        break
print(ans)