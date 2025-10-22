low = 3
high = 7

def odd(value):
    if value%2==0:
      value+=1
    return value
low=odd(low)
high=odd(high)
print(max(high-low)//2 + 1)