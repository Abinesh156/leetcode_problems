nums = [0,1,0,3,12]
# count=nums.count(0)
# for i in range(count):
#     nums.remove(0)
# for i in range(count):
#     nums.append(0)

# print(nums)

for i in range (len(nums)):
    if nums[i]==0:
        bun=nums[i]
        nums.remove(nums[i])
        nums.append(0)
   

        

