# QUEST 1.   first 4 perfect numebr
# def is_perfect_number(num):
#     divisors_sum = sum(i for i in range(1, num) if num % i == 0)
#     return divisors_sum == num

# def find_perfect_numbers(count):
#     perfect_numbers = []
#     num = 2  # Start checking from 2

#     while len(perfect_numbers) < count:
#         if is_perfect_number(num):
#             perfect_numbers.append(num)
#         num += 1

#     return perfect_numbers

# # Example usage to find the first four perfect numbers
# first_four_perfect_numbers = find_perfect_numbers(4)
# print("First four perfect numbers:", first_four_perfect_numbers)




# QUESTION 1 B INPUT AND CATEGORISE
def is_perfect_number(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Get user input
try:
    user_input = int(input("Enter an integer: "))
    
    if is_perfect_number(user_input):
        print(f"{user_input} is a perfect")
    else:
        print(f"{user_input} is not a perfect")
except ValueError:
    print("Invalid input. Please enter a valid integer.")


# QUEST 1 B 2

# def classify_number(num):
#     divisors_sum = sum(i for i in range(1, num) if num % i == 0)

#     if divisors_sum == num:
#         return "Perfect"
#     elif divisors_sum < num:
#         return "Deficient"
#     else:
#         return "Abundant"

# # Get user input
# try:
#     user_input = int(input("Enter an integer: "))
#     result = classify_number(user_input)
#     print(f"The number {user_input} is a {result} number.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")




# QUESTION 2 check a whole range of number and decide what 
# each number is: abundant, deficient, or perfect. 

# def classify_number(num):
#     divisors_sum = sum(i for i in range(1, num) if num % i == 0)

#     if divisors_sum == num:
#         return "Perfect"
#     elif divisors_sum < num:
#         return "Deficient"
#     else:
#         return "Abundant"

# def classify_numbers_in_range(start, end):
#     classification = {}

#     for num in range(start, end + 1):
#         category = classify_number(num)
#         classification[num] = category

#     return classification

# # Example usage for numbers in the range 1 to 30
# start_range = 1
# end_range = 30

# result = classify_numbers_in_range(start_range, end_range)

# for num, category in result.items():
#     print(f"{num} is a {category} number.")







# QUETS 3 Game enter random number
# import random

# def hi_low_game():
#     # Generate a random number between 0 and 100
#     secret_number = random.randint(0, 100)
    
#     print("Welcome to the Hi-Low Number Guessing Game!")
#     print("Try to guess the hidden number between 0 and 100.")
#     print("Enter a number outside this range to quit.")

#     while True:
#         try:
#             # Get user's guess
#             user_guess = int(input("Enter your guess: "))

#             # Check if the guess is within the valid range
#             if 0 <= user_guess <= 100:
#                 # Provide hints and check if the guess is correct
#                 if user_guess < secret_number:
#                     print("Go higher!")
#                 elif user_guess > secret_number:
#                     print("Go lower!")
#                 else:
#                     print("Congratulations! You guessed the correct number.")
#                     break
#             else:
#                 print("Quitting the game. The correct number was", secret_number)
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")

# # Start the game
# hi_low_game()



# QUESTION 4 Hailstone

# def hailstone_sequence(n):
#     sequence = [n]

#     while n != 1:
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3 * n + 1
#         sequence.append(n)

#     return sequence

# # Example usage
# initial_number = 9
# result_sequence = hailstone_sequence(initial_number)

# print(f"Hailstone sequence for {initial_number}: {result_sequence}")


