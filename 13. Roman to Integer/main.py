s="MCMXCIV"
ans=[]

roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
for i in s:
    ans.append(roman_dict[i])
print(ans)
for i in range(len(ans)-1):
    if ans[i]<ans[i+1]:
        final=final+(ans[i+1]-ans[i])


print(final)
