# import sys
# import pyperclip
# # pw.py an insecured password locker program

# PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
#              'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
#              'luggage': '12345'}

# if len(sys.argv) < 2:
#     print('Usage: python pw.py [account] - copy account password')
#     sys.exit()

# account = sys.argv[1]  # Get the account name from command line arguments

# if account in PASSWORDS:
#     pyperclip.copy(PASSWORDS[account])  # Copy the password to clipboard
#     print(f'Password for {account} copied to clipboard.')
# else:
#     print(f'No password found for {account}.')
#     sys.exit(1)

# # Adding bullets to Wiki Markups
# # text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author
# # abbreviation\nLists of cultivars'

# text = pyperclip.paste()

# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i] = '* ' + lines[i]

# text = '\n'.join(lines)
# pyperclip.copy(text)  # Copy the modified text to clipboard
# print('-'.join('There can be only one.'.split()))

# # Table Printer
# table_data = [['apples', 'oranges', 'cherries', 'banana'],
#               ['Alice', 'Bob', 'Carol', 'David'],
#               ['dogs', 'cats', 'moose', 'goose']]
# def print_table(table):
#     col_widths = [0] * len(table)  # Initialize column widths

#     # Calculate the maximum width for each column
#     for i in range(len(table)):
#         for item in table[i]:
#             col_widths[i] = max(col_widths[i], len(item))

#     # Print the table row by row
#     for i in range(len(table[0])):
#         row = ''
#         for j in range(len(table)):
#             row += table[j][i].ljust(col_widths[j]) + ' '
#         print(row)
import re


def is_phone_number(text):
    """Check if the input text is a valid phone number."""
    if len(text) != 12:
        return False
    if text[3] != '-' or text[7] != '-':
        return False
    for i in range(12):
        if i in (3, 7):
            continue
        if not text[i].isdigit():
            return False
    return True


is_phone_number('415-555-4242')  # Example usage
print(is_phone_number('415-555-4242'))  # Should return True

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
