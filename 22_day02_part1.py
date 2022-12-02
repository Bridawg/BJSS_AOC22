# Initialise Array
myValues=[]
score=0
counter=0
myVal=None
# Read lines into the array
inputFile='22_day02_input.txt'
#inputFile='22_day02_input_test.txt'

with open(inputFile) as f:
    for line in f:
       # print(line.strip())
        myValues.append(line.strip())
print(len(myValues))

# Step though array
#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors
#The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

for x in myValues:
    myPair = x.split()
   # print(myPair)
    match myPair[0]:
        case 'A':
            match myPair[1]:
                case 'X':
                    score = score+1
                    score = score+3
                case 'Y':
                    score = score+2
                    score = score+6
                case 'Z':
                    score = score+3
                    score = score+0
        case 'B':
            match myPair[1]:
                case 'X':
                    score = score+1
                    score = score+0
                case 'Y':
                    score = score+2
                    score = score+3
                case 'Z':
                    score = score+3
                    score = score+6

        case 'C':
            match myPair[1]:
                case 'X':
                    score = score+1
                    score = score+6
                case 'Y':
                    score = score+2
                    score = score+0
                case 'Z':
                    score = score+3
                    score = score+3
    #if x == '':
    #    elfCalories.append(counter)
    #    counter=0
    #else:
    #    counter=counter+int(x)


        
print(str(score)+" value")