arr = [40,11,26,27,-20]
ans=[]
arr=sorted(arr)
minnum = float('inf')

for i in range(len(arr)-1):
    diff = arr[i + 1] - arr[i]
    if diff < minnum:
        minnum = diff
        ans=[[arr[i],arr[i+1]]]
    elif diff==minnum:
      ans.append([arr[i],arr[i+1]])
print(ans)



