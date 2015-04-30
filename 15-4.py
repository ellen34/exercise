#digit_sum

def digit_sum(n):
    n = str(n)
    total = 0
    for item in range(len(n)):
        total += int(n[item])
    return total

digit_sum(434)

