nums = [5,1,5,2,5,3,5,4]
# nums1=list(set(nums))
# k=0
# for i in nums1:
#     x=nums.count(i)
#     if x>1:
#         print(i)
#         break
d={}
for i in range(len(nums)):
    d[nums[i]] = i
    if nums[i] in d:
        print( nums[i])
