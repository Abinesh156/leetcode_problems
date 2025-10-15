s = "abcabcabcabc"
i = 1
limit = len(s) // 2

while i <= limit:
    Value = s[0:i]
    if len(s) % len(Value) == 0:  # only check if s can be divided by Value
        if Value * (len(s) // len(Value)) == s:
            print("Pattern Found:", Value)
            print (s.count(Value))
            break
    i += 1
else:
    print("No Pattern")