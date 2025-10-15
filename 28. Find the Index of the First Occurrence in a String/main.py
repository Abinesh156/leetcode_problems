haystack = "hello"
needle = "ll"
lh=len(haystack)
ln=len(needle)
i=0
ans=[]
while i<lh:
    value=haystack[i:i+ln]
    print(value)
    if value==needle:
        ans.append(i)
    i=i+1
if ans==[]:
   ans.append(-1)
print(ans)

   
# for i in range(0,lh):
#     for j in range (i,ln):
#         print(j)





