for count in range(0,1001):
    if count%2 != 0:
        print count
for count in range(5,1000001):
    if count%5 == 0:
        print count
a = [1, 2, 5, 10, 255, 3]
sum1 = 0
for counter in a:
    sum1 += counter
print sum1
print sum1/len(a)
