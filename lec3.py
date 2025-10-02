# create funtion
# def hobbies(*list):
#     print(type(list),list)

# hobbies("sleep","eat")

# write a function to return tax to user
# t=int(input("enter ammount"))

# def tax(a):
#     Tax=0
#     if 10000>a:
#         print("zero tax for you")
#     elif 10000<a<50000:
#         Tax=0.02
#     elif 50000<a<100000:
#      print("pay 5% tax")
#      Tax=0.05
#     else:
#        print("pay 10% tax")
#        Tax=0.10
#     return a*Tax
# print(tax(t))

# a=input("enter word")
# def check_palindrome(a):
#    if a==a[::-1]:
#     print("yes it's palindrome")
    
# check_palindrome(a)

# sum of even square number and odd cube number
# def square(no):
#     return(no**2)
# def cube(no):
#     return( no**3)
# def calculate(a):
#  sum=0
#  for item in a:
    
#   if item % 2==0:
#         sum+=square(item)
#   else:
#         sum+=cube(item)
#  return sum
    
# c=calculate([2,3,6,4])
# print(c)

# write funtion that computes the total price of item  in a shopping cart, inculde tax
# . the funtion should take alist of item prices and an optional tax rate.
#  if no tax rate i provided , the funtion should assume a default tax rate of 5%
# def billing(list,tax=0.05):
#     print(f"Total:{sum(list)}")
#     print(f"Tax:{sum(list)*tax}")

#     print( "Total",sum(list)+sum(list)*tax)
# billing([23,45,67])

# take a number and print it's word 

# numbers_dict={
#     '1': "one",
#     '2': "two",
#     '3': "three",
#     '4': "four",
#     '5': "five",
#     '6': "six",
#     '7': "seven",
#     '8': "eight",
#     '9': "nine",
#     '10': "ten"
# }
# def word(a):
#     for i in str(a):
#         print(numbers_dict[i],end=" ")
# word(123)



# 1.tea,2.coffee,3.water,4.bun maska
# create menu and allow user to select
# def menu_display():
#     print("Menu:")
#     print("1. Tea-------------10INR")
#     print("2. Coffee----------40INR")
#     print("3. Water-----------20INR")
#     print("4. Bun Maska------100INR")
#     print("press 0 to exit.")

# def order():
#    o=input("Want to order?Yes or No")
#    if o=="y":
#     menu_display()
#     teas,coffees,water,buns = map(int,(input("Enter teas,coffees,water,bun maskas quantity:").split(",")))
#     print_bill(teas,coffees,water,buns)
   
#    else:
#       print("ok")
#       exit()# Directly exit the program
      



# def print_bill(teas,coffees,water,buns):
#     print("                 Bill            ")
#     print("---------------------------------")
#     print(f"Tea(10)    X  {teas}    {teas*10}")
#     print(f"Coffee(40) X  {coffees}    {coffees*40}")
#     print(f"water(10) X  {water}    {water*10}")
#     print(f"buns(10) X  {buns}    {buns*10}")
#     print(f"Total:{teas*10+coffees*40+water*20+buns*100}")

#     print("press 0 to exit.")
    
# while True:
#     order()
   
# You are given a list of 10 names, and your task is to find and return the longest name in the list.
#  If there are multiple names with the same longest length, return the first one found.
names = ["Alice", "Bob", "Christine", "Daniel", "Eve", "Francis", "George", "Hannah", "Igor", "Jack"]
largest_name = max(names, key=len)
print(largest_name)




 



