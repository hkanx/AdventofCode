"""
Date: 12/19/21
Instructions: Calculate the horizontal position and depth you would have 
after following the planned course. What do you get if you multiply your 
final horizontal position by your final depth?

game plan - splice each item, 
use white spaces to make tuples within a list.
each list index that contains tuple index 0(str) of 'forward', call tuple index 1(int)
and add to new x-coord list. sum items of list. 

"""

# open (and close), make list and strip leading and trailing spaces from a string. 
# Ex. ['forward 8', 'forward 3']
with open('day2_input.txt') as f:
    lines = f.readlines()
lines = [val.strip() for val in lines]


"""
#testing
lines = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]
"""

# strip whitespace between each order and int
# make list inside original list, each str called order and each num an int
steps = [step.strip().split(' ') for step 
    in open('day2_input.txt', 'r').readlines()]
steps = [[order, int(num)] for order, num in steps]

# PART 1
# make initial coord (0,0). for each order and num pair in new list, if forward change horizontal or depth by num steps. 
# print coord product
horizontal, depth = 0,0
for order, num in steps:
    if order == 'forward':
        horizontal += num
    elif order == 'down':
        depth += num
    elif order == 'up':
        depth -= num
print('Part 1:', horizontal * depth)

# PART 2
aim, horizontal, depth = 0,0,0
for change, value in steps:
    if change == 'forward':
        horizontal += value
        depth += aim * value
    elif change == 'down':
        aim += value
    else:
        aim -= value
print('Part 2:', horizontal * depth)
