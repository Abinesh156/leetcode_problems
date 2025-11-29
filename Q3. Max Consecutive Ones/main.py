nums = [1,1,0,1,1,1]
ans=[]
j=0
for i in nums:
    if i==1:
        j=j+i
    else:
        ans.append(j)
        j=0
ans.append(j)
print(max(ans))