"""
Date: 12/18/21
Instructions: Count the number of times a depth measurement 
increases from the previous measurement. 
(There is no measurement before the first measurement.)
"""

# open and make each item in list an integer
f = open("day1_input.txt", "r")
#text = f.readlines()
test_list = list(map(int, f))

print(test_list)

# Soln 1:
#print(sum([test_list[i - 1] < test_list[i] for i in range(1, len(test_list))]))

#Soln 2:
output = []
for i in range(1, len(test_list)):
    output.append(test_list[i - 1] < test_list[i])

print(sum(output))
    