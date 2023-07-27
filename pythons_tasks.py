
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


# num = [1,2,3,4,6]

# n = len(num) + 1
# exp_num = n * (n+1) // 2
# actu_num = sum(num)
# mising_num = exp_num - actu_num
# print(mising_num)

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


# import socket

# ipaddr = socket.gethostbyname(socket.gethostname())
# print(ipaddr)


# def palindrom(string):
#     palin = string[::-1]
#     if palin == string:
#         print("Is palindrome")
#     print("No")
# palindrom("madams")


# str = "shteyfhhgask"

# rev_str =  range(len(str) -1, -1 ,-1)
# rev = ""
# for i in rev_str:
#     rev += str[i]
# print(rev)


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


# def is_anagram(str1, str2):
#     return sorted(str1.lower()) == sorted(str2.lower())

# string1 = "listen"
# string2 = "silent"
# if is_anagram(string1, string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

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


# def fun(string):
#     special_char = [",", ":", "!"]
#     result = ""
#     for char in string:
#         if char not in special_char:
#             result += char
#     print(result.lower())

# fun("h,ello, :Manu!")

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


# str = "Hello! , Ram:"

# result = ""

# for i in str:
#     if i.isalpha():
#         if i.isupper():
#             result += chr(ord(i) + 32)
#         else:
#             result += i
# print(result) 


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


# import socket
# ip = socket.gethostbyname(socket.gethostname())
# print(ip)


# num = [1,2,3,5,6]
# n = len(num) + 1
# print(n)
# exp_num = (n * (n+1)) // 2
# print(exp_num)
# acut_num = sum(num)
# missi_num = exp_num - acut_num
# print(missi_num)

# import random

# num = random.randint(1, 10)
# print(num)

# def factiorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factiorial(num - 1)
        
# print(factiorial(5))


# import random
# odd_num = []
# for i in range(1, 50):
#     if i % 2 != 0:
#         odd_num.append(i)
# random.shuffle(odd_num)
# random_odd = odd_num.pop()
# print(random_odd)
# print(odd_num)

# def fun_file(path):
#     count = 0
#     with open(path, "r") as f:
#         for i in f:
#             count += i.count("e")
#     print(count)
# fun_file("C:\\Users\\ManoharK-2768\\Desktop\\file_01.txt")


# str = "adlnsajbackjb"
# rev_str = ""
# for i in range(len(str) - 1, -1, -1):
#     rev_str += str[i]
# print(rev_str)


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


# count_lines("C:\\Users\\ManoharK-2768\\Desktop\\file_01.txt")

# def is_prime(num):
#     if num < 2:
#         print(False)
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(False)
#     print(True)
# def print_prime_num(n):
#     p_num = []
#     for i in range(2, n+1):
#         if is_prime(i):
#             p_num.append(n)
#     print(p_num)

# print_prime_num(100)

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def print_prime_num(n):
#     prime_num = []
#     for i in range(2, n+1):
#         if is_prime(i):
#             prime_num.append(i)
#     print(prime_num)
# print_prime_num(50)


# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# def print_prime_num(n):
#     prime_num = []
#     for i in range(2, n+1):
#         if is_prime(i):
#             prime_num.append(i)
#     print(prime_num)

# print_prime_num(100)


# num = [1,3,2,3,4,6,5,7,8,9,1,1]
# dup_num = []
OAOA# for i in num:
#     if num.count(i) > 1 and i not in dup_num:
OA#         dup_num.append(i)
# print(dup_num)

OA# num = [1,2,3,4,5,2,6,7,5,9]

OA# dup_num = []
OA
# for i in num:
#     if i not in dup_num:
OA#         dup_num.append(i)
# print(dup_num)
OA
# d1 = {"a": 1, "b": 2, "c": 3}
OA# d2 = {"c": 4, "d": 5, "e": 6}

# d12 = {}

# for key, value in d1.items():
#     if key in d2:
OA#         d12[key] = [value, d2[key]]
#     else:
#         d12[key] = value
# for key, value in d2.items():
#     if key not in d12:
#         d12[key] = value
# print(d12)


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements = []
# for element in list1:
#      if element in list2:
#           common_elements.append(element)

# print(common_elements)
OAOA
# l =[1,2,3,4,5]
OA# l1 = 0
# for i in l:
#     l1 += i
OA    
OA# print(l1)

OA# str1 = "silent"
# str2 = "lsten"
OAOA
OA# if len(str1) != len(str2):
OA#     print(False)
OA# str1 = sorted(str1.lower()) 
OA# str2 = sorted(str2.lower())

OA# if str1 == str2:
#     print(True)
OA
OA# str = "Hello manohar"
# str = ""
# ovels = "aeiou"
# for i in str:
OA#     if i.lower() in ovels:
#         str += i
# print(str)

# str = "Hello manohar"

# vowels = " "
# conso = " "

# for char in str:
#     if char.lower() in "aeiou":
#         vowels += char
#     else:
#         conso += char
# print(vowels, conso)


# import math

# input_list = [2, 3, 1, 88, 22, 15]
# sqrt_list = []

# for i in input_list:
#     sqrt_list.append(math.sqrt(i))
# print(sqrt_list)

# import math

# input_list = [2, 3, 1, 88, 22, 15]
# sqrt_list = [math.sqrt(num) for num in input_list]
# print(sqrt_list)

# Here's a Python program that prints prime numbers for every 10 numbers:
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

# num = [1,2,3,4,6,7,8]
# n = len(num) + 1

# excp_num = n * (n + 1) // 2

# actual_sum = sum(num)

# missing = excp_num - actual_sum

# print(missing)


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


# l = [12,13,5,2,6,7,8]

# sort = sorted(l)
# list_sort = sort[::-1]
# print(list_sort[2])

# k = [
#     [123, 234, 345, 234, 321, 444], 
#     [456, 123, 434, 567, 678, 678, 123], 
#     [456, 345, 333, 888, 777, 456, 999, 222],
#     ]
 
# sub_list = []
# for i in k:
#     list(set(i))
#     sub_list.append(i)

# print(sub_list)
# k_list = []
# for i in k:
#     i = set(i)
#     k_list.append(i)
# print(k_list)
    

# t = (123, 'abc', 'def', 345, 'sss', 999)
# int_t = []
# str_t = []

# for i in t:
#     if type(i) == int:
#         int_t.append(i)
#     else:
#         type(i) == str
#         str_t.append(i)
# print(int_t, str_t)


# l = [0, 1, 3, 0, 1, 2, 0, 1, 2, 3, 4, 1, 6, 3]
# l2 = []
# l3 = []

# for i in l:
#     if i == 1:
#         l2.append(i)
#     else:
#         l3.append(i)
# print(l2+l3)


# string = "Manohar"
# rev_str = " "
# for i in range(len(string) -1 , -1, -1):
#     rev_str += string[i]
# print(rev_str[1])


# l = [0, 1, 3, 0, 1, 2, 0, 1, 2, 3, 4, 1, 6, 3]
# output = []

# # Move all ones to the start of the list
# for i in l:
#     if i == 1:
#         output.insert(0, i)
#     else:
#         output.append(i)

# print(output)

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

# string = "Ge;ek * s:fo ! r;Ge * e*k:s !"
# str = ""
# for i in string:
#     if i.isalnum():
#         str += i
# print(str)

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


# def rec_fact(n):
#     if n == 1:
#         return n
#     else:
#         res = n * rec_fact(n - 1)
#         return res
# num = int(input("enter number: "))

# if num < 0:
#     print("not exist")
# elif num == 0:
#     print(1)
# else:
#     print("{num} is: ", rec_fact(num))


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

# from binarytree import Node
# root = Node(3)
# root.left = Node(6)
# root.right = Node(8)

# # Getting binary tree
# print('Binary tree :', root)

# # Getting list of nodes
# print('List of nodes :', list(root))

# # Getting inorder of nodes
# print('Inorder of nodes :', root.inorder)

# # Checking tree properties
# print('Size of tree :', root.size)
# print('Height of tree :', root.height)

# # Get all properties at once
# print('Properties of tree : \n', root.properties)


# # Creating binary tree
# from given list


# from binarytree import build


# # List of nodes
# nodes =[3, 6, 8, 2, 11, None, 13]

# # Building the binary tree
# binary_tree = build(nodes)
# print('Binary tree from list :\n',
# 	binary_tree)

# # Getting list of nodes from
# # binarytree
# print('\nList from binary tree :',
# 	binary_tree.values)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# def insert(root, value):
#     if root is None:
#         return Node(value)
#     elif value < root.value:
#         root.left = insert(root.left, value)
#     else:
#         root.right = insert(root.right, value)
#     return root


# def print_tree(root, level=0):
#     if root is not None:
#         print_tree(root.right, level + 1)
#         print("   " * level + str(root.value))
#         print_tree(root.left, level + 1)


# # Create the binary tree
# root = None
# root = insert(root, 4)
# root = insert(root, 2)
# root = insert(root, 6)
# root = insert(root, 1)
# root = insert(root, 3)
# root = insert(root, 5)
# root = insert(root, 7)

# # Print the tree
# print("Binary Tree:")
# print_tree(root)

# str = "tutorialspoint"
# # initializing a list to add all the duplicate characters
# duplicate_char = []
# for character in str:
#    # check whether there are duplicate characters or not
#    # returning the frequency of a character in the string
#       if str.count(character) > 1:
#    # append to the list if it is already not present
#          if character not in duplicate_char:
#             duplicate_char.append(character)
# print(*duplicate_char)
# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver.get("https://www.google.com/")

# search_box = driver.find_element(By.NAME, "")
# search_box.send_keys("salaar teaser")
# search_box.submit()
# time.sleep(2)
    
# num = [1,2,3,4,6,7,8,9]

# n = len(num) + 1

# exp = (n * (n + 1)) // 2
# act = sum(num)
# mis = exp - act
# print(mis)


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

# import random

# numbers = [1, 2, 3, 4, 5]
# print(random.random())

# print(random.randint(1,100))

# print(random.choice(numbers))

# random.shuffle(numbers)
# print(numbers)

# str = "manohar"

# print(str[::-1])

# rev_str = "".join(reversed(str))
# print(rev_str)


# Write a program to print Prime numbers in python

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



# test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}

# temp = []
# duplicate = {}

# for key, value in test_dict.items():
#     if value not in temp:
#         temp.append(value)
#         duplicate[key] = value
# print(duplicate)
# print(temp)


# original_dict = {'a': 1, 'b': 2, 'c': 3}
# swap_dict = {}
# for key , value in original_dict.items():
#     swap_dict[value] = key
# print(swap_dict)


# import re

# with open("C:/Users/ManoharK-2768/Desktop/interview_queries.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     matches = re.findall(r"[nN]utanix", content)
#     count = len(matches)
#     print(count)

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


# str = "aaabbbbaaaaccccgggggg"

# ct = max(str)
# print(ct)


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

# def is_prime(num):
#   if num < 2:
#     return False
#   for i in range(2, num):
#     if num % i == 0:
#       return False
#     return True
# def print_prime(n):
#   for i in range(2, n+1):
#     if is_prime(i):
#       print(i)

# print_prime(100)


# squares = [x ** 2 for x in range(1,6)]
# print(squares)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_num = [x for x in numbers if x % 2 == 0]
# print(even_num)

# even_odd = [x if x % 2 != 0 else "even" for x in numbers]
# print(even_odd)

# string = "Manohar Achari"
# upper_case = [i.upper() for i in string if i.isalpha()]
# print(upper_case)


# list = [1, 2, "manu", 3, "chari", (1,2,3)]

# new_list = ["number" if isinstance(i, int) else "string" if isinstance(i, str) else "tuple" for i in list]
# print(new_list)


# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"c": 4, "d": 5, "e": 6}

# merge_dict = {}

# for key, value in d1.items():
#     if key in merge_dict:
#         merge_dict[key].append(value)
#         print(merge_dict)
#     else:
#         merge_dict[key] = [value]

# for key, value in d2.items():
#     if key in merge_dict:
#         merge_dict[key].append(value)
#     else:
#         merge_dict[key] = [value]

# print(merge_dict)

# import re
# str = "Hello World"

# sub_str = re.sub("World", "Manu", str)
# find_str = re.findall("l", str)
# spl_str = re.split("l", str)
# se_str = re.search("He", str)
# sp_str = re.search("o", str)
# match = re.match("Hello World", str)
# print(sp_str.span())
# print(match)

# L = [2, 2, 1, 1, 1, 2, 2]
# count_dict = {}

# Count the occurrences of each number in the list
# for num in L:
#     if num in count_dict:
#         count_dict[num] += 1
#     else:
#         count_dict[num] = 1
# print(count_dict)

# # Find the maximum count and corresponding number
# max_count = 0
# max_num = None

# for num, count in count_dict.items():
#     if count > max_count:
#         max_count = count
#         max_num = num

# # Print the maximum repeated number
# print("Maximum repeated number:", max_num)


# L = [2, 2, 1, 1, 1, 2, 2]

# count_dict = {}

# for num in L:
#     count_dict[num] = count_dict.get(num, 0) + 1
# print(count_dict)
# max_num = max(count_dict, key=count_dict.get)

# print("Maximum repeated number:", max_num)


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
#     merged.append(list1[1])
#     i += 1

# while j < len(list2):
#     merged.append(list2[j])
#     j += 1

# print(merged)

# list1 = [1, 3, 5]
# list2 = [2, 4, 6, 8]

# new_list = [i for i in list1] + [i for i in list2]

# print(new_list)

# new_list = []
# for i in list1:
#     if i > new_list:
#         new_list.append(i)
# for i in list2:
#     if i > new_list:
#         new_list.append(i)
# print(new_list)


# string = "How to troubleshoot if you get exception"

# rev_str = ""

# for i in  range(len(string )-1, -1, -1):
#     rev_str += string[i]

# print(rev_str)

# l1 = [2,4,6]
# l2 = [1,3,5]

# L = []
# i, j = 0, 0

# while i < len(l1) and j < len(l2):
#     L.append(l1[i])
#     i += 1
#     L.append(l2[j])
#     j += 1
# while i < len(l1):
#     L.append(l1[i])
#     i += 1
# while j < len(l2):
#     L.append(l2[j])
#     j += 1
# print(L)


# def remove_dupl(list):
#     result = []
#     rev_list = []
#     for i in list:
#         if i not in result:
#             result.append(i)
#     print(result[::-1])

# my_list = [1, 2, 3, 2, 4, 3, 5, 4, 6, 7, 6, 5]
# remove_dupl(my_list)

# my_list1 = [1, 2, 3, 4, 5]
# my_list2 = [4, 5, 6, 7, 8]

# List = []

# for i in my_list1:
#     if i in my_list2 and i not in List:
#         List.append(i)
# print(List)

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



# def factiorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factiorial(n - 1)
# def print_fact(limit):
#     for i in range(1, limit + 1):
#         print(factiorial(i))

# print_fact(5)

# l=[1,2,4,2,3,4,6]
# l1=[]

# try:
#     for i in l:
#         if l[i]>=l[i+1]:
#             l1.append(i)
#         else:
#             l1.append(l[i+1])

# except:
#     print("range reached")

# print(l1)


# import re
# str_1 = "nutanix"
# print(str_1.replace("x", "X"))

# print(str_1)

# L1 = [1,2,3,4,1,2,3,7,8]
# L = sorted(L1)
# List1 = []
# for i in range(len(L)):
#     # print(L[i])
#     if i in List1:
#         print("true")
#     else:
#         print("false")
# print(List1) 


# L = [2, 2, 1, 1, 1, 2, 2]
# count_dict = {}

# for num in L:
#     if num in count_dict:
#         count_dict[num] += 1
#     else:
#         count_dict[num] = 1
# print(count_dict)


# L1 = [1,2,3,4,1,2,3,7,8]

# cd = {}

# for i in L1:
#     if i in cd:
#         cd[i] += 1
#     else:
#         cd[i] = 1
# print(cd)



    
# string = "manohar how are you"
# str1 = string.count("o")
# print(str1)



# L1 = [1,2,3,4,1,2,3,7,8]
# L = []
# for i in L1:
#     if i not in L:
#         L.append(i)
# print(L)

# d1 = {"a":1, "b":2, "c":3}
# d2 = {"c":4, "d":5, "e":6}
# d12 = {}
# for key, value in d1.items():
#     if key in d2:
#         d12[key] = [value, d2[key]]
#     else:
#         d12[key] = value
# for key, value in d2.items():
#     if key not in d12:
#         d12[key] = [value]
#     else:
#         d12[key] = value
# print(d12)


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


# L = [1,2,3,2,3,1,1,2,3,2,2,1,3]

# res = {}

# for i in L:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

# max_res = max(zip(res.values()))
# print(max_res)


# from itertools import combinations

# L=[1,2,4,7,5]
# K=6

# sum_pair = []
# for pair in combinations(L, 2):
#     if sum(pair) == K:
#         sum_pair.append(pair)
# print(sum_pair)

# L = [2,2,1,1,1,2,2]
# res = {}

# for i in L:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1

# max_num = max(zip(res.values(), res.keys()))
# print(max_num)

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


# str1 = "manohar how are you"

# vowels = "a,e,i,o,u"
# res = ""
# for i in str1:
#     if i not in vowels:
#         res += i
# print(res)

# string1 = "listen"
# string2 = "silent"

# st1 = string1.replace(" ", "").lower()
# st2 = string2.replace(" ", "").lower()

# if len(st1) != len(st2):
#     print("false")

# if sorted(st1) == sorted(st2):
#     print("correct")
# else:
#     print("wrong")


# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# num = 5
# print(fact(num))

# import re
# abc="gher/2021/ertdwererw/fold1/fold2/fold/3er/2023-07-19/h12:49"

# date_pattern = r'\d{4}-\d{2}-\d{2}'
# time_pattern = r'\d{1,2}:\d{2}'

# res = re.findall(time_pattern,abc)
# res2 = re.findall(date_pattern,abc)
# print(res, res2)


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
