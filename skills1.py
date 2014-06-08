# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = some_list[0:-1:2]
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = some_list[1:-1:2]
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = list()
    index = 0
    for index in range(len(word_list)):
        if len(word_list[index]) > 4:
            new_list.append(word_list[index])
        index +=  1
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    some_list.sort()
    return some_list[0]

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    some_list.sort()
    return some_list[-1]

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    # index = 0
    for index in range(len(some_list)):
        some_list[index] = some_list[index]/2.0
    return some_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = list()
    for index in range(len(word_list)):
        length_list.append(len(word_list[index]))# = len(word_list[index])
    return length_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    count = 0
    for index in range(len(numbers)):
        count += int(numbers[index])
    return count

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    count = 1
    for index in range(len(numbers)):
        count = count * numbers[index]
    return count

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    count = 0
    for index in range(len(numbers)):
        count += int(numbers[index])
    avg = count/len(numbers)
    return avg

