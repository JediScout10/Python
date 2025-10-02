

# ✅ Question 1: Even or Odd Counter
# Write a program that:

# Takes multiple numbers from the user (space-separated).

# Prints how many are even and how many are odd.
# n=list(map(int, input( " enter number by separting with ").split()))

# def check(n):
#  even_no=0
#  odd_no=0
#  for num in n:
#     if num == 0 :
#      return False
#     elif num % 2==0:
#        print(num,"is even number")
#        even_no+=1
#     else :
#        print(num,"is odd number")
#        odd_no+=1
#  print("\nTotal even numbers:", even_no)
#  print("Total odd numbers:", odd_no)
    
# check(n)

# ✅ Question 2: FizzBuzz Challenge (Classic Interview Q)
# Print numbers from 1 to 50:

# If divisible by 3 → print "Fizz"

# If divisible by 5 → print "Buzz"

# If divisible by both → print "FizzBuzz"

# Otherwise → print the number

# def check(n):
#  if n%3==0:
#     print("Fizz")
#  elif n%5==0:
#     print('BUZZ')
#  elif n%3==0 and n%5==0:
#     print("FizzBuzz")
#  else:
#     print(n)

# for num in range(1,51):
#    check(num)

# ✅ Question 3: Factorial Finder
# Ask the user for a number and print its factorial.

# n=int(input('Enter number to find factorial'))
# def check(n):
#     if n<0:
#      print("wrong number")
#     else:
#        m=1
#        for i in range(1,n+1):
#           m=m*i
#     print(m)
       
# check(n)

# ✅ Question 4: Find Largest Number in a List
# Ask the user to enter numbers, and find out which number is the largest.

# n=list(map(int, input("enter numbers to find which one is greater:").split()))
# print("gretest number:",max(n))
# print("smallest number:", min(n))

# ✅ Question 5:Count Vowels in a String
# Input a string from the user and count how many vowels it has.

# n=input("enter a string")
# v="aeiouAEIOU"
# count=0
# for i in n:
#     if i in v:
#         count+=1
# print("number of vowels in string",count)

# ✅ Question 6:Find All Prime Numbers from 1 to N
# Ask the user for a number N and print all prime numbers from 1 to N.

# n=int(input("enter number:"))

# for i in range(2,n+1):
#     for f in range(2,i):
#         if i%f==0:
#            break

#     else:
#         print(i,"is a prime no")

# ✅ Question 7: Sum of Digits
# Ask the user to enter a number, and then calculate the sum of its digits.

# n=(input("enter number:"))
# total=0
# for i in n:
#     total+=int(i)
# print(total)

# ✅ Question 8: Palindrome Number
# Ask the user to enter a number.
# Check if the number is a palindrome

# n=int(input("enter number:"))
# original = n
# reverse = 0
# while n>0:
#     digit = n%10
#     reverse = reverse * 10 + digit 
#     n = n // 10
# if reverse==original :
#         print(original,"is a palindrome")
# else:
#         print(original ,"is not a palindrome")

# ✅ Question 9: Count the Digits of a Number
# Ask the user to enter a number.
# Your program should count how many digits the number has.

# n=int(input("enter number:"))
# count=0
# while n>0:
#  n = n // 10     
#  count += 1 

# print(count)


# ✅ Question 10: Count Digits, Letters, and Special Characters in a String
# 📝 Task:
# Ask the user to enter any string.
# Your program should count and print:
# Total number of digits
# Total number of letters
# Total number of special characters (anything that is not a digit or letter)
# text = input("Enter a string: ")

# letters = 0
# digits = 0
# special = 0

# for char in text:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         special += 1

# print("Letters:", letters)
# print("Digits:", digits)
# print("Special Characters:", special)

# ✅ Question 11 : Count the Frequency of Each Character in a String
# 📝 Task:
# Ask the user to enter a string.
# Your program should print how many times each character appears in the string.
 
# n=input("enter a string:")
# dict={}

# for i in n:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1

# for i,f in dict.items():
#     print(f"{i}:{f}")

# ✅ Question 12: Count Words in a Sentence
# 📝 Task:
# Ask the user to enter a full sentence.
# Your program should count how many words are in that sentence.

# n=input("enter a sentence :").split()
# count=0
# for i in n:
#     count+=1
# print(f"total world:{count}")

# ✅ Question 13: Reverse Each Word in a Sentence
# 📝 Task:
# Ask the user to enter a full sentence.
# Your program should reverse each word, but keep the word order the same.

# n=input("enter a sentence :").split()

# for i in n:
#     print(i[::-1])


# ✅ Question 14: Find the Largest Word in a Sentence
# 📝 Task:
# Ask the user to enter a sentence.
# Your program should find and print the longest word in that sentence and its length.

# n=input("enter a sentence :").split()
# longest_word = ""
# max_length = 0
# for i in n:
#    print(f"{i}:{len(i)}")
#    if len(i)>max_length :
#       max_length=len(i)
#       longest_word=i
# print("The longest word is:",longest_word)
# print("longest length:",max_length)

# ✅ Question 15: Count Digits in a Number
# 📝 Task:
# Ask the user to enter a positive integer number.
# Your program should count how many digits the number has.

# n=(input("enter your number:"))
# count=0
# for i in n:
#     count+=1
# print(f"The number has {count} digits.")

# ✅ Question 16: Find Numbers Divisible by Both 3 and 5
# 📝 Task:
# Ask the user for a number N.
# Print all numbers from 1 to N that are divisible by both 3 and 5.

# n=int(input("enter number:"))

# for i in range(1,n+1):
#     if i%3==0:
#      print(i,"is divisible by 3")
#     elif i%5==0:
#         print(i,"is divisible by 5")
#     else:
#        print(i,"is not divisible by both 3 and 5.")

# ✅ Question 17: Find the Second Largest Number
# 📝 Task:
# Ask the user to input a list of numbers.
# Find and print the second largest number (not using sort()).

# n=list(map(int,input("enter multiple number separting by space:").split()))
# largest=0 
# sec_largest=0
# for i in n:
#     if i>largest:
#          largest=i
#          for i in n:
#           if i<sec_largest<largest:
#            sec_largest=i
# print("second largest number:",(sec_largest))
       
# ✅ Question 18: Remove Duplicates from List
# 📝 Task:
# Ask the user to enter a list of numbers.
# Your program should:
# without set
# Remove duplicates

# Print the new list with unique numbers only
    
# n = list(map(int, input("Enter numbers separated by space: ").split()))

# unique = []
# for i in n:
#     if i not in unique:
#         unique.append(i)

# print("List with duplicates removed (order preserved):", unique)

# ✅ Question 19: Print a Right-Angled Triangle Pattern
# 📝 Task:
# Ask the user for a number N (rows).
# Print a triangle like this:

# n=int(input('ENTER NUMBER:'))

# for i in range(1, n + 1):
#     print("*" * i)

# ✅ Question 20: Check Armstrong Number
# 📝 Task:
# Ask the user for a number.
# Check if it's an Armstrong number (e.g., 153 → 1³ + 5³ + 3³ = 153)

# n=int(input('ENTER NUMBER:'))
# f=n
# str(n)
# a=len(str(n))
# def power(n):
#     total=0
#     for i in str(n):
#       total+=int(i) ** a
#     print(total)
#     if total==f:
#        print(f,"It’s an Armstrong number")
#     else:
#        print(f," Not an Armstrong number")

# power(n)
 
# ✅ Question 21: Count Positive, Negative, and Zero Numbers
# 📝 Task:
# Ask the user to enter a list of numbers (space-separated).
# Your program should:
# Count how many numbers are positive
# How many are negative
# How many are zero

# n=int(input('ENTER NUMBER:'))
# positive=0
# negative=0
# zero=0

# for i in str(n):
#     if int(i)>0:
#      positive+=1
#     elif int(i)<0:
#        negative+=1
#     elif int(i)==0:
#        zero+=1

# print(positive,"numbers are positive")
# print(negative,"numbers are negative")
# print(zero,"numbers are zero")

# ✅ Question 22: Find Numbers Greater Than the Average
# 📝 Task:
# Ask the user to enter a list of numbers (space-separated).
# Your program should:
# Calculate the average of the numbers.
# Print all numbers that are greater than the average.

# n=list(map(int,input("enter a list of numbers:").split()))
# f=sum(n)/len(n)
# print("Avarage:",f)
# print("Numbers that are greater than the average")
# for i in n:
#     if i>f:
#         print(i)
 
# ✅ Question 23: Print a Pyramid Pattern

# 📝 Task:
# Ask the user for a number N (number of rows).
    
# n=int(input('ENTER NUMBER:'))

# for i in range(0,n):
#     print(" "*(n-1-i),"*"*(2*i+1))

# ✅ Question 25: Print an Inverted Right-Angled Triangle

# 📝 Task:
# Ask the user to enter a number n (number of rows).
# Print an inverted right-angled triangle pattern made of stars *.

# n=int(input('ENTER NUMBER:'))

# for i in range(0,n+1):
#     print("*"*(n-i))

# ✅ Question 26: Count Even and Odd Digits in a Number

# 📝 Task:
# Ask the user to enter a number (positive integer).
# Your program should:
# Count how many even digits and odd digits are in that number.
# Then, print both counts.

# n=int(input('ENTER NUMBER:'))
# even=0
# odd=0
# for i in str(n):
#     if int(i)%2==0:
#         even+=1
#     elif int(i)==0:
#         even+=1
#     else:
#         odd+=1
# print("Even digits:",even)
# print("Odd digits:",odd)

# ✅ Question 27: Find the First Repeating Character in a String

# 📝 Task:
# Ask the user to enter a string.
# Your program should find the first character that repeats in the string and print it.
# If no character repeats, print a message saying so.

# n=input("enter a string:")
# f=set()
# for i in n:
#   if i in f:
#     print("First repeating character:", i)
#     break
#   else:
#     f.add(i)
# else:
#    print("No repeating characters found.")

# ✅ Question 29:Count Frequency of Each Word in a Sentence
# 📝 Task:
# Ask the user to enter a full sentence.
# Your program should count how many times each word appears.

# n=input("enter a string:").split()
# dict={}
# for i in n:
#         if i in dict:
#          dict[i]+=1
#         else:
#           dict[i]=1

# for i,f in dict.items():
#    print(f"{i}:{f}")
        
# ✅ Question 30: Replace Specific Word in a Sentence

# 📝 Task:
# Ask the user to enter a sentence, a word they want to replace, and the new word.
# Then print the updated sentenc

# n=input("enter a string:")
# old_word = input("Word to replace: ")
# new_word = input("New word: ")
# new_sentence = n.replace(old_word, new_word)
# print("Updated sentence:", new_sentence)

# ✅ Question 31: Count Uppercase and Lowercase Letters in a String

# 📝 Task:
# Ask the user to enter a string.
# Your program should:
# Count how many uppercase letters are in the string.
# Count how many lowercase letters are in the string.
# Print both counts.

# n=input("enter a string:")
# upper=0
# lower=0
# for i in n:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)

# ✅ Question 32: Find the Sum of All Even Numbers in a List

# 📝 Task:
# Ask the user to enter a list of numbers (space-separated).
# Your program should:
# Find only the even numbers.
# Add them together.
# Print the sum of all even numbers.

# n = list(map(int, input("Enter numbers (space-separated): ").split()))
# sum=0
# for i in n:
#     if i%2==0:
#       sum+=i
#     else :
#        False
# print("Sum of even numbers:", sum)

# ✅ Question 33: Find the Difference Between Max and Min in a List
# Task:
# Ask the user to enter a list of numbers (space-separated).
# Your program should find the difference between the largest and smallest number in the list.

# n=list(map(int,input("enter number separated by space:").split()))
# f=n.sort()
# g=len(n)
# a=n[g-1]-n[0]
# print(a)

# n = list(map(int, input("Enter numbers separated by space: ").split()))

# max_num = max(n)
# min_num = min(n)
# diff = max_num - min_num

# print(f"Difference = {max_num} - {min_num} = {diff}")

# ✅ Question 34: Find All Duplicates in a List
# 📝 Ask the user for a list of numbers (space-separated).
# Print all elements that appear more than once, but only once in the result.

# n = list(map(int, input("Enter numbers separated by space: ").split()))
# dict={}
# for i in n:
#     if i in dict:
#         dict[i]+=1
#     else :
#        dict[i]=1

# print("Duplicates:")
# for key, value in dict.items():
#     if value > 1:
#         print(f"{key}: {value}")

# ✅ Question 35: Check Anagram Strings
# 📝 Ask the user for two strings.
# Check if they are anagrams (contain same characters, just rearranged).

# n = input("Enter first string: ").replace(" ", "").lower()
# n1 = input("Enter second string: ").replace(" ", "").lower()

# if sorted(n) == sorted(n1):
#     print("Anagram ✅")
# else:
#     print("Not an Anagram ❌")


# ✅ Question 36: Sort Words in a Sentence
# 📝 Ask the user for a sentence.
# Print the words in alphabetical order (case-insensitive).
# key=str.lower parameter to sort alphabetically without case sensitivity.


# n=list(input("enter a snetence:").split())
# print(sorted(n,key=str.lower))

# ✅ Question 37: Capitalize First Letter of Each Word
# 📝 Input a sentence.
# Capitalize the first letter of each word.

# n=input("enter a string:")
# print(n.title())

# To capitalize all words in a string in Python, you can use the title()


   

