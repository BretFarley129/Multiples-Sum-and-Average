
#Multiples pt 1
for i in range(1,1000, 2):
    print i

#Multiples pt 2
for i in range(5, 1000001, 5):
    print i


#Sum
a = [1, 2, 5, 10, 255, 3]
def summation(arr):
    x = 0
    for i in arr:
        x += i
    return x

print summation(a)

#Average
def avg(arr):
    s = summation(arr) + 0.0
    l = len(arr)
    return s/l

print avg(a) 