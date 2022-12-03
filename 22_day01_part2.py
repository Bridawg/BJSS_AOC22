# Initialise Array
myValues=[]
elfCalories=[]
counter=0
myVal=None
# Read lines into the array
inputFile='22_day01_input.txt'
#inputFile='22_day01_input_test.txt'

with open(inputFile) as f:
    for line in f:
       # print(line.strip())
        myValues.append(line.strip())
#print(len(myValues))

# Step though array
for x in myValues:
    #print(x)
    if x == '':
        elfCalories.append(counter)
        counter=0
    else:
        counter=counter+int(x)

if counter>0:
    elfCalories.append(counter)

bigVal = max(elfCalories)
elfCalories.sort()
limit = len(elfCalories)
total = elfCalories[limit-1]+elfCalories[limit-2]+elfCalories[limit-3]
print (total)