def prime(num):
    if num <= 1:
        return False 
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

def filter_num(numbers, filter = 'even'):
    if filter == 'even':
        return [x for x in numbers if x%2 == 0]
    elif filter == 'even':
        return [x for x in numbers if x%2 == 1]
    else:
        return [x for x in numbers if prime(x)]
        
numbers = [1,4,5,7,9,1,0,10,13,21]

even_num = filter_num(numbers, 'even')
odd_num = filter_num(numbers, 'odd')
prime_num = filter_num(numbers, 'prime')

print(even_num) 
print(odd_num)  
print(prime_num)