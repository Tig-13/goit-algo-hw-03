import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or quantity > (max_num - min_num + 1):
        return []
    
    list_of_numbers = []

    while len(list_of_numbers) < quantity:
        y = random.randint(min_num, max_num)
        if y not in list_of_numbers:
            list_of_numbers.append(y)
    
    return sorted(list_of_numbers)

min_num = int(input('Input min = '))
max_num = int(input('Input max = '))
quantity = int(input('Input quantity = '))
lottery_numbers = get_numbers_ticket(min_num, max_num, quantity)
print("Ваші лотерейні числа:", lottery_numbers)