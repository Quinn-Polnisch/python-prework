# Question 1
def hello_name(username):
    '''Prints hello to the user'''
    print(f'Hello {username}!')


# Question 2
def first_odds(nums):
    '''finds the odd numbers in a given list of numbers'''
    for num in nums:
        if num % 2 == 1:
            print(num)


# Question 3
def max_num_in_list(alist):
    '''finds the max number in a list'''
    max_num = 0
    for num in alist:
        if num > max_num:
            max_num = num
    return max_num


# Question 4
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
            
        else:
            return True
        
    else:
        return False
    

# Question 5
def is_consecutive(alist):
    '''
    returns a boolean value about whether or not a list is
    in sequencial order and reverse sequential order
    '''

    for index in range(len(alist)-1):
        index2 = index + 1
        if alist[index2] > alist[index] and (alist[index2] - alist[index]) == 1:
            continue
        elif alist[index] > alist[index2] and (alist[index] - alist[index2]) == 1:
            continue
        else:
            return False
    return True



# hello_name('flynn')

# first_odds(range(100))

# print(max_num_in_list([1,4,3,2,10,1,-20]))

# print(is_leap_year(3200))

# print(is_consecutive([-1,1,0]))