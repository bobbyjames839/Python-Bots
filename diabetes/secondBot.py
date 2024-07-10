level_str = input('Please provide your glucose level here: ')

# Initialize the level variable
level = None

try:
    level = float(level_str)
except ValueError:
    print('Please insert a valid number.')


extra_injections = (level - 7) / 3

if level is not None:
    if level > 40 or level < 0:
        print('Invalid blood glucose level')
    elif level > 7:
        print(f'Your blood glucose level is too high, you should inject {extra_injections:.1f} units to bring them down.')
    elif level < 4:
        print('Your blood glucose levels are low, please eat some sugar.')
    else:
        print('Congrats, your blood glucose levels are looking good.')

#improve this bot here 


