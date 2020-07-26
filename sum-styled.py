limit = 10


def sum_of_natural_numbers(limit):
    sum_of_numbers = 0
    for i in range(limit+1):
        sum_of_numbers += 1
    return sum_of_numbers


answer = sum_of_natural_numbers(limit)
print(answer)
