mat = [[4,6,7],
       [2,9,4],
       [5,5,5]]
ans=[]
j=0
for i in range(len(mat)):
    ans.append(mat[i][i])
for i in range(len(mat)-1,-1,-1):
    ans.append(mat[j][i])
    j+=1
print(ans)
if len(mat)%2==0:
    print("ggg",sum(ans))
else:
    print(sum(ans) - mat[len(mat)//2][len(mat)//2])
