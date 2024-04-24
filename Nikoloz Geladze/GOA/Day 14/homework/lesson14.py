# 1.

age = int(input("please enter your age"))

if age < 18:
    print("you are child")
elif age >= 18 and age < 65:
    print("you are adult")
else:
    print("you are old")

# 2.

for i in range(5):
    number = int(input("please enter number: "))
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

# 3. 

grade = input("please enter grade (a,b,c,d or F): ")

if grade == "A":
    print("exselnte!")
elif grade  == "b":
    print("good job!")
elif grade == "c":
    print("you passed.")
elif grade == "D":
    print("you can do better.")
else:
    print("you failed.")

#4. 

num = 1

while num < 10:
    print(num)
    num = num + 1