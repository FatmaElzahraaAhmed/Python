# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1, 2, 2, 3, 3] returns [1, 2, 3].

def reduce_adjacent_duplicates(lst):
    if not lst:
        return []
    
    reduced_list = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            reduced_list.append(lst[i])
    
    return reduced_list

# Test for Q1
print(reduce_adjacent_duplicates([1, 2, 2, 3, 3]))  # Output: [1, 2, 3]


# 2- Given two strings, divide them into front and back halves
# If the string length is odd, the front half gets the extra character.
# Return a concatenated string of the form: (a-front + b-front) + (a-back + b-back).

def split_string(s):
    length = len(s)
    middle = (length + 1) // 2  # Ensure front gets extra char if odd
    return s[:middle], s[middle:]

def mix_strings(a, b):
    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)
    return a_front + b_front + a_back + b_back

# Test for Q2
print(mix_strings("abcd", "xyz"))  # Output: 'abxcyzd'
print(mix_strings("abcde", "vwxyz"))  # Output: 'abcvwdexyz'


# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.

def all_unique(seq):
    return len(set(seq)) == len(seq)

# Test for Q3
print(all_unique([1, 5, 7, 9]))  # Output: True
print(all_unique([2, 4, 5, 5, 7, 9]))  # Output: False


# 4- Given an unordered list, sort it using bubble sort algorithm.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break  # If no swaps, the list is sorted
    return lst

# Test for Q4
print(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]


# 5- Guessing game
import random

def guessing_game():
    attempts = 10
    guesses = set()
    random_number = random.randint(1, 100)

    print("Welcome to the guessing game!")
    print("You have 10 tries to guess the number (between 1 and 100).")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        
        if guess < 1 or guess > 100:
            print("Invalid input. Please guess a number between 1 and 100.")
            continue
        
        if guess in guesses:
            print("You already guessed that number. Try again.")
            continue
        
        guesses.add(guess)

        if guess == random_number:
            print("Congratulations! You guessed the correct number!")
            play_again = input("Would you like to play again? (y/n): ")
            if play_again.lower() == 'y':
                attempts = 10
                guesses = set()
                random_number = random.randint(1, 100)
                continue
            else:
                print("Thanks for playing!")
                break
        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        attempts -= 1

    if attempts == 0:
        print("Sorry, you've used all your tries. The correct number was:", random_number)
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == 'y':
            guessing_game()
        else:
            print("Thanks for playing!")

# Uncomment to play the guessing game
# guessing_game()
