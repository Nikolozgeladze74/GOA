numbers = []

for i in range(12, 50 + 1, 4):
    numbers.append(i)


reversed_list = []

for index in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[index])

print(numbers)
print(reversed_list)