def wins(time, distance):
    return sum((not(miliseconds == 0 or miliseconds == time) and miliseconds * (time - miliseconds) > distance for miliseconds in range(time+1)))

with open ("input.txt") as f:
    line = f.readlines()
    time, destination = list(map(int,(filter(None, line[0][line[0].index(":")+1:].split(" "))))), list(map(int,(filter(None, line[1][line[1].index(":")+1:].split(" ")))))
    timelong, destinationlong, result = int("".join([str(x) for x in time])), int("".join([str(x) for x in destination])), 1

    for x in range(len(time)):
        result *= wins(time[x],destination[x])

    print(f"Part 1: {result}\nPart 2: {wins(timelong,destinationlong)}")
