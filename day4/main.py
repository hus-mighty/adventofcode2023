import time
start_time = time.time()

#Part 1
cardlist = []

with open('input.txt') as f:
    for line in f.readlines():

        entrylist, winninglist, points = [], [], 1

        linenew = list(filter(None, line.split(" ")))
        cardline = [int(linenew[1].strip(":")), entrylist, winninglist, points]

        for x in range(2, len(linenew)):
            if(x >= 2 and x < linenew.index("|")):
                entrylist.append(int(linenew[x]))
            if(x > linenew.index("|") and x <= len(linenew)):
                winninglist.append(int(linenew[x]))
       
        cardline.append(len(list(set(cardline[1]).intersection(set(cardline[2])))))
        
        if(cardline[4] > 2):
            for x in range(cardline[4]-1):
                cardline[3] = cardline[3] * 2
        else:
            cardline[3] = cardline[4]
        cardlist.append(cardline)

count = 0
for y, x in enumerate(cardlist):
    count+=x[3]

#Part 2
for x in cardlist:
    for x in range(x[0],x[0]+x[4]):
        cardlist.append(cardlist[x])

print(f'Part 1: {count}\nPart 2: {len(cardlist)}')

print("Process finished --- %s seconds ---" % (time.time() - start_time))
