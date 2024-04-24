#1)
def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"
    
#2)
def number_to_string(num):
      return str(num)

#3)
def opposite(number):
     return number - number * 2

#4)
def make_negative( number ):
    if number > 0:
        return number * -1
    else:
        return number
    
#5)
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
#6)
def positive_sum(arr):
    sum = 0
    
    for number in arr:
        if number > 0:
            sum = sum + number
    
    return sum

#7)
def remove_char(s):
    return s[1:-1]

#8)
def square_sum(numbers):
    sum = 0
    
    for num in numbers:
        sum = sum + (num * num)
    
    return sum

#9)
def double_integer(i):
    return i * 2