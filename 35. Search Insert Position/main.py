nums = [1,3,5,6]
target = 2
# ans=target
# def insertposition(target,nums,ans):
#     if target in nums:
#         return nums.index(target)
#     if max(nums)<target:
#         return len(nums)
#     if 
#     while ans not in nums:
#         ans=ans+1
#         return nums.index(ans)
# print(insertposition(target,nums,ans))


nums.append(target)
nums.sort()

print(nums.index(target))

