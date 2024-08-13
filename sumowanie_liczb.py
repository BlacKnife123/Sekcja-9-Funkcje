def sumAll(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total += number

    return total

numbers = [-6,-72,5,6,7,8,94]

print(sumAll(numbers))