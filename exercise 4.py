#QUESTION 1
# def symbols():
#     sym=["+-------+","\\\t/","/\t\\","\\\t/","/\t\\","\\\t/","/\t\\","+-------+"]
#     for i in sym:
#         print(i)
# symbols()

# QUESTION 2

# def special_symbols():
#     sym=["***********","***********","***********","***********","***********",]
#     for i in sym:
#         print(i)
# special_symbols()



# QUESTION 3

for num in range(1, 7):
    print(f"{num: <4} | {num * 2: <4} | {num * 15 - 11: <4} | {40 - 10 * num: <4} | {-7 + 4}") 



# for a in range(1, 7):
#     print(a)
 
# for b in range(2, 13, 2):
#     print(b)
 
# for c in range(4, 80, 15):
#     print(c)
 
# for d in range(30, -21, -10):
#     print(d)
 
# for e in range(-1, 13, 4):
#     print(e)
    
# for f in range(97, 83, -3):
#     print(f)
# for g in range(-2, 86, 18):
#     print(g)






# QUESTION 4

# for row in range(0,10):
#     for col in range(0,row+1):
#         print('*',end="") 
#     print()

# for row in range(0,10):
#     for col in range(0,row+1):
#          print('*',end=" ")
#     print()

# for row in range(1,8):
#      for col in range(1,row+1):
#         print(row,end=" ")
#      print()



# QUESTION 5

# def pay(salary, hours_worked):
#     if salary < 0 or hours_worked < 0:
#         return "Invalid input. Salary and hours worked must be non-negative."

#     # Assuming salary is the hourly rate
#     total_payment = salary * hours_worked
#     return total_payment

# # Test the method
# salary_rate = 20.5  # Example hourly rate
# hours_worked = 20   # Example hours worked

# result = pay(salary_rate, hours_worked)
# print(f"The TA should be paid: ${result:.2f}")


# QUESTION 5

# def pay(hourly_rate, hours_worked):
#     if hourly_rate < 0 or hours_worked < 0:
#         return "Invalid input. Hourly rate and hours worked must be non-negative."

#     regular_hours = min(hours_worked, 8)
#     overtime_hours = max(hours_worked - 8, 0)

#     total_payment = (hourly_rate * regular_hours) + (1.5 * hourly_rate * overtime_hours)
#     return total_payment

# # Test the method
# hourly_rate = 4.00
# hours_worked = 10

# result = pay(hourly_rate, hours_worked)
# print(f"The TA should be paid: ${result:.2f}")


# for i in range(1, 7):
#     print(i)

# for row in range(1,8):
#     for col in range(1,row+1):
#         print(row,end=" ")
# print()


#  QUESTION 6

# import math
# def area(r):
#     circle= r*r*math.pi
#     print(circle)
# area(2)
 


# QUEST... 7 EXAMPLE

# low = 1
# high = 1001
# sum = 0
# for i in range(low,high):
#   sum += i
 
# print("sum = " , sum)

#  QUESTION 7

# low_q=int(input("low? "))
# high_q=int(input("high? "))
# low = low_q
# high = high_q
# sum = 0
# for i in range(low,high):
#   sum += i
# print("sum = " , sum)

 
 

# QUESTION 8

# def abc():
#     list1=[]
#     x=int(input('enter numbers\n'))
#     list1.append(x)
#     while x!=0:
#         x=int(input('enter numbers\n'))
#         list1.append(x)
#         if x==0:
#             print(list1)
#             add=sum(list1)#sum is an inbuilt function
#             print('Sum is',add)
#             break
# abc()


# QUESTION 8

# def ab():
#     list1=[]
#     x=int(input('enter numbers\n'))
#     list1.append(x)
#     while x!=0:
#         x=int(input('enter numbers\n'))
#         list1.append(x)
#         if x==0:
#             print(list1)
#             i=0
#             sum=0
#             while i<len(list1):
#                 sum+=list1[i]
#                 i=i+1
#             print('Sum is',sum)
#             break
# ab()



# QUESTION 9

# def abc():
#     list1=[]
#     x=int(input('enter numbers\n'))
#     list1.append(x)
#     while x!=-1:
#         x=int(input('enter numbers\n'))
#         list1.append(x)
#         if x==-1:
#             print(list1)
#             add=sum(list1)#sum is an inbuilt function
#             print('Sum is',add)
#             break
# abc()


# QUESTION9

# def ab():
#     list2=[]
#     x=int(input('enter numbers\n'))
#     list2.append(x)
#     while x!=-1:
#         x=int(input('enter numbers\n'))
#         list2.append(x)
#         if x==-1:
#             print(list2)
#             i=-1
#             sum=0
#             while i<len(list2):
#                 sum+=list2[i]
#                 i=i+1
#             print('Sum is',sum)
#             break
# ab()



# QUESTION 10

# def repl(input_str, repetitions):
#     if repetitions <= 0:
#         return ""
    
#     result_str = input_str * repetitions
#     return result_str

# # Test the method
# input_string = "day"
# repetition_count = 4
# result = repl(input_string, repetition_count)
# print(result)


# QUESTION 11

# def printRange(num1, num2):
#     if num1 < num2:
#         for num in range(num1, num2 + 1):
#             print(num, end=" ")
#     elif num1 > num2:
#         for num in range(num1, num2 - 1, -1):
#             print(num, end=" ")
#     else:
#         print(num1)

# # Sample calls to printRange
# print("Increasing sequence:")
# printRange(1, 10)

# print("\nDecreasing sequence:")
# printRange(11, 5)

# print("\nSingle number:")
# printRange(3, 3)


# QUESTION 12

# def smallestLargest():
#     num_of_numbers = int(input("Enter the number of numbers to read: "))

#     if num_of_numbers <= 0:
#         print("Please enter a valid number greater than 0.")
#         return

#     numbers = []

#     for i in range(num_of_numbers):
#         try:
#             num = float(input(f"Enter number {i + 1}: "))
#             numbers.append(num)
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             return

#     if len(numbers) > 0:
#         smallest = min(numbers)
#         largest = max(numbers)

#         print(f"The smallest number is: {smallest}")
#         print(f"The largest number is: {largest}")
#     else:
#         print("No numbers entered.")

# # Call the method to test
# smallestLargest()


# QUESTION 13

# def printAverage():
#     total = 0
#     count = 0
#     while True:
#         try:
#             num = float(input("Enter a number (negative number to calculate average): "))
#             if num < 0:
#                 break  # Exit the loop if a negative number is entered
#             total += num
#             count += 1
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#     if count > 0:
#         average = total / count
#         print(f"The average of {count} nonnegative numbers is: {average:.2f}")
#     else:
#         print("No nonnegative numbers entered.")
# # Call the method to test
# printAverage()





# Question 14

# def numUnique(num1, num2, num3):
#     unique_numbers = set([num1, num2, num3])
#     return len(unique_numbers)

# # Test the method
# result1 = numUnique(18, 3, 4)
# print(result1)  # Output: 3

# result2 = numUnique(6, 6, 6)
# print(result2)  # Output: 2



# QUESTION 15

# import random

# def roll_dice():
#     return random.randint(1, 6)

# def simulate_dice_rolls():
#     total = 0
#     rolls = 0

#     while total != 7:
#         dice1 = roll_dice()
#         dice2 = roll_dice()
#         total = dice1 + dice2

#         print(f"Roll {rolls + 1}: {dice1} + {dice2} = {total}")

#         rolls += 1

#     print(f"\nIt took {rolls} rolls to get a total of 7.")

# # Simulate dice rolls
# simulate_dice_rolls()





# a_fruits=[x for x in fruits if 'a'in x]
# print(a_fruits)

# list1=[1,4,5,6,7,8,9,0,1,2,4]

# newlist=[i*2 for i in list1]
# print(newlist)

# def divide(x,y):
#     try:
#         ans=x//y
#         print(f'your answer is {ans}')
#     except Exception as e:
#         print(f'the error as {e}')
# print(divide(4,0))


# logic=True
# while logic:
#     que=int(input("enter a number\n"))
#     sum = 0
#     if que !=0:
#       sum+=que
#       que2=int(input("enter a number\n"))
#       sum+=que2
#       if que2 == 0:
#        print(sum)
#        logic = False



