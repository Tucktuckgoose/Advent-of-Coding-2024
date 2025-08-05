import re

def find_all_muls(s): # Accepts the string with the input data
    # Returns a list of mul(Xxx, Yyy) patterns of the form [location, Xxx, Yyy]
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    results = []
    for match in re.finditer(pattern, s):
        results.append((match.start(), int(match.group(1)), int(match.group(2))))
    return(results)

def find_all_dosanddonts(s): # Accepts the string with the input data
    # Returns a list of locations of do and don'ts of the form [location, bool]
    pattern = r"do\(\)|don't\(\)"
    results = []
    for match in re.finditer(pattern, s):
        results.append((match.start(), match.group() == "do()"))
    return(results)

def find_do_sections(li,bo, line_len): # Accept the list of do_results, the current do boolean statement, and the length of the line
    # Returns a list of do and don't sections of the form [start, stop, do or don't]
    sections = []
    state = bo
    last = 0
    for item in li:
        if item[1] != state:
            sections.append((last, item[0], state))
            state = (not state)
            last = item[0]
    sections.append((last, line_len, state))
    return(sections)
        

with open("Day-3/input.txt") as input:
    sum = 0
    do = True
    for line in input:
        mul_results = find_all_muls(line)
        do_results = find_all_dosanddonts(line)
        sections = find_do_sections(do_results, do, len(line))
        for result in mul_results:
            for section in sections:
                if (result[0] >= section[0] and result[0] <= section[1] and section[2]):
                    sum += result[1]*result[2]
                    break
        do = sections[-1][2]
    print(sum)