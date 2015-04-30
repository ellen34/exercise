#Practice the function of lambda

squares = [ x ** 2 for x in range(1,11)]
print filter(lambda n: n >=30 and n <= 70, squares)
print map(lambda n: n * 2, squares)
print reduce(lambda x, y: x + y, squares)
