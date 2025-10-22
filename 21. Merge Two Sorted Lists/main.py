list1 = [1,2,4]
list2 = [1,3,4]
j=0
ans=[]
i=0
for i in list1:
    i+=1
while j<i-1:
    ans.append(list2[j])
    ans.append(list1[j])
    try:
       ans.append(list1[1+j])
    except IndexError:
        pass
    j+=2
    
print(ans)