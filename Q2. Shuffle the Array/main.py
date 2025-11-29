nums = [2,5,1,3,4,7] 
n = 3

ans = []
i = 0

while i < n:
    ans.append(nums[i])      # x part
    ans.append(nums[i+n])    # y part
    i += 1

print(ans)
