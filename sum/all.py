def list_sum(numbers):
    if numbers == 0:
        return []
    sum_total = 0
    for n in numbers:
        sum_total += n   
    return sum_total
total =  [3,5,6,7,8]
print(list_sum(total))        
