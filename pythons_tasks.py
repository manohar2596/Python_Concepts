'''Certainly! Here's a Python program that defines a binary tree using the
Node class and then prints all the leaf nodes of the tree:'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def print_leaf_nodes(root):
#     if root is None:
#         return

#     if root.left is None and root.right is None:
#         print(root.data)

#     print_leaf_nodes(root.left)
#     print_leaf_nodes(root.right)

# # Example usage:
# # Create a binary tree
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# # Print leaf nodes
# print("Leaf nodes:")
# print_leaf_nodes(root)


'''Defines a Python function called is_unique_string that checks 
   if a given input string contains only unique characters. 
   Here's how the code works:'''

# def is_unique_string(input_string):
#     # Create a set to store unique characters
#     unique_chars = set()

#     for char in input_string:
#         # If the character is already in the set, it's a duplicate
#         if char in unique_chars:
#             return False
#         else:
#             unique_chars.add(char)

#     return True

# # Example usage:
# input_str = input("Enter a string: ")
# is_unique = is_unique_string(input_str)
# if is_unique:
#     print("The string is unique.")
# else:
#     print("The string contains duplicate characters.")


'''Defines a Python function called find_missing_number that
   is used to find a missing number in a sequence of 
   consecutive numbers. Here's how the code works:'''

# Method 1

# def find_missing_number(numbers):
#     n = len(numbers) + 1
#     expected_sum = n * (n + 1) // 2
#     print(expected_sum)
#     actual_sum = sum(numbers)
#     print(actual_sum)
#     missing_number = expected_sum - actual_sum
#     return missing_number

# # Example usage:
# input_numbers = [1, 2, 4, 5, 6]
# missing_num = find_missing_number(input_numbers)
# print("The missing number is:", missing_num)

# Method 2

# num = [1,2,3,4,6]

# n = len(num) + 1
# exp_num = n * (n+1) // 2
# actu_num = sum(num)
# mising_num = exp_num - actu_num
# print(mising_num)

'''Defines a Python function called is_parentheses_balanced
   that checks if a given input string contains balanced 
   parentheses. Here's how the code works:'''

# def is_parentheses_balanced(input_string):
#     stack = []
#     opening_parentheses = ['(', '[', '{', '<']
#     closing_parentheses = [')', ']', '}', '>']
#     parentheses_map = {')': '(', ']': '[', '}': '{', '>': '<'}

#     for char in input_string:
#         if char in opening_parentheses:
#             stack.append(char)
#         elif char in closing_parentheses:
#             if not stack or stack[-1] != parentheses_map[char]:
#                 return False
#             stack.pop()

#     return len(stack) == 0

# # Example usage:
# input_str = input("Enter a string: ")
# is_balanced = is_parentheses_balanced(input_str)
# if is_balanced:
#     print("Parentheses are balanced.")
# else:
#     print("Parentheses are not balanced.")


'''Defines a Python function called check_substring_match
   that checks if a given substring exists in a string 
   in the same order as the characters appear in the
   substring. Here's how the code works:'''

# def check_substring_match(string, substring):
#     string_index = 0

#     for char in substring:
#         # Find the next occurrence of the character in the string
#         string_index = string.find(char, string_index)

#         # If the character is not found or it is not in the expected order, return False
#         if string_index == -1 or string_index < string_index - 1:
#             return False

#         # Move to the next character in the string
#         string_index += 1

#     # If all characters are found and in the expected order, return True
#     return True

# # Example usage:
# string = "mnqrstabcdefmnoplq"
# substring = "amntcdp"

# if check_substring_match(string, substring):
#     print("Pass")
# else:
#     print("Fail")

'''using Python's socket module to obtain the 
   IP address associated with the local host (your computer).'''

# import socket

# ipaddr = socket.gethostbyname(socket.gethostname())
# print(ipaddr)

'''Determine whether a given string is a palindrome'''

# Method 1

# def palindrom(string):
#     palin = string[::-1]
#     if palin == string:
#         print("Is palindrome")
#     print("No")
# palindrom("madams")

# Method 2

# def is_palindrome(string):
#     # Remove spaces and convert to lowercase
#     string = string.replace(" ", "").lower()
#     print(string)
#     reversed_string = string[::-1]
#     return string == reversed_string

# # Example usage:
# text = "Madam Arora malayalam"
# if is_palindrome(text):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

'''Reverse a string'''

# str = "shteyfhhgask"

# rev_str =  range(len(str) -1, -1 ,-1)
# rev = ""
# for i in rev_str:
#     rev += str[i]
# print(rev)

'''Defines a Python function called remove_special_chars
   that removes special characters from a given string 
   and converts uppercase letters to lowercase. 
   Here's how the code works:'''

# def remove_special_chars(string):
#     special_chars = [",", ":", "!", "@", "#"]
#     result = ""

#     for char in string:
#         if ord(char) not in range(33, 127) or char in special_chars:
#             continue
#         elif char.isupper():
#             result += char.lower()
#         else:
#             result += char

#     return result

# # Example usage:
# text = "H@i Th#ere!"
# cleaned_text = remove_special_chars(text)
# print(cleaned_text)

'''Defines two functions, factorial and factorial_series,
   to calculate and print factorial values of numbers in
   a series. Here's how the code works:'''

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def factorial_series(n):
#     for i in range(1, n+1):
#         print(f"Factorial of {i} is: {factorial(i)}")

# # Example usage:
# factorial_series(4)

'''Defines a Python function called is_prime to check
   if a given number is prime or not. Here's how the code works:'''

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# # Example usage:
# num = 17
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

'''Appears to be an implementation of a function called
   is_anagram that checks if two input strings are anagrams of each other'''

# def is_anagram(str1, str2):
#     return sorted(str1.lower()) == sorted(str2.lower())

# string1 = "listen"
# string2 = "silent"
# if is_anagram(string1, string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

'''Performs a sorting operation on the list L using 
   the bubble sort algorithm after it has been initially
   sorted with the sort() method.'''

# Method 1

# L1 = [3,5,9]
# L2 = [4,5,6]
# L = L1+L2
# L.sort()
# print(L)
# len_L = len(L)
# print(len_L)

# i = 0

# while i < len_L -1:

#     j = 0
#     while j < len_L -i -1:

#         if L[j] > L[j+1]:
#             L[j], L[j+1] = L[j+1], L[j]
#         j +=1
#     i+=1

# print(L)

# Method 2

# L1 = [1,7,2,3,6]
# L2 = [9,5,8,4,0]
# L3 = L1 + L2

# i = 0
# while i < len(L3) - 1:
#     j = 0
#     while j < len(L3) - i - 1:
#         if L3[j] > L3[j+1]:
#             L3[j], L3[j+1] = L3[j+1], L3[j]
#         j = j +1
#     i = i +1


# print(L3)

'''Defines a function called fun that takes a string as input,
   removes specific special characters (",", ":", "!") from 
   the string, and then converts the resulting string to lowercase.'''

# def fun(string):
#     special_char = [",", ":", "!"]
#     result = ""
#     for char in string:
#         if char not in special_char:
#             result += char
#     print(result.lower())

# fun("h,ello, :Manu!")

'''Defines a Python function called asci_fun that takes
   an input string and returns a new string where all 
   uppercase letters are converted to lowercase, 
   and non-alphabetic characters are removed. '''

# def asci_fun(input_string):
#     result = ""
#     for char in input_string:
#         if char.isalpha():
#             if char.isupper():
#                 result += chr(ord(char) + 32)
#             else:
#                 result += char
#     return result

# input_string = "A pen, is :Si 'neP .a"
# result = asci_fun(input_string)
# print(result)

'''converts any uppercase alphabetic characters to 
   lowercase while preserving non-alphabetic characters.'''

# str = "Hello! , Ram:"

# result = ""

# for i in str:
#     if i.isalpha():
#         if i.isupper():
#             result += chr(ord(i) + 32)
#         else:
#             result += i
# print(result) 

'''Prints the command-line arguments passed to the script.
   Prints the current working directory.
   Prints platform information.'''

# import sys
# import os

# def main():
#     # Print command-line arguments
#     print("Command-line arguments:")
#     for arg in sys.argv:
#         print(arg)

#     # Print current working directory
#     print("Current working directory:")
#     print(os.getcwd())

#     # Print platform information
#     print("Platform information:")
#     print(sys.platform)

# if __name__ == '__main__':
#     main()

'''calculates the missing number in a sequence of numbers'''

# num = [1,2,3,5,6]
# n = len(num) + 1
# print(n)
# exp_num = (n * (n+1)) // 2
# print(exp_num)
# acut_num = sum(num)
# missi_num = exp_num - acut_num
# print(missi_num)

'''calculate the factorial of a number.'''

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# print(factorial(5))

'''Generates a list of odd numbers from 1 to 49, shuffles 
   the list, and then pops a random odd number from the list.'''

# import random
# odd_num = []
# for i in range(1, 50):
#     if i % 2 != 0:
#         odd_num.append(i)
# random.shuffle(odd_num)
# random_odd = odd_num.pop()
# print(random_odd)
# print(odd_num)

'''Takes a file path as an argument. This function opens the 
   file located at the specified path, reads its content line
   by line, and counts the occurrences of the letter "e" in each line. 
   It then prints the total count of "e" in the entire file.'''

# def fun_file(path):
#     count = 0
#     with open(path, "r") as f:
#         for i in f:
#             count += i.count("e")
#     print(count)
# fun_file("File path")

'''reverses a given string.'''

# str = "adlnsajbackjb"
# rev_str = ""
# for i in range(len(str) - 1, -1, -1):
#     rev_str += str[i]
# print(rev_str)

'''Defines two functions, has_duplicat_lines and count_lines, 
   to check for and count lines with duplicate words in a file.'''

# def has_duplicat_lines(line):
#     word = line.strip().split()
#     uniq_word = set(word)
#     print(len(word) != len(uniq_word))

# def count_lines(path):
#     count = 0
#     with open(path, "r") as f:
#         for i in f:
#             if not has_duplicat_lines(i):
#                 count += 1
#     print(count)


# count_lines("File path")

'''Defines a function is_prime to check if a number 
   is prime and another function print_prime_num to print 
   prime numbers up to a given limit. When you call print_prime_num(100), 
   it prints the prime numbers from 2 to 100.'''

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def print_prime_num(n):
#     p_num = []
#     for i in range(2, n+1):
#         if is_prime(i):
#             p_num.append(i)
#     print(p_num)

# print_prime_num(100)


'''Finding duplicate numbers in a list and creating a list of unique numbers. '''

# Section 1: Finding Duplicate Numbers

# num = [1,3,2,3,4,6,5,7,8,9,1,1]
# dup_num = []
# for i in num:
#     if num.count(i) > 1 and i not in dup_num:
#         dup_num.append(i)
# print(dup_num)

# Section 2: Creating a List of Unique Numbers

# num = [1,2,3,4,5,2,6,7,5,9]

# dup_num = []

# for i in num:
#     if i not in dup_num:
#         dup_num.append(i)
# print(dup_num)

'''Merges two dictionaries, d1 and d2, into a new 
   dictionary d12 such that common keys have their values 
   combined into lists, and unique keys are added directly.'''

# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"c": 4, "d": 5, "e": 6}

# d12 = {}

# for key, value in d1.items():
#     if key in d2:
#         d12[key] = [value, d2[key]]
#     else:
#         d12[key] = value
# for key, value in d2.items():
#     if key not in d12:
#         d12[key] = value
# print(d12)

'''finds and prints the common elements between two lists, list1 and list2. '''

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements = []
# for element in list1:
#      if element in list2:
#           common_elements.append(element)

# print(common_elements)

'''sum of all the elements in the list l.'''

# l =[1,2,3,4,5]
# l1 = 0
# for i in l:
#     l1 += i

# print(l1)

'''checking whether two strings, str1 and str2, are anagrams of each other.'''

# str1 = "silent"
# str2 = "lsten"

# if len(str1) != len(str2):
#     print(False)
# str1 = sorted(str1.lower()) 
# str2 = sorted(str2.lower())

# if str1 == str2:
#     print(True)

''' print the vowels from the original_str.'''

# original_str = "Hello manohar"
# vowels = "aeiou"
# new_str = ""

# for char in original_str:
#     if char.lower() in vowels:
#         new_str += char

# print(new_str)

'''characters of the input string str into two categories: 
   vowels and consonants. It then prints the vowels and consonants separately.'''

# str = "Hello manohar"

# vowels = " "
# conso = " "

# for char in str:
#     if char.lower() in "aeiou":
#         vowels += char
#     else:
#         conso += char
# print(vowels, conso)

'''calculates the square root of each element in the input_list 
   and stores the results in a new list sqrt_list.'''
# Method 1

# import math

# input_list = [2, 3, 1, 88, 22, 15]
# sqrt_list = []

# for i in input_list:
#     sqrt_list.append(math.sqrt(i))
# print(sqrt_list)

# Method 2

# import math

# input_list = [2, 3, 1, 88, 22, 15]
# sqrt_list = [math.sqrt(num) for num in input_list]
# print(sqrt_list)

''' Here's a Python program that prints prime numbers for every 10 numbers'''

# import math

# def fun_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# def print_prime(start, end):
#     for num in range(start, end + 1):
#         if fun_prime(num):
#             print(num, end=" ")
#         if num % 10 == 0:
#             print()

# print_prime(1, 100)

'''Find the missing number'''

# num = [1,2,3,4,6,7,8]

# n = len(num) + 1
# excp_num = n * (n + 1) // 2
# actual_sum = sum(num)
# missing = excp_num - actual_sum

# print(missing)

'''defines a function merge_and_sort_lists that merges and 
   sorts two input lists, list1 and list2, into a single merged and sorted list.'''

# def merge_and_sort_lists(list1, list2):
#     merged_list = []
#     i, j = 0, 0

#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1

#     while i < len(list1):
#         merged_list.append(list1[i])
#         i += 1

#     while j < len(list2):
#         merged_list.append(list2[j])
#         j += 1

#     return merged_list

# # Example usage
# list1 = [1, 4, 7, 9]
# list2 = [2, 5, 8, 10]
# merged_and_sorted = merge_and_sort_lists(list1, list2)
# print("Merged and sorted list:", merged_and_sorted)

'''sorting a list l in descending order and then printing 
the element at the 2nd position (0-based index) in the sorted list.'''

# l = [12,13,5,2,6,7,8]

# sort = sorted(l)
# list_sort = sort[::-1]
# print(list_sort[2])

''' removing duplicates from sublists within the 2D list k 
    and storing the modified sublists in both sub_list and k_list.'''

# k = [
#     [123, 234, 345, 234, 321, 444],
#     [456, 123, 434, 567, 678, 678, 123],
#     [456, 345, 333, 888, 777, 456, 999, 222],
# ]

# # Using sub_list to store modified sublists without duplicates
# sub_list = []
# for i in k:
#     sub_list.append(list(set(i)))

# print("Sublist with duplicates removed:")
# print(sub_list)

# # Using k_list to store modified sublists without duplicates
# k_list = []
# for i in k:
#     k_list.append(list(set(i)))

# print("\nk_list with duplicates removed:")
# print(k_list)

'''separates the elements of a tuple t into two lists: 
   int_t for integer elements and str_t for string elements'''

# t = (123, 'abc', 'def', 345, 'sss', 999)
# int_t = []
# str_t = []

# for i in t:
#     if type(i) == int:
#         int_t.append(i)
#     elif type(i) == str:
#         str_t.append(i)

# print("Integer elements:", int_t)
# print("String elements:", str_t)

'''separates the elements of list l into two lists:
   l2 for elements equal to 1 and l3 for elements not equal to 1.
   Then, it concatenates the two lists to produce the final result. '''

# l = [0, 1, 3, 0, 1, 2, 0, 1, 2, 3, 4, 1, 6, 3]
# l2 = []
# l3 = []

# for i in l:
#     if i == 1:
#         l2.append(i)
#     else:
#         l3.append(i)
# print(l2+l3)

'''reverses a string string and then prints the character at the 1st index of the reversed string.'''

# string = "Manohar"
# rev_str = " "
# for i in range(len(string) -1 , -1, -1):
#     rev_str += string[i]
# print(rev_str[1])

'''rearranges the elements in the list l by moving all the 1 
   values to the beginning of the list while preserving the order of other elements.'''

# l = [0, 1, 3, 0, 1, 2, 0, 1, 2, 3, 4, 1, 6, 3]
# output = []

# # Move all ones to the start of the list
# for i in l:
#     if i == 1:
#         output.insert(0, i)
#     else:
#         output.append(i)

# print(output)

'''merges and sorts two lists, list1 and list2, into a single list output.'''

# list1 = [1, 5, 6, 9, 11]
# list2 = [3, 4, 7, 8, 10]

# output = []

# i, j = 0, 0

# while i < len(list1) and j < len(list2):
#     if list1[i] < list2[j]:
#         output.append(list1[i])
#         i = i + 1
#     else:
#         output.append(list2[j])
#         j = j + 1

# print(output)

'''swaps the case (changes uppercase letters to lowercase and vice versa) 
  of each character in the string str1 while leaving non-alphabetic characters unchanged.'''

# str1="Great Power"
# res = " "

# for i in range(0, len(str1)):
#     if str1[i].islower():
#         res += str1[i].upper()
#     elif str1[i].isupper():
#         res += str1[i].lower()
#     else:
#         res += str1[i]

# print(res)

'''removes all non-alphanumeric characters (anything that is not a letter or digit) 
   from the string string and stores the result in a new string str.'''

# string = "Ge;ek * s:fo ! r;Ge * e*k:s !"
# str = ""
# for i in string:
#     if i.isalnum():
#         str += i
# print(str)

''' first filters out non-alphabetic characters from the string, 
    and then it swaps the case of the alphabetic characters.'''

# string = "Ge;ek * s:fo ! r;Ge * e*k:s !"
# result = ""

# for i in string:
#     as_va = ord(i)
#     if (65 <= as_va <= 95) or (97 <= as_va <= 122):
#         result += i
# res = ""
# for j in range(0, len(result)):
#     if result[j].islower():
#         res += result[j].upper()
#     elif result[j].isupper():
#         res += result[j].lower()
#     else:
#         res += result[j]
# print(res)
# print(result)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     res = n * factorial(n -1)
#     return res
# print(factorial(3))

''' calculate the factorial of a given number num using recursion.'''

# def rec_fact(n):
#     if n == 1:
#         return 1
#     else:
#         res = n * rec_fact(n - 1)
#         return res

# num = int(input("Enter a number: "))

# if num < 0:
#     print("Factorial does not exist for negative numbers.")
# elif num == 0:
#     print("Factorial of 0 is 1.")
# else:
#     print(f"{num}! is:", rec_fact(num))

'''print prime numbers within a specified range, from lower to upper.'''

# lower = 10
# upper = 100
# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

'''merges two dictionaries d1 and d2 into a new dictionary d12, 
   ensuring that if keys are common between d1 and d2, their values 
   are stored in a list within d12. If a key exists only in one of 
   the dictionaries, it is simply added to d12 with its corresponding value.'''

# Exapmple 1
#   
# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"c": 4, "d": 5, "e": 6}

# d12 ={}

# for key ,value in d1.items():
#     if key in d2:
#         d12[key] = [value, d2[key]]

#     else:
#         d12[key] = value

# for key, value in d2.items():
#     if key not in d12:
#         d12[key] = value

# print(d12)

# Example 2

# d1 = {"a":3, "b":4, "c":8, "d":2}
# d2 = {"c":5, "d":1, "e":7, "f":9}

# d12 = {}

# for key, value in d1.items():
#     if key in d2:
#         d12[key] = [value, d2[key]]
#     else:
#         d12[key] = value

# for key, value in d2.items():
#     if key not in d12:
#         d12[key] = value
# print(d12)

# Example 3

# d1 = {"a": 3, "b": 4, "c": 8, "d": 2}
# d2 = {"c": 5, "d": 1, "e": 7, "f": 9}
# d3 = {"c": 0, "f": 3, "g": 7, "h": 12}
# d123 = {}

# # Merge d1, d2, and d3 into d123
# for key, value in d1.items():
#     if key in d2 and key in d3:
#         d123[key] = [value, d2[key], d3[key]]
#     elif key in d2:
#         d123[key] = [value, d2[key]]
#     elif key in d3:
#         d123[key] = [value, d3[key]]
#     else:
#         d123[key] = value

# for key, value in d2.items():
#     if key not in d123:
#         d123[key] = value

# for key, value in d3.items():
#     if key not in d123:
#         d123[key] = value

# print(d123)

# Example 4

# d1 = {"a": 3, "b": 4, "c": 8, "d": 2}
# d2 = {"c": 5, "d": 1, "e": 7, "f": 9}

# d12 = {}

# for key, value in d1.items():
#     if key in d2:
#         d12[key] = [value, d2[key]]
#     else:
#         d12[key] = value

# for key, value in d2.items():
#     if key in d12:
#         d12[key] = [value, d12[key]]
#     else:
#         d12[key] = value

# print(d12)

# Example 5

# d1 = {"a": 3, "b": 4, "c": 8, "d": 2}
# d2 = {"c": 5, "d": 1, "e": 7, "f": 9}

# d12 = {}

# for key, value in d1.items():
#     if key in d2:
#         d12[key] = [value, d2[key]]
#     else:
#         d12[key] = value

# for key, value in d2.items():
#     if key not in d12:
#         d12[key] = value

# print(d12)

''' two dictionaries, d1 and d2, and you want to perform various 
    operations like merging the dictionaries, extracting values, and extracting keys. '''

# Method 1

# d1= {'A1':1, 'A2':2,'A2':3, 'A3':4}
# d2= {'B1':6,'B2':7,'B3':8,'B4':9} 
# q1={}
# q1.update(d1)
# q1.update(d2)
# q2=[]
# for x in d1.values():
#     q2.append(x)
# for x in d2.values():
#     q2.append(x)
# print(q2)
# q3=[]
# for x in d1.keys():
#     q3.append(x)
# for x in d2.keys():
#     q3.append(x)
# print(q3)

# Method 2

# dict_1= {'A1':1, 'B1':2,'C1':3, 'D1':4}
# dict_2= {'M':6,'N':7,'o':8,'p':9}
# dict_3 = {}
# dict_3.update(dict_1)
# dict_3.update(dict_2)
# L = []
# L2 = []
# for i in dict_3:
#     print(i)
#     L.append(dict_3[i])
# for j in dict_3:
#     L2.append(j)
# print(L)
# print(L2)

'''using the random module in Python to perform various random operations.'''

# import random

# numbers = [1, 2, 3, 4, 5]
# print(random.random())

# print(random.randint(1,100))

# print(random.choice(numbers))

# random.shuffle(numbers)
# print(numbers)

'''Reverse a string'''

# Method 1
# str = "manohar"

# print(str[::-1])

# Method 2

# rev_str = "".join(reversed(str))
# print(rev_str)


'''Write a program to print Prime numbers in python'''

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#         return True

# def print_prime_num(start, end):
#     prim_num = []
#     for num in range(start, end+1):
#         if is_prime(num):
#             prim_num.append(num)
#     print(prim_num)

# print_prime_num(1,20)

'''find and store the key-value pairs where the values are unique 
   in a new dictionary duplicate, and you also want to create a 
   list temp to store the unique values.'''

# test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}

# temp = []
# duplicate = {}

# for key, value in test_dict.items():
#     if value not in temp:
#         temp.append(value)
#         duplicate[key] = value
# print(duplicate)
# print(temp)

'''In dictionary swapping the key and value'''

# original_dict = {'a': 1, 'b': 2, 'c': 3}
# swap_dict = {}
# for key , value in original_dict.items():
#     swap_dict[value] = key
# print(swap_dict)

'''count the occurrences of the word "Nutanix" (case-insensitive) 
   in a given text file. using regular expressions.'''

# import re

# with open("File path", "r", encoding="utf-8") as f:
#     content = f.read()
#     matches = re.findall(r"[nN]utanix", content)
#     count = len(matches)
#     print(count)

'''finds and counts the number of permutations of the substring "mamal" within the string "x."'''

# from itertools import permutations

# x = "mamalxxxxlammaaxxxxamalm"
# sub = "mamal"

# # Get all permutations of the substring
# sub_permutations = set(permutations(sub))

# # Count the occurrences of permutations in the string x
# count = 0
# for i in range(len(x) - len(sub) + 1):
#     if tuple(x[i:i + len(sub)]) in sub_permutations:
#         count += 1

# print("Number of permutations of 'mamal' in 'x':", count)

'''finds the maximum repeated character(s) in a given 
   string using the collections.Counter class.'''

# from collections import Counter

# def get_max_repeated_char(string):
#     char_count = Counter(string)
#     print(char_count)
#     max_count = max(char_count.values())
#     print(max_count)
#     max_chars = [char for char, count in char_count.items() if count == max_count]
#     return max_chars

# # Example usage
# max_chars = get_max_repeated_char("aaabbbbbsssssshhhhhhhhhhgggggggggg")

# print("Maximum repeated character(s):", max_chars)

'''Swap the dictionary'''

# dict = {"a":1, "b":2, "c":3, "d":4}

# swap_dict = {}
# li = []
# for key, value in dict.items():
#     li.append(value)

# for key, value in dict.items():
#     if value == li[2]:
#         swap_dict[value] = key
#     else:
#         swap_dict[key] = value
# print(swap_dict)

'''finds the character(s) with the maximum and minimum counts
   in the given string using the collections.Counter class.'''

# from collections import Counter

# string = "aadddddnnnnnnnnttttnenennenwnssnsnsnsnnsnso"

# item = Counter(string)
# mini = []
# maxi = []
# for key, value in item.items():
#   if value == min(item.values()):
#     mini.append(key)
#   if value == max(item.values()):
#     maxi.append(key)
# print(maxi)
# print(mini)


'''Squares of Numbers:'''

# squares = [x ** 2 for x in range(1,6)]
# print(squares)

'''Filtering Even Numbers:'''

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_num = [x for x in numbers if x % 2 == 0]
# print(even_num)

'''Even and Odd Labeling:'''

# even_odd = [x if x % 2 != 0 else "even" for x in numbers]
# print(even_odd)

'''Uppercase Letters from a String:'''

# string = "Manohar Achari"
# upper_case = [i.upper() for i in string if i.isalpha()]
# print(upper_case)

'''list comprehension is used to categorize elements in the list 
   into three categories: "number" if an element is an integer, 
   "string" if it's a string, and "tuple" if it's a tuple.'''

# list = [1, 2, "manu", 3, "chari", (1,2,3)]

# new_list = ["number" if isinstance(i, int) else "string" if isinstance(i, str) else "tuple" for i in list]
# print(new_list)

'''various string operations you performed using the re module:'''

# import re
# str = "Hello World"
# #re.sub
# sub_str = re.sub("World", "Manu", str)
# #re.findall
# find_str = re.findall("l", str)
# #re.split
# spl_str = re.split("l", str)
# #re.search
# se_str = re.search("He", str)
# sp_str = re.search("o", str)
# #re.match
# match = re.match("Hello World", str)
# print(sp_str.span())
# print(match)


'''counting the occurrences of each number in the list'''

# from collections import Counter

# L = [2, 2, 1, 1, 1, 2, 2]

# # Use Counter to count occurrences of each number in the list
# count_dict = Counter(L)

# print(count_dict)

'''find the maximum count and the corresponding number from 
   the count_dict is correct. It will correctly identify the 
   number with the highest count in the list'''

# max_count = 0
# max_num = None

# for num, count in count_dict.items():
#     if count > max_count:
#         max_count = count
#         max_num = num

# # Print the maximum repeated number
# print("Maximum repeated number:", max_num)

'''find and print the number with the highest count in the list L.'''

# L = [2, 2, 1, 1, 1, 2, 2]

# count_dict = {}

# for num in L:
#     count_dict[num] = count_dict.get(num, 0) + 1
# print(count_dict)

# max_num = max(count_dict, key=count_dict.get)

# print("Maximum repeated number:", max_num)

'''merge list1 and list2 correctly, creating a merged list with 
   elements from both lists in the specified order.'''

# list1 = [1, 3, 5]
# list2 = [2, 4, 6, 8]

# i, j = 0, 0

# merged = []

# while i < len(list1) and j < len(list2):
#     merged.append(list1[i])
#     i += 1
#     merged.append(list2[j])
#     j += 1

# while i < len(list1):
#     merged.append(list1[i])
#     i += 1

# while j < len(list2):
#     merged.append(list2[j])
#     j += 1

# print(merged)

'''removes duplicates from the input list list and then prints the unique elements in reverse order.'''

# def remove_duplicates(input_list):
#     result = []
#     for item in input_list:
#         if item not in result:
#             result.append(item)
#     print(result[::-1])

# my_list = [1, 2, 3, 2, 4, 3, 5, 4, 6, 7, 6, 5]
# remove_duplicates(my_list)


'''creating a list called List that contains elements common to 
   both my_list1 and my_list2 while removing duplicates.'''

# my_list1 = [1, 2, 3, 4, 5]
# my_list2 = [4, 5, 6, 7, 8]

# common_elements = []

# for item in my_list1:
#     if item in my_list2 and item not in common_elements:
#         common_elements.append(item)

# print(common_elements)


'''Defines two classes, A and B, demonstrating the use of abstract methods and inheritance.'''

# Example 1: Abstract Base Class A and Subclass B

# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def display(self):
#         print("This is class A function")
# class B(A):
#     def display(self):
#         print("This is class B function")

# obj = B()
# obj.display()

'''Defines two classes, Rectangle and Circle, demonstrating how to 
   create objects and access methods in a more straightforward manner.'''

# Example 2: Classes Rectangle and Circle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14 * self.radius


# Creating objects
# rectangle = Rectangle(5, 3)
# circle = Circle(4)

# # Accessing methods
# print("Area of the rectangle:", rectangle.area())
# print("Perimeter of the rectangle:", rectangle.perimeter())
# print("Area of the circle:", circle.area())
# print("Perimeter of the circle:", circle.perimeter())


'''Defines a simple hierarchy of geometric shapes using Python's 
   abstract base class (ABC) and abstract methods. The Shape class 
   is an abstract base class with two abstract methods: area and perimeter. 
   Subclasses like Rectangle and Circle inherit from Shape and provide 
   concrete implementations for these methods.'''

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 2 * 3.14 * self.radius


# # Creating objects
# rectangle = Rectangle(5, 3)
# circle = Circle(4)

# # Accessing abstract methods
# print("Area of the rectangle:", rectangle.area())
# print("Perimeter of the rectangle:", rectangle.perimeter())
# print("Area of the circle:", circle.area())
# print("Perimeter of the circle:", circle.perimeter())


'''the elements of the list l, compares adjacent elements, 
   and appends the maximum of each pair to the list l1. 
   The try block helps avoid an IndexError when accessing l[i + 1], 
   and you've correctly handled the case where the range is reached with the except block.'''

# l = [1, 2, 4, 2, 3, 4, 6]
# l1 = []

# try:
#     for i in range(len(l) - 1):
#         if l[i] >= l[i + 1]:
#             l1.append(l[i])
#         else:
#             l1.append(l[i + 1])
# except IndexError:
#     print("Range reached")

# print(l1)


'''Replace the small x to capital X'''

# import re
# str_1 = "nutanix"

# str_1 = str_1.replace("x", "X")
# print(str_1)


'''check whether the index i is already present in the List1.'''

# L1 = [1, 2, 3, 4, 1, 2, 3, 7, 8]
# seen = set()
# duplicates = []

# for num in L1:
#     if num in seen:
#         duplicates.append(num)
#     else:
#         seen.add(num)

# print("Duplicate elements:", duplicates)


'''counts the occurrences of each number in the list L 
   and stores the counts in a dictionary called count_dict.'''

# L = [2, 2, 1, 1, 1, 2, 2]
# count_dict = {}

# for num in L:
#     if num in count_dict:
#         count_dict[num] += 1
#     else:
#         count_dict[num] = 1
# print(count_dict)


'''Finds pairs of numbers from the list L whose sum is equal to K.'''

# from itertools import combinations

# L=[1,2,4,7,5]
# K=6

# sum_pair = []
# for pair in combinations(L, 2):
#     if sum(pair) == K:
#         sum_pair.append(pair)
# print(sum_pair)

'''Finds the maximum repeated number in the list L and its count.'''

# L = [2,2,1,1,1,2,2]
# res = {}

# for i in L:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

# max_num = max(zip(res.values(), res.keys()))
# print(max_num)

'''performs selection sort on the input list argument and sorts it 
   in ascending order. The selection sort algorithm repeatedly 
   finds the minimum element from the unsorted part of the list and moves it to the beginning.'''

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         # print(min_index)
#         for j in range(i+1, n):
#             # print(j)
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# # Example usage:
# arr = [7, 2, 5, 1, 9, 3]
# selection_sort(arr)
# print(arr)  # Output: [1, 2, 3, 5, 7, 9]


'''extracting the date and time from the given string'''

# import re

# abc = "gher/2021/ertdwererw/fold1/fold2/fold/2023-07-19/12:49"

# date_pattern = r'\d{4}-\d{2}-\d{2}'
# time_pattern = r'\d{1,2}:\d{2}'

# res_date = re.findall(date_pattern, abc)
# res_time = re.findall(time_pattern, abc)

# print("Dates:", res_date)
# print("Times:", res_time)


'''separating vowels and consonants from an input string and counting their occurrences is correct.'''

# def separate_vowels_consonants(input_string):
#     vowels = "aeiouAEIOU"
#     vowel_count = 0
#     consonant_count = 0
#     vowel_string = ""
#     consonant_string = ""

#     for char in input_string:
#         if char.isalpha():
#             if char in vowels:
#                 vowel_count += 1
#                 vowel_string += char
#             else:
#                 consonant_count += 1
#                 consonant_string += char

#     return vowel_string, consonant_string, vowel_count, consonant_count

# # Example usage:
# input_string = "Hello, World!"
# vowels, consonants, vowel_count, consonant_count = separate_vowels_consonants(input_string)
# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Vowel count:", vowel_count)
# print("Consonant count:", consonant_count)

############# Decorators ############

'''Example of using a decorator called str_upper to modify 
   the behavior of the print_str function. '''

# def str_upper(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#
#     return inner
#
#
# @str_upper
# def print_str():
#     return "Hello World"
#
#
# print(print_str())

'''example of using a decorator called div_decorate 
   to modify the behavior of a div function, which performs division.'''

# def div_decorate(func):
#     def inner(x, y):
#         if y == 0:
#             return "Give proper input"
#         return func(x, y)
#
#     return inner
#
# @div_decorate
# def div(a, b):
#     return a / b
#
# print(div(2, 2))

'''Decorator for example of multiple function'''

# def multiple(func):
#     def inner(x, y):
#         if x ==0 or y ==0:
#             return "Give a valid input"
#         return func(x, y)
#     return inner
#
# @multiple
# def mult(a, b):
#     return a * b
# print(mult(20, 10))

'''Defines two decorator functions, upper_id and split_id, 
   and applies them to the ordinary function using decoraters'''

# def upper_id(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#     return inner
# def split_id(func):
#     def wrapper():
#         str2 = func()
#         return str2.split()
#     return wrapper
#
# @split_id
# @upper_id
# def ordinary():
#     return "good morning"
#
# print(ordinary())


'''Defined a nested decorator outer that takes an argument exm. 
   The outer decorator returns another decorator called upper, 
   which, in turn, decorates the ordinary function. '''

# def outer(exm):
#     def upper(func):
#         def inner():
#             str1 = func() + " " + exm
#             return  str1.upper()
#         return inner
#     return upper
#
# @outer("manohar")
# def ordinary():
#     return "good morning"
# print(ordinary())


"""Implementing a rotation of a list to the right by k positions"""
#Method 1
'''
L = [1,2,3,4,5]
k = 2
output = []

for i in range(len(L) - k, len(L)):
    output.append(L[i])
for i in range(0, len(L) - k):
    output.append(L[i])

print(output)

#Method 2

from collections import deque

L = [1,2,3,4,5]
k = 2
output = deque(L)
output.rotate(k)
L = list(output)
print(L)
'''
