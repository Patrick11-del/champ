def small_number(numbers):

    if not numbers:
        return None

    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest
x = [3,7,6,9,10,5,8] 

print(small_number(x))
