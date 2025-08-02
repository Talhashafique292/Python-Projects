"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
4. View this code at https://nostarch.com/big-book-small-python-projects
5. Tags: short, math, simulation """

import datetime, random  # Step 1 import

# Step 2 get number of Random birthdays 
def getBirthdays(numberOfBrithdays):
    """Returns a list of random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBrithdays):
        # The year is unimportant for our simulation, as long as all
        # Birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get random day into year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364)) 
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

# Step 3 get Matching birthdays from random birthdays
def getMatch(birthdays):
    '''Return the date object of a birthday that occurs more than onece
    in the birthdays lis.'''
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique

    # Compare each birthday to every birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday


#Display the intro
print('''Birthday Paradox, by Al Sweigeart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This programe does a Monto Carlo simulation (that is, repeated random
Simulations) to explore this concept.

(Its not actually a paradox, its just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while True:  # Keep asking untill user enters a valid amount.
    print('''How many birthdays shall I generate? (Max 100) ''')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid ammount
print()

# Generate and display birthdays
print("Here are", numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i !=0:
        # Display a comma for each birthday after after the first birthday.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end = "")
if match != None:
    montName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to beging...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birhtdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, "people have a", probability, '%'' chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think')











