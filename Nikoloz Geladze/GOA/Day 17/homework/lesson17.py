#1
numbers = [3,6,-1,2,8,9,4,5,7,-2]

max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)

#2
numbers = []

for i in range(30, 50+1):
    numbers.append(i)

odd_count = 0

for number in numbers:
    if number % 2 != 0:
        odd_count = odd_count + 1

print(odd_count)


#3
numbers = []

for i in range(12, 50 + 1, 4):
    numbers.append(i)


reversed_list = []

for index in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[index])

print(numbers)
print(reversed_list)

#4
numbers = []

for i in range(50,100+1):
    numbers.append(i)


even_numbers = []

for index in range(0, len(numbers)):
    if numbers[index] % 2 == 0:
        even_numbers.append(str(numbers[index]) + "-" + str(index))

print(numbers)
print(even_numbers)