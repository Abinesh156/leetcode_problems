arr = [1,10,10,10,19]
arr=(sorted(arr))
ans=[]
for i in range(len(arr)-1):
    ans.append(arr[i]-arr[i+1])
ans=sorted(ans)
if ans[0]==ans[len(ans)-1]: 
    print(ans[0],ans[len(ans)-1])
    print(True)
    
   