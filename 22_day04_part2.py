# Initialise Values
myValues=[]
counter=0

# Datafiles
inputFile='22_day04_input.txt'
#inputFile='22_day04_input_test.txt'

with open(inputFile) as f:
    for line in f:
        myValues.append(line.strip())

# Step though array
for x in myValues:
   # print(x)
    myPair = x.split(",")
    #print (myPair)
    elfOneRange = myPair[0].split("-")
    elfTwoRange = myPair[1].split("-")
    print(elfOneRange)
    print(elfTwoRange)
    elfOneRange[0] = int(elfOneRange[0])
    elfOneRange[1] = int(elfOneRange[1])
    elfTwoRange[0] = int(elfTwoRange[0])
    elfTwoRange[1] = int(elfTwoRange[1])

    if elfOneRange[0] <= elfTwoRange[0]:
         if elfOneRange[1]>= elfTwoRange[0]:
             counter = counter + 1
             print("overlap detected")
    else:
         if elfTwoRange[1] >= elfOneRange[0]:
             counter = counter + 1
             print("overlap detected")
print(counter)