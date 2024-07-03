#1
def is_even(n): 
    return n % 2 == 0

#2
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    
    sum_of_numbers = 0
    
    for num in numbers:
        sum_of_numbers += num
    
    result = sum_of_numbers / len(numbers)
    
    return result

#3
def length_of_sequence(arr,n):
    if arr.count(n) != 2:
        return 0
    
    first_index = arr.index(n)
    second_index = 0
    
    for index in range(len(arr) - 1, -1, -1):
        if arr[index] == n:
            second_index = index
            break
    
    return len(arr[first_index:second_index + 1])

#4
def tail_swap(strings):
    first_list = strings[0].split(':')
    second_list = strings[1].split(':')
    
    temp_var = second_list[1]
    second_list[1] = first_list[1]
    first_list[1] = temp_var
    
    return [':'.join(first_list), ':'.join(second_list)]

#5
def score(dice):
    # dice scores  [1   ,   2,   3,   4, 5,   6]
    scores_3same = [1000, 200, 300, 400, 500, 600]
    scores_single = [100 ,   0,   0,   0,  50,   0]
    
    sum = 0
    for i in range(1,7):
        count_i = dice.count(i)
        sum += (count_i // 3) * scores_3same[i-1] + (count_i % 3) * scores_single[i-1]
            
    return sum