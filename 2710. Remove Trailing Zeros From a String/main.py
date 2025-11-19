# num = "51230100"
# reversed_num = num[::-1]  # This reverses the string
# print(reversed_num)
# j=1
# for i in range(len(num)):
#     if int(reversed_num[i])+int(reversed_num[j]) >=1:
#         print(num[i])
#     j=j+1


# num="51230100"
# # num=num[::-1]
# # ans=num


# # def removezero(num,ans):
# #     for i in num:
# #         if i=="0":
# #             ans = ans.replace(i, "",1) 
# #         elif int(i)>0:
# #             return ans[::-1]
# # print(removezero(num,ans))


num="51230100"
ans=list(num)
for i in range(len(num)-1,0,-1):
    if num[i]=="0":
        ans.pop(i)
    elif num[i]!="0":
        print(i)
        break
print("".join(ans))