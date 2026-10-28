def largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

                
    return largest

largest_num = [3, 41, 56, 21, 76, 9]

print(largest_number(largest_num))
