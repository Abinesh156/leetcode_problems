nums = [5,11,20,20,1]
nums.sort()
k = 5
numOperations = 1
count=[]

m=[]
j=0

for i in nums:
    count.append(nums.count(i))
if j<numOperations:
    print("hi")
    j+=1
maxcount=max(count)
print(maxcount)
