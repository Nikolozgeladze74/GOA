#1
for x in range(11):
     print(x)

#2
name = "nikolozi"

for x in [name]:
     print(x)


#3
for x in range(7):
    print(x)



#4
for x in range(0, 77 + 1):
    x = x + 10
    print(x)



#5
for x in range(3, 74):
     print(x)



#6
for x in [77]:
     print(x)



#7
for x in range(3, 40, 3):
   print(x)



#8
for x in range(3, 40, 9):
   print(x)



#9
for x in range(30 + 1):
    if x < 5: continue
    print(x)
else:
    print("GOA is the BEST!")



#10
num_1 = int(input("enter a first number: "))
num_2 = int(input("enter a second number: "))

sum = num_1 == num_2
for x in range(300):
     if x < sum: continue
     num_1 = num_1 + num_2
     print(x)
     if x == 299:
         print(x == x)
else:
     print("GOA is the best")