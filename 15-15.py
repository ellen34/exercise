def median(numbers):
    numbers.sort()
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) / 2]
    else:
        val = float(numbers[len(numbers) / 2] + numbers[len(numbers) / 2 - 1]) / 2.0
        return val

print median([7,12,3,1,6])
