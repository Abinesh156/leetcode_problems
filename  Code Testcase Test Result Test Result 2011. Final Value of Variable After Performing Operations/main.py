operations = ["++X","++X","X++"]
value={"X--":-1,"X++":1}
j=[]
for i in operations:
    if i=="++X"or i=="X++":
        j.append(1)
    elif i=="--X" or "X--":
        j.append(-1)
print(j)