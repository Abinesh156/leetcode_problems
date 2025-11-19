l1 = [2,4,3]
l2 = [5,6,4]

l1=l1[::-1]
l2=l2[::-1]
l1_str =int( "".join(map(str, l1)))
l2_str = int("".join(map(str, l2)))

result=[]
ans=l1_str+l2_str

print(ans)
 
for i in str(ans):
    result.append(int(i))

print(result[::-1])