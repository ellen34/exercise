#is_int
def is_int(x):
    if x == int(x):
        return True
    else:
        if  round(x) != 0 and x / float(round(x)) == 1.0 :
            return True
        else:
            return False
    
is_int(7.0)
is_int(7.5)
is_int(-1)

