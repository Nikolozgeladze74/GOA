def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))



def reverseseq(n):
    return list(range(n, 0, -1))


def no_space(x):
    final = ""
    for symbol in x:
        if symbol != " ":
            final += symbol
    return final



def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]


def factorial(n):
    j = 1
    for i in range(1, n+1):
       j *= i
    return j




def divisors(n):
    i = 1
    result = 0
    while i <= n:
        if n%i == 0:
            result += 1
        i+=1
    return result


