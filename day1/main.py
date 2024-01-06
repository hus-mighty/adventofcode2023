import operator

digit = ("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9), ("zero", 0)
calibrationvalues = []
    
with open('input.txt') as f:
    lines = f.readlines()

def sumlist(list):
    count = 0
    for x in list:
        count = count + x
    print(count)
    return count

for line in lines:
    numberlist1 = []
    numberlist2 = []
    
    for x in range(len(line)):
        for num in digit:
            if(num[0] in line):
                pos = line.find(num[0]) + x
                name = num[0]
                number = num[1]
                numberlist1.append((name, number, pos))
            
            if(str(num[1]) in line):
                pos = line.find(str(num[1])) + x
                name = num[0]
                number = num[1]
                numberlist1.append((name, number, pos))
            
        line = line[1:]

    numberlist1 = list(dict.fromkeys(numberlist1))

    for x in range(len(numberlist1)):
        numberlist2.append(min(numberlist1, key=operator.itemgetter(2)))
        numberlist1.remove(min(numberlist1, key=operator.itemgetter(2)))

    numberlist1.clear

    numberlist1.append(min(numberlist2, key=operator.itemgetter(2)))
    numberlist1.append(max(numberlist2, key=operator.itemgetter(2)))
    
    for num in numberlist1:
        line = line + str(num[1])
    calibrationvalues.append(int(line))

sumlist(calibrationvalues)



