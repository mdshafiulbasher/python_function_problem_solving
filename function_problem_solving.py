# 1. Write a Python function to find the maximum of three numbers.
def max_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(max_number(5,10,7))

# 2. Write a Python function to sum all the numbers in a list
def sum_of_list(numbers):
    sum=0
    for num in numbers:
        sum = sum+num
    return sum
numbers_list = [6,8,7,5,2,1,9]
print("sum of the list: ",sum_of_list(numbers_list))

# 3. Write a Python program to reverse a string.
def reverse_string(string):
    string_to_list = []
    for str in string:
        string_to_list.append(str)
    string_to_list.reverse()
    list_to_string = ""
    for list in string_to_list:
        list_to_string = list_to_string+list
    return list_to_string
print("reverse string: ", reverse_string("1234abcd"))

# 4. Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count_upper_lower(sentence):
    remove_space=sentence.replace(" ", "")
    without_space_sentence = remove_space
    count_upper=0
    count_lower=0
    for word in without_space_sentence:
        if word.islower() == True:
            count_lower+=1
        else:
            count_upper+=1
    print("No. of Upper case characters : ",count_upper)
    print("No. of Lower case characters :",count_lower)
count_upper_lower('The quick Brow Fox')

# 5. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def remove_duplicate_item(items):
    unique_list = []
    for item in items:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
number_list = [1,2,3,3,3,3,4,5]
print("Unique List :",remove_duplicate_item(number_list))

# 6. Write a Python program to print the even numbers from a given list.
def even_number(items):
    even_number_list = []
    for item in items:
        if item%2==0:
            even_number_list.append(item)
    return even_number_list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even Number List :", even_number(numbers))