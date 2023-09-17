def power_numbers(numbers):
    sq = []
 
    for n in numbers:
        power = n ** 2
        sq.append(power)
        
    return sq

print(power_numbers(numbers = [1,2,3,5]))