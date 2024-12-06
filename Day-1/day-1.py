left = []
right = []
with open("Day-1/input.txt") as input:
    for line in input:
        numbers = line.split()
        left.append(int(numbers[0].strip()))
        right.append(int(numbers[1].strip()))

left.sort()
right.sort()

'''
First star code
delta = 0
for i in range(len(left)):
    delta += abs(left[i] - right[i])

print(delta)
'''

'''
Second star code
'''
total_score = 0
for id in left:
    appearances = 0
    for comparison in right:
        if id == comparison:
            appearances += 1
    total_score += appearances * id

print(total_score)