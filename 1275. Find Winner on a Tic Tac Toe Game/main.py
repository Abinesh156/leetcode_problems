moves = [[2,2],[1,2],[2,1],[1,1],[2,0]]
a=[]
b=[]
row_a=[]
col_a=[]
row_b=[]
col_b=[]
cross=[0,1,2]
def sepratemoves(moves):
    for i in moves:
        if moves.index(i)%2:
            b.append(i)
        else:
            a.append(i)
def rowcol(num,row,col):
    for j in range(len(num)):
        row.append(num[j][0])
    for j in range(len(num)):
        col.append(num[j][1])

sepratemoves(moves)
print("movea",a)
print("moveb",b)
rowcol(a,row_a,col_a)
rowcol(b,row_b,col_b)
print("a",row_a,col_a)
print("b",row_b,col_b)
if len(moves)==9:
    print("draw")
elif row_a==col_a==len(row_a)==3 or sum(row_a)==sum(col_a)==3==len(row_a):
    print("A",col_a[len(col_a)-1],col_a[0])
elif row_b==col_b==cross==len(row_b)==3 or sum(row_b)==sum(col_b)==3==len(row_b):
    print("B")
else:
    print("pending")




