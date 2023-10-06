import random

# Task 1: Fill an array with 10 random integers between 1 and 100.
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Random Numbers:", random_numbers)

# Task 2: Find the largest number in the array.
max_number = max(random_numbers)
print("Largest Number:", max_number)

# Task 3: Check if a number is smaller than 10 and print the result.
user_input = int(input("Enter a number: "))
if user_input < 10:
    print(f"{user_input} is smaller than 10.")

# Task 4: Separate even and odd numbers from the array.
even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# Task 5: Create a custom array and count its elements.
custom_array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]  # Modify with your elements
element_to_count = int(input("Enter an element to count: "))
count = custom_array.count(element_to_count)
print(f"{element_to_count} appears {count} times in the custom array.")

# Task 6: Count numbers greater than 30 in the random_numbers array.
count_greater_than_30 = len([num for num in random_numbers if num > 30])
print("Numbers greater than 30:", count_greater_than_30)

#-------------------------------------------------------------------------------------

import random

# Task 1: Fill an array with 10 random integers between 1 and 100.
array = [random.randint(1, 100) for _ in range(10)]

# Task 2: Find and print the maximum number in the array.
max_num = max(array)
print("The maximum number in the array is:", max_num)

# Task 3: Check if a number is smaller than 10.
number = int(input("Enter a number: "))
if number < 10:
    print("The number is smaller than 10.")
else:
    print("The number is not smaller than 10.")

# Task 4: Separate even and odd numbers in the array.
even_numbers = [num for num in array if num % 2 == 0]
odd_numbers = [num for num in array if num % 2 != 0]
print("Even numbers in the array:", even_numbers)
print("Odd numbers in the array:", odd_numbers)

# Task 5: Create a custom array and count the number of elements.
custom_array = [5, 10, 15, 20, 25, 30]
element_to_count = int(input("Enter an element to count: "))
count = custom_array.count(element_to_count)
print(f"The element {element_to_count} appears {count} times in the custom array.")

# Task 6: Count the elements in the array that are greater than 30.
count_greater_than_30 = sum(1 for num in array if num > 30)
print("Number of elements greater than 30 in the array:", count_greater_than_30)

#--------------------------------------------------------------------------------------

import random

# 1. Töltsön fel 10 véletlen (1-100 között) egész számmal egy tömböt.
random_numbers = [random.randint(1, 100) for _ in range(10)]

# 2. Írassa ki/válogassa szét a tömbben szereplő számok közül a legnagyobb számot.
max_number = max(random_numbers)
print(f'A tömb legnagyobb száma: {max_number}')

# 3. Kérjen be egy számot és döntse el, kisebb-e 10-nél. Írassa ki a megoldást!
user_input = int(input('Kérem, adjon meg egy számot: '))
if user_input < 10:
    print('A megadott szám kisebb, mint 10.')
else:
    print('A megadott szám nem kisebb, mint 10.')

# 4. Írassa ki/válogassa szét a tömbben szereplő számok közül a páros és páratlan számokat.
even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]
print(f'Páros számok: {even_numbers}')
print(f'Páratlan számok: {odd_numbers}')

# 5. Hozz létre egy saját tömböt választott mennyiségű elemmel. Írj egy programot, ami megszámolja, hány darab elem szerepel ebben a tömbben.
custom_array = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
element_to_count = int(input('Kérem, adjon meg egy számot, hogy megszámoljuk, hány darab van belőle a tömbben: '))
count = custom_array.count(element_to_count)
print(f'A(z) {element_to_count} szám {count} darab szerepel a tömbben.')

# 6. Hány 30-nál nagyobb elem van a tömbben.
count_gt_30 = sum(1 for num in custom_array if num > 30)
print(f'{count_gt_30} darab elem nagyobb, mint 30 a tömbben.')

#----------------------------------------------------------------------------------------------------------------------------------------------