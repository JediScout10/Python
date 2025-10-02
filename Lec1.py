#take input
# name=input("who are you ")
# native=input("where are you from")
# print(f"hi{name},so you are from{native}")

# #type2 to print
# def intro(name,native):
#     print(f"hi{name},so you are from{native}")

#funtion to check age
#name=input("who are you ")
# native=input("where are you from")
# age=int(input("your age?"))

# def intro2( name,native,age):
#     if 0>age:
#         print("wrong age")

#     elif 18<age > 58:
#         print("Sleep well")
#     elif 18 < age <= 58:
#         print("go work")
#     else:
#         print("Go play")
   

# intro2(name,native,age )

#funtion to calulate no of vowels
# def vowel(name):
#     count=0
#     v="aeiouAEIOU"
#     for char in v:
#         count=count+name.count(char)
#     print("no of vowels",count)

# vowel(name)

#funtion to check palindrome
# string=input("enter word")

# def check_palindrome(string):
#    if string ==string[::-1]:
#       print("yes it palindrome")
#    else:
#       print("not palindrome")
       
# check_palindrome(string)

#funtion to calculate percentage
# def cal_percentage(obtained_marks,total_marks):
#     return (obtained_marks/total_marks)*100


# obtained_marks,total_marks=map(int,input("enterd your marks and total marks").split())
# print(f"your marks:{obtained_marks} from {total_marks}")
   
# print(f"your percantage: {cal_percentage(obtained_marks,total_marks)}")    

#for loop
# for i in range(1,11,2):
#     print(i)
#     #8369363552 vinay raikar

# for i in range(6,0,-1):
#     print("X"*i)


# for i in range(1,7,+1):
#     print(" "*(6-i),"X"*i)

#  x-tree  
# for i in range(1,7,+1):
#     print(" "*(6-i),"X "*i)

#take line from user
# n=int(input("give no line you need to print"))
# for i in range(1,n,+1):
#     print("X"*i)

#alternate x,o tree
# n = int(input("Enter the number of lines you need to print: "))
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(" " * (n - i) + " O" * i)
#     else:
#         print(" " * (n - i) + " X" * i)

#print n number in one line
# n=int(input("enter n:"))
# def number(n): 
#   for i in range(1,n+1):
#    print(i,end=',')

#   number(n)

# while True:
    # i=int(input("say:"))
   
    # if i<0:
    #     print("bye")
    #     break
    # print("chal BATA")

#add all number
# total=0
# while True:
#     i=int(input("enter number:"))     
#     if i==0:
#      print("total",i)
#      break
#     total += i
       
#guess price
# cost=float(input("enter cost:"))
# count=0
# while True:
#  guessed_cost=float(input("guess:"))
#  count+=1
#  if cost==guessed_cost:
#   print("right")
#   break
#  elif cost>guessed_cost:
#   print("guess more price:") 
#  else :
#   print("guess less :")

  
# print("numbr of guess:",count)






