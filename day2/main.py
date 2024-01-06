import re

with open('input2.txt') as f:
    lines = f.readlines()

red,green,blue = 12,13,14

gamelist = []
powlist = []

for line in lines:

    lowest_red, lowest_green, lowest_blue = 0,0,0

    gameentry = []

    y = line.replace(",",";")
    z = y.replace(":",";").split(";")
    
    for y in z:
        color = re.sub("\d+", "", y).strip()
        number = re.sub('\D', '',y).strip()
        gameentry.append([color, int(number)])

    for x in gameentry:
        if(x[0] == "blue"):
            if( x[1] > blue):
                gameentry[0][1] = 0
            if( x[1] > lowest_blue):
                lowest_blue = x[1]
        elif(x[0] == "red"):
            if( x[1] > red):
                gameentry[0][1] = 0
            if( x[1] > lowest_red):
                lowest_red = x[1]
        elif(x[0] == "green"):
            if( x[1] > green):
                gameentry[0][1] = 0
            if( x[1] > lowest_green):
                lowest_green = x[1]

    gamelist.append(gameentry)
    powlist.append(lowest_red * lowest_green * lowest_blue)

count = 0
for x in gamelist:
    count = count + int(x[0][1])
print(count)

powresult = 0
for x in powlist:
    powresult = powresult + int(x)
print(powresult)
