def wins(time, distance):
    wins = 0
    for miliseconds in range(time+1):
        i = miliseconds * (time - miliseconds)
        if(i > distance and not(miliseconds == 0 or miliseconds == time)):
            wins += 1
    return wins

with open ("input.txt") as f:
    line = f.readlines()

    time = list(map(int,(filter(None, line[0][line[0].index(":")+1:].split(" ")))))
    destination = list(map(int,(filter(None, line[1][line[1].index(":")+1:].split(" ")))))

    timelong = int("".join([str(x) for x in time]))
    destinationlong = int("".join([str(x) for x in destination]))
    result = 1

    for x in range(len(time)):
        result *= wins(time[x],destination[x])

    print(f"Part 1: {result}\nPart 2: {wins(timelong,destinationlong)}")
