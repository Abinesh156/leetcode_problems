moves = "RLUURDDDLU"
u,d,l,r=moves.count("U"),moves.count("D"),moves.count("L"),moves.count("R")
if (r-l,u-d)==(0,0):
    print(True)
else:
    print(False)

