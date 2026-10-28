def even_number(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count
list_num = [3, 4, 6,8,10,7]

print(even_number(list_num))
