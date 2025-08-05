reports = []

with open("Day-2/input.txt") as input:
    for line in input:
        levelsStr = line.strip().split()
        levelsInt = []
        for level in levelsStr:
            levelsInt.append(int(level))
        reports.append(levelsInt)

'''
First Star Code
'''
safeReports = 0
for report in reports:
    type = ""
    if (report[0] - report[1] > 0):
        type = "descending"
    elif (report[0] - report[1] < 0):
        type = "ascending"
    else:
        # Values are equal, this is a unsafe report continue
        continue
    
    previous = report[0]
    if (type == "ascending"):
        for i in range(1,len(report)):
            if (report[i] - previous > 0 and report[i] - previous <= 3):
                previous = report[i]
            else:
                break
            if (i == len(report) - 1):
                safeReports += 1
    elif (type == "descending"):
        for i in range(1, len(report)):
            if (report[i] - previous < 0 and report[i] - previous >= -3):
                previous = report[i]
            else:
                break
            if (i == len(report) - 1):
                safeReports += 1
    else:
        print("Error, how did you get here?")
print(safeReports)