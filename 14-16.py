list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

c = zip(list_a, list_b)
print c

for a, b in zip(list_a, list_b):
    # Add your code here!
    if cmp(a,b) > 0:
        print a
    elif cmp(a,b) < 0:
        print b
    else:
        print 'x'


