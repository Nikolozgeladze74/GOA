#ყველამ შეასრულეთ classwork-ის ამოცანები:

#ყველამ შეასრულეთ classwork-ის ამოცანები:

#8 kyu:

#https://www.codewars.com/kata/58649884a1659ed6cb000072
#https://www.codewars.com/kata/58cb43f4256836ed95000f97
#https://www.codewars.com/kata/5704aea738428f4d30000914

#7kyu:

#https://www.codewars.com/kata/583f158ea20cfcbeb400000a
#https://www.codewars.com/kata/56b7f2f3f18876033f000307
#https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763

#6kyu:

#https://www.codewars.com/kata/52b757663a95b11b3d00062d
#https://www.codewars.com/kata/569d488d61b812a0f7000015









#1
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."
    
#2
def find_difference(a, b):
    v1 = a[0] * a[1] * a[2]
    v2 = b[0] * b[1] * b[2]
    if v1 > v2:
        return v1 - v2
    elif v1 < v2:
        return v2 - v1
    else:
        return 0
    
#3
def triple_trouble(one, two, three):
    count = 0
    length = len(one)
    string = ""
    while count < length:
        string += one[count] + two[count] + three[count]
        count += 1
    return string

#4
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b * 1.0
    
#5
def in_asc_order(arr):
    min = 0
    for n in arr:
        if n < min:
            return False
        min = n
    return True