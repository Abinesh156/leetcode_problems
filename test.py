# # nums =[3,2,3]
# # target = 6
# # k=len(nums)-1
# # for i in nums:
# #     for j in range(len(nums)-1):
# #         if i+nums[k]==target:
# #                 print(nums.index(i),k)
# #         k=k-1

# # nums1 = [0,0]
# # nums2 = [0,0]
# # array=sorted(nums1+nums2)
# # print(array)
# # if len(array)%2==1:
# #     print(float(array[len(array)//2]))
# # elif len(array)%2==0:
# #      mid1=(array[len(array)//2])
# #      mid2=((array[(len(array)//2)-1]))
# #      print(mid1,mid2)
# #      print((mid2+mid1)/2)
      


# # s="heh"
# #  How to reverse a string in Python?
# # rev=s[::-1]

# # if s==rev:
# #     print("pal")
# # else:
# #     print("not pal")


# # How to check if a given string is a palindrome in Python?
# # n=6
# # ans=n
# # for i in range(n-1,0,-1):
# #     ans=ans*i
# # print(ans)


# # Fibonacci 
# n=7
# ans=[]
# end=0


# for i in range(n):
#     ans.append(i)
#     if ans[len(ans)-1]+ans[len(ans)-2] == n or ans[len(ans)-1]+ans[len(ans)-2]>n:
#         print(ans)
#     else:
#         ans.append()




# n = 1020030
# k=str(n)
# k=list(k)
# while True:
#     if "0" in k:
#         k.remove("0")


# nums = [1,2,3]
# print(sorted(nums))


# nums=[1,2,3,4,5]
# maxnum=0
# for i in nums:
#     if i>maxnum:
#         secmax=maxnum
#         maxnum=i
#     elif secmax<i:
#         secmax=i

# print(maxnum,secmax)


# num=[-1,-2,-3,10,10,10]
# num=set(sorted(num))

# i=2
# k=0
# print(i>k)
# while i>k:
#     num.remove(max(num)) #second largest
#     k+=1

# print(max(num))

# s = "A man, a plan, a canal: Panama"
# #ignore non-alphanumeric and case
# s=''.join(e for e in s if e.isalnum()).lower()
# if s[::-1]==s:
#     print("pal")
# else:
#     print("not pal")


n=[1,2,1,2,4,5,6,6]

n1=list(set(n))
print(n)