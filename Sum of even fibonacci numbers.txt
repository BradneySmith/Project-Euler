a,b = 1,2
count = 0
while b < 4000000:
    a,b = b, a+b
    if a % 2 == 0: count += a
print(count)