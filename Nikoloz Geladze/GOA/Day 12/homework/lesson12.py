#დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია, უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი.

num = int(input("enter a number: "))

if num < 0:
     print("This number is negative")
if num == 0:
     print("This number is equal to zero")
if num > 0:
     print("This number is positive")

#დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი.
#მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა,
#რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა. თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას,
#დაბეჭდეთ "Wrong decision".
choice = input("if you want miles to kilometers type 1. if you want kilometers to miles type 2: ")

if choice == "1":
     amount1 = int(input("Enter number: "))
     print(amount1, "miles to kilometers would be", amount1 * 1.6)
elif choice == "2":
     amount2 = int(input("Enter number: "))
     print(amount2, "kilometers to miles would be", amount2 * 0.62 )
else:
     print("wrong decision")

#შექმენით რეგისტრაციის ალგორითმი. მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი და მეილი,
#საბოლოოდ კი ერთ წინადადებაში გამოიტანეთ მიღებული ინფორმაცია.
name = input("Enter youre name: ")
lastname = input("entrer youre lastname: ")
age = int(input("enter youre age: "))
email = input("entr youre email: ")

print("your name is:",name, "  your lastname is:",lastname, "  your age is:",age, "  your email is:", email)


#მომხმარებელს სამჯერ შეეკითხეთ რიცხვითი მნიშვნელობა და დაბეჭდეთ მათი საშუალო არითმეტიკული.
num_1 = int(input("please enter an number: "))
num_2 = int(input("please enter an number: "))
num_3 = int(input("please enter an number: "))

print((num_1 + num_2 + num_3)/3)

#მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი. შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ
# ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში.

#მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის, ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ.
# ციკლში იტერაცია მოახდინეთ ერთით და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი).
num1 = int(input("Enter the first number >: "))
num2 = int(input("Enter the second number >: "))

if num1 < num2:
     for i in range(num1, num2, +1):
        print(i)
else:
     for i in range(num2, num1, +1):
         print(i)
print(i * i * i)