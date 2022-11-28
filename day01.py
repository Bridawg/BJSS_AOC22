# Initialise Array
myValues=[]
counter=0
myVal=None
# Read lines into the array
inputFile='input_day01.txt'
inputFile='input_day01_test.txt'
with open(inputFile) as f:
    for line in f:
        #print(line.strip())
        myValues.append(line.strip())

# Step though array
for x in myValues:
    print(x)
    if myVal is None:
        myVal = x
    elif myVal<x:
        counter = counter + 1
    myVal = x
        
print(str(counter)+" value")