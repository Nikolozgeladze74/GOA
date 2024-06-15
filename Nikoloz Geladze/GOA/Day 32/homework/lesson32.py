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

#6
def no_odds(values):
    list = []
    for i in values:
        if i%2==0:
            list.append(i)
    return list

#7
def number_of_occurrences(element, sample):
    total = 0
    for i in sample:
        if element == i:
            total += 1
    return total