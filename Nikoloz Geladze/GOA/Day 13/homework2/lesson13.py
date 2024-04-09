#2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი.
# გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი.


for i in range(5):
    input("please enter a number: ")
    if i / 2:
        print("your number is odd")
    else:
        print("your number is even")
    