s = "MCMXCIV"
ans = []
final = 0

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

for i in range(len(ans)):
    if i < len(ans) - 1 and ans[i] < ans[i + 1]:
        final -= ans[i]          # subtract small value
    else:
        final += ans[i]          # otherwise just add

print(final)
