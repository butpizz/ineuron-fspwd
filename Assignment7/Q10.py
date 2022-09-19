# 10. Write a program to display day name on the basis of user’s liking of a color.
# Ask user for his favorite color. User can answer in a sentence like “I like red color”.
# Assuming all color name entered by user is in lowercase. Use match case to display
# day name associated with the color.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colors - Sunday


day = input('Enter sentence : ')

day = day.lower()

match day:
    case day if 'yellow' in day:
        print('Monday')

    case day if 'blue' in day:
        print('Tuesday')

    case day if 'orange' in day:
        print('Wednesday')

    case day if 'white' in day:
        print('Thursday')

    case day if 'black' in day:
        print('Friday')

    case day if 'red' in day:
        print('Saturday')

    case day if ('red', 'black', 'white', 'orange', 'blue', 'yellow') not in day:
        print('Sunday')
