#5) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა,
# სანამ მომხმარებელი სწორად არ გამოიცნობს

i = int(input("guess the number: "))
while i < 10:
    print(i) 
    i += 1