def list_sum(numbers):
    if numbers == 0:
        return []
    sum_total = 0
    for n in numbers:
        sum_total += n   
    return sum_total
total =  [3,5,6,7,8]
print(list_sum(total))        


def count_occurrences(numbers, target):
    count = 0

    for x in numbers:
        if x == target:
            count += 1
    return count

num = [2, 5, 2, 8, 2]
target = 2

result = count_occurrences(num, target)
print(f"target number: {target}\n number of appearance: {result}")


def find_number(numbers, target):
    if target not in numbers:
        return -1
    target_num = []
    for index, value in enumerate(numbers):
        if value == target:
            target_num.append(index)
            
    return target_num        
            
x = [5, 8, 9]
target = 5

print(find_number(x, target))

def reverse_list(items):

    new_list = []

    for index in range(len(items) -1, -1, -1):
        new_list.append(items[index])
    return new_list    
reverse = [1, 2, 3, 4]

print(reverse_list(reverse))
