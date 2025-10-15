s = "anagram"
t = "nagaram"

if len(s)!=len(t):
    print(False)
else:
    array1=set(s)
    array1=sorted(array1)
    array2=set(t)
    array2=sorted(array2)
    ds={}
    dt={}
    for i in array1:
        value=s.count(i)
        key=i
        ds[key] = value
    for i in array2:
        value=t.count(i)
        key=i
        dt[key] = value
    
    if dt==ds:
        print(True)
    else:
        print(False)