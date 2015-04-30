#is_prime

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                print "This is not a prime"
                return False
                break
            else:
                continue
        print "This is a prime"
        return True
        
is_prime(211)
