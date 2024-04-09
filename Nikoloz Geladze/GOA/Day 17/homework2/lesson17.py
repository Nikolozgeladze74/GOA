numbers = [3,6,-1,2,8,9,4,5,7,-2]

max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)