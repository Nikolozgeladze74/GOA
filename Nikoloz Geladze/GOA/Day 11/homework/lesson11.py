# 1 შექმენით სია სადაც გადასცემთ 10 ინტეჯერს, შემდეგ გადაუარეთ ამ სიას და თტოეულ მათგანს გაამრავლეთ/გაყეთ/დაუმატეთ/გამოაკელით ერთმანეთს.

num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] * 2)


num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] / 2)


num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] + 2)


num_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.]
for i in num_list :
    print(num_list[i] - 2)



# 2შექმენით სია,სადაც გამოიტანთ სათითაოდ მნიშვნელობებს და ასევე  ჩაანაცვლებთ სხვა მნიშვნელობით.

car_list = ["Ferrari", "Porche", "Bugatti"]
print(car_list[0])
print(car_list[1])
print(car_list[2])
car_list[1] = "Rolls Royce"
print(car_list)



# 3 დავალება შექმენით სია და მომხმარებელს აარჩევინეთ სასურველი მნიშვნელობა.

sport_list  = ["Football", "MMA", "Boxing"]
choise = int(input("wich one is your favourite sport? "))
print(sport_list[choise])