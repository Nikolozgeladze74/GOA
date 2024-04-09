numbers = []

for i in range(30, 50+1):
    numbers.append(i)

odd_count = 0

for number in numbers:
    if number % 2 != 0:
        odd_count = odd_count + 1

print(odd_count)