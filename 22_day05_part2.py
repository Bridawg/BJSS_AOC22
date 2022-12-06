# Initialise Values
myValues=[]
#myGrid=[]
myHolder=[]

counter=0
counter2 = 0
counter3 = 0
doMap=1
# Datafiles
inputFile='22_day05_input.txt'
#inputFile='22_day05_input_test.txt'

with open(inputFile) as f:
    for line in f:
        myValues.append(line)
        counter += 1

# Step though array
for x in myValues:
    #print(x)
    if len(x)<2:
        doMap=0
        # Generate Map
        myHolder.reverse() 
        print(myHolder)
        myHolder.pop(0)
        Dim1 = len(myHolder)
        Dim2 = int((len(myHolder[0])-3)/4)+1        
        print(str(Dim1)+"x"+str(Dim2))
        myGrid = [[None]*Dim1 for _ in range(Dim2)]
        print(myHolder)
        print(myGrid)
        for y in myHolder:#step through 
            counter=0
            counter2=0
            myLen = len(y)
            while counter < myLen:
                print("incoming")
                print(counter2)
                print(counter3)
                stripe = y[counter:counter+3]
                #print(stripe)
                
                if "[" in stripe:
                    myGrid[counter2][counter3] = stripe[1:2]
                    print(stripe[1:2])
                counter +=4
                counter2 += 1
            counter3 +=1

        
        print(myGrid)
        for x in myGrid:
            while(None in x):
                x.remove(None)
        print(myGrid)

    else:
        if doMap==1: #Hold map
            myHolder.append(x)

        else: # process map instruction
            bob = x.split()
            moveCount = int(bob[1])
            moveFrom = int(bob[3])-1
            moveTo = int(bob[5])-1
            print(bob)
            print(str(moveCount)+" "+str(moveFrom)+" "+str(moveTo))
            myStack=[]
            for z in range(moveCount):
                myStack.append(myGrid[moveFrom].pop())
            myStack.reverse()    
            myGrid[moveTo].extend(myStack)

            print (myGrid)
myString="Answer is: "
for i in myGrid:
    myString += i.pop()
print(myString)