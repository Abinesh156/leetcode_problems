operations = ["5","-2","4","C","D","9","+","+"]
ans=[]
for i in operations:
     if i=="D":
        ans.append(ans[len(ans)-1]*2)
     elif i=="C":
        ans.pop()
     elif i=="+":
        ans.append(ans[len(ans)-2]+ans[len(ans)-1])
     else:
        ans.append(int(i))
     i=i+1
print(sum(ans))