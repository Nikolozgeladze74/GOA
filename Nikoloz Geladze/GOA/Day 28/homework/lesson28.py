def get_average(marks):
    return sum(marks) // len(marks)



def make_negative( number ):
    if number > 0:
        return number * -1
    else:
        return number
    


def str_count(strng, letter):
    count = 0
    for e in strng:
        if e == letter:
            count += 1
            
    return count


def is_leap_year(year):
    print(year%4, year)
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
    


    def best_friend(txt, a, b):
        for i in range(len(txt)):
            if txt[i] == a:
                if i + 1 == len(txt):
                    return False
            elif txt[i + 1] != b:
                return False
    return True