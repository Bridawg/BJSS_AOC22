# Initialise Array
myValues=[]
score=0
counter=0
myVal=None
# Read lines into the array
inputFile='22_day02_input.txt'
#inputFile='22_day02_input_test.txt'
rock=1
paper=2
scissors=3

with open(inputFile) as f:
    for line in f:
       # print(line.strip())
        myValues.append(line.strip())
#print(len(myValues))

# Step though array
#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors
#The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
for x in myValues:
    myPair = x.split()
   # print(myPair)
    match myPair[0]:
        case 'A': #rock
            match myPair[1]:
                case 'X': # lose
                    score = score+0
                    score = score+scissors
                case 'Y': # draw
                    score = score+3
                    score = score+rock
                case 'Z':  # win
                    score = score+6
                    score = score+paper
        case 'B': #paper
            match myPair[1]:
                case 'X': # lose
                    score = score+0
                    score = score+rock
                case 'Y': # draw
                    score = score+3
                    score = score+paper
                case 'Z': # win
                    score = score+6
                    score = score+scissors
        case 'C': #scissors
            match myPair[1]:
                case 'X': # lose
                    score = score+0
                    score = score+paper
                case 'Y': # draw
                    score = score+3
                    score = score+scissors
                case 'Z': # win
                    score = score+6
                    score = score+rock
    print(score)
        
print(str(score)+" value")
#13645 too high