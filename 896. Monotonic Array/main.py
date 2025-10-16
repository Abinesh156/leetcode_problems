nums = [1,3,2,4]

def mono(num):
    ans=[]
    for i in range(len(nums)-1):
        if i!=len(nums):
            if nums[i] <= nums[i+1] and nums[i] != nums[i+1]:
                
                ans.append(True)
            elif nums[i] >= nums[i+1] and nums[i] != nums[i+1]:
                ans.append(False)
    ans=sorted(ans)
    if len(ans)!=0:
        if ans[0]==ans[len(ans)-1]:
            return True 
        else:
            return False
    else:
        return True
print(mono(nums))