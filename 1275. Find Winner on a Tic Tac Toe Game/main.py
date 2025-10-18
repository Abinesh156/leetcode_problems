moves = [[2,2],[1,2],[2,1],[1,1],[2,0]]
a=[]
b=[]
row_a=[]
col_a=[]
row_b=[]
col_b=[]

def sepratemoves(moves):
    for i in range(len(moves)):
        if i % 2 == 0:
            a.append(moves[i])
        else:
            b.append(moves[i])

def rowcol(num,row,col):
    for j in range(len(num)):
        row.append(num[j][0])
        col.append(num[j][1])

sepratemoves(moves)
rowcol(a,row_a,col_a)
rowcol(b,row_b,col_b)

def check_winner(rows, cols):
    for i in range(3):
        if rows.count(i) == 3:  # row win
            return True
        if cols.count(i) == 3:  # column win
            return True
    # diagonal checks
    if [ [rows[i], cols[i]] for i in range(len(rows)) ].count([0,0]) + \
       [ [rows[i], cols[i]] for i in range(len(rows)) ].count([1,1]) + \
       [ [rows[i], cols[i]] for i in range(len(rows)) ].count([2,2]) == 3:
        return True
    if [ [rows[i], cols[i]] for i in range(len(rows)) ].count([0,2]) + \
       [ [rows[i], cols[i]] for i in range(len(rows)) ].count([1,1]) + \
       [ [rows[i], cols[i]] for i in range(len(rows)) ].count([2,0]) == 3:
        return True
    return False

if check_winner(row_a, col_a):
    print("A")
elif check_winner(row_b, col_b):
    print("B")
elif len(moves) == 9:
    print("Draw")
else:
    print("Pending")
