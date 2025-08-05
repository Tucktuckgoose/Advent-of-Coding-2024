import re

def find_all_muls(s):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    results = []
    for match in re.finditer(pattern, s):
        results.append((match.start(), int(match.group(1)), int(match.group(2))))
    return(results)

with open("Day-3/input.txt") as input:
    sum = 0
    for line in input:
        results = find_all_muls(line)
        for result in results:
            sum += result[1]*result[2]
    print(sum)