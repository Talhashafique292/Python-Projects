# def collatz(number):
#     if number % 2 == 0:
#         even = number // 2
#         print(f"The number is even: {even}")
#         return even
#     else:
#         odd = 3 * number + 1
#         print(f"The number is odd: {odd}")
#         return odd


# # collatz(5)


# def run_collatz_sequence():
#     while True:
#         try:
#             user_input = int(input())
#             if user_input <= 0:
#                 print("please enter a positive integer")
#                 continue
#             print(f"Starting collatz sequence: {user_input}")
#             while user_input != 1:
#                 num = collatz(number)
#             break
#         except ValueError:
#             print("Invalid integer please input again")
#         except Exception as e:
#             print(f"unexpected error: {e}")


# run_collatz_sequence()

# spam = ['a', 'b', 'c', 'd']

# print(spam[:2])

# bacon = [3.14, 'cat', 11, 'cat', True]
# print(bacon.index('cat'))
# bacon.append(99)
# bacon.remove('cat')
# print(bacon)

# spam = ['apples', 'bananas', 'tofu', 'cats']
# cars = ["Toyota", "Corola", "BMW"]


# def list_to_string(spam):
#     if not spam:
#         return ""
#     # Sinlge item case
#     if len(spam) == 1:
#         return str(spam[0])
#     # 2 items
#     if len(spam) == 2:
#         return f"{spam[0]} and {spam[1]}"

#     # 3 or more items case, extract all items except last one
#     items_except_last = spam[:-1]
#     last_item = spam[-1]

#     # convert all items into string and join them
#     string_items_except_last = [str(item) for item in items_except_last]
#     string_last_item = str(last_item)

#     # join the item before last one with ", "
#     joined_items = ", ".join(string_items_except_last)
#     return f"{joined_items}, and {string_last_item}"


# # test case 1
# print(f"list: {spam}")
# print(f"list formated to string: {list_to_string(cars)} ")

# # test case 2
# singe_item = [1, 2]
# print(f"single item: {list_to_string(singe_item)}")

# # Character Picture Grid
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]


# def grid_characters(grid):
#     for Y in grid:
#         for X in Y:
#             print(X, end=' ')
#         print()


# grid_characters(grid)

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


# while True:
#     print("Enter a name to get the birthday (or 'exit' to quit):")
#     name = input()
#     if name.lower() == 'exit':
#         break

#     if name in birthdays:
#         print(f"{name}'s birthday is {birthdays[name]}.")
#     else:
#         print(f"I don't have birthday information for {name}.")

# spam = {"color": "red", "age": 42}

# for v in spam.values():
#     print(v)
# for k in spam.keys():
#     print(k)
# for k, v in spam.items():
#     print(f"{k} = {v}")

# The get() method in dictionaries allows you to retrieve a value for a given key,
# and if the key does not exist, it returns a default value instead of raising an error.

# picnicItems = {'apples': 5, 'cups': 2}
# print(f"There are {picnicItems.get('apples', 0)} apples.")  # returns 5

# # returns 0 since 'Mangoes' not there
# print(f"There are {picnicItems.get('Mangoes', 0)} cups.")
# # Without get() method, it would raise a KeyError if 'Mangoes' is not found
# print(f"There are {picnicItems['Mangoes']} cups.")  # This would raise KeyError

# setdefault() method in dictionaries allows you to set a default value for a key if it does not exist.
# spam = {"name": "Zophie", "species": "cat", "age": 7}
# spam.setdefault("color", "gray")
# print(spam)  # {'name': 'Zophie', 'species': 'cat', 'age': 7, 'color': 'gray'}
# spam.setdefault("age", 5)  # This won't change the age since it already exists
# print(spam)  # {'name': 'Zophie', 'species': 'cat', 'age': 7, 'color': 'gray'}

# import pprint
# message = "It was a bright cold day in April, and the clocks were striking thirteen."
# count = {}
# for character in message:
#     # Initialize the character count if not present
#     count.setdefault(character, 0)
#     count[character] += 1  # Increment the count for the character

# # Print the character counts
# print(count)

# pprint("Character counts:")
# message = "It was a bright cold day in April, and the clocks were striking thirteen."
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# pprint.pprint(count)
# # Returns a formatted string representation of the dictionary
# pprint.pformat(count)
# pprint.pprint(count)  # Pretty print the character counts

# Data structure to model real world things
# Tic tac toe game
# empty_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# the_board = {'top-L': 'X', 'top-M': 'O', 'top-R': 'X',
#              'mid-L': 'O', 'mid-M': 'X', 'mid-R': 'O',
#              'low-L': 'X', 'low-M': 'O', 'low-R': 'X'}

# print(the_board)

# Printing the board in a readable format
# def print_board(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# print(print_board(the_board))

# Players can take turns to mark their moves on the board


# def print_board(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# turn = 'X'  # Starting player
# for i in range(9):  # 9 moves in total
#     print_board(empty_board)
#     print(
#         f"Turn for {turn}. Move on which space? (e.g., 'top-L', 'mid-M', etc.)")
#     move = input()

#     empty_board[move] = turn  # Update the board with the player's move
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# print_board(empty_board)

# Nested Dictionaries
# all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
#               'Bob': {'ham sandwiches': 3, 'apples': 2},
#               'Charlie': {'cups': 5, 'cookies': 10}}


# def total_brought(guests, item):
#     num_brought = 0
#     for k, v in guests.items():
#         num_brought += v.get(item, 0)  # Use get to avoid KeyError
#     return num_brought


# print(f"Apples  : {total_brought(all_guests, 'apples')} apples.")
# print(f"Cups    : {total_brought(all_guests, 'cups')} cups.")
# print(f"Cakes   : {total_brought(all_guests, 'cakes')} cakes.")
# print(f"Cookies : {total_brought(all_guests, 'cookies')} cookies.")
# print(
#     f"Ham Sandwiches: {total_brought(all_guests, 'ham sandwiches')} ham sandwiches.")
# print(f"Pretzels: {total_brought(all_guests, 'pretzels')} pretzels.")

# Fantasy Game Inventory

# inventory = {
#     'gold coin': 42,
#     'dagger': 1,
#     'ruby': 3
# }


# def display_inventory(inventory):
#     '''Display the inventory in a readable format.
#     Args:
#         inventory (dict): A dictionary representing the player's inventory.
#     '''
#     print("Inventory:")
#     for item, quantity in inventory.items():
#         print(f"{item}: {quantity}")
#     print(f"Total number of items: {sum(inventory.values())}")


# display_inventory(inventory)

# # List to dictioinary function for fantasy game inventory


# def add_to_inventory(inventory, items):
#     '''Add items to the inventory.
#     Args:
#         inventory (dict): A dictionary representing the player's inventory.
#         items (list): A list of items to add to the inventory.
#     '''
#     for item in items:
#         inventory[item] = inventory.get(item, 0) + 1  # Increment or add item
#     return inventory


# inventory = {
#     'gold coin': 42,
#     'dagger': 1,
#     'ruby': 3
# }

# items_to_add = ['gold coin', 'dagger', 'gold coin', 'ruby', 'ruby', 'ruby']


# def display_inventory(inventory):
#     '''Display the inventory in a readable format.
#     Args:
#         inventory (dict): A dictionary representing the player's inventory.
#     '''
#     print("Inventory:")
#     for item, quantity in inventory.items():
#         print(f"{quantity} {item}")
#     print(f"Total number of items: {sum(inventory.values())}")


# inventory = add_to_inventory(inventory, items_to_add)
# display_inventory(inventory)

# Join() and split() Methods
join_method = ', '.join(['cat', 'dog', 'fish'])
print(join_method)

split_method = 'My Name is Talha'.split()
print(split_method)

split_delimter_method = 'MyABCnameABCisABCSimon'.split('ABC')
print(split_delimter_method)

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))
