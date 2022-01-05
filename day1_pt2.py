"""
Date: 12/18/21
Instructions: Count the number of times the sum of measurements in this 
three-number sliding window increases from the previous sum.
(There is no measurement before the first measurement.)
"""

# open and make each item an integer
f = open("day1_input.txt", "r")
#text = f.readlines()
test_list = list(map(int, f))

#Soln 2:
output = []
sliding_output = []

for i in range(0, (len(test_list)) - 2):
    sliding_output.append(test_list[i] + test_list[i+1] + test_list[i+2])

for i in range(1, len(sliding_output)):
    output.append(sliding_output[i - 1] < sliding_output[i])

print(sum(output))
