# Initialise Values
myValues=[]
myGrid=[]
myHolder=[]

counter=0
doMap=1
# Datafiles
inputFile='22_day05_input.txt'
inputFile='22_day05_input_test.txt'

with open(inputFile) as f:
    for line in f:
        myValues.append(line)
        counter += 1
print("A")
print(counter)
counter=0

# Step though array
for x in myValues:
    #print(x)
    if len(x)<2:
        doMap=0
        #Generate Map
        myHolder = myHolder.reverse() 
        print(myHolder)
       # temp = int((len(myHolder[0])-3)/4)+1
        for y in myHolder:
            print(temp)
        # temp = int((len(x)-3)/4)+1
        
        # print(temp)
        # while y<=temp:
        #     bob=x[0:3].strip("[]")
        # bob=x[0:3].strip("[]")
        # print(bob)

        # bob=(x[4:7].strip("[]")
        # print(bob)

        # bob=x[8:10].strip("[]")
        # print(bob)
    else:
        if doMap==1: #Hold map
            myHolder.append(x)
            #print(x)

        else: # process map instruction
            bob = x.split()
            moveCount = bob[1]
            moveFrom = bob[3]
            moveTo = bob[5]
            print(bob)
            print(str(moveCount)+" "+str(moveFrom)+" "+str(moveTo))

#print("break")

#     myPair = x.split(",")
#     #print (myPair)
#     elfOneRange = myPair[0].split("-")
#     elfTwoRange = myPair[1].split("-")
#     print(elfOneRange)
#     print(elfTwoRange)
#     elfOneRange[0] = int(elfOneRange[0])
#     elfOneRange[1] = int(elfOneRange[1])
#     elfTwoRange[0] = int(elfTwoRange[0])
#     elfTwoRange[1] = int(elfTwoRange[1])
#     if elfOneRange[0] == elfTwoRange[0] or elfOneRange[1] == elfTwoRange[1]:
#         counter = counter + 1
#         print("overlap detected")
#     elif elfOneRange[0] < elfTwoRange[0]:
#         if elfOneRange[1]> elfTwoRange[1]:
#             counter = counter + 1
#             print("overlap detected")
#     elif elfOneRange[0] > elfTwoRange[0]:
#          if elfOneRange[1]< elfTwoRange[1]:
#             counter = counter + 1
#             print("overlap detected")
# print(counter)