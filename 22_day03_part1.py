# Initialise Values
myValues=[]
score=0
counter=0
myVal=None
valueList=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Datafiles
inputFile='22_day03_input.txt'
#inputFile='22_day03_input_test.txt'

with open(inputFile) as f:
    for line in f:
        myValues.append(line.strip())

# Step though array
for x in myValues:
   # print(x)
    half = int((len(x))/2)
    print(half)
    left = x[:half]
    leftSet = set(left)
    right = x[half:]
    rightSet = set(right)
   # print(left)
   # print(right)
    for i in leftSet:
        if i in rightSet:
           # print(i)
            #print(valueList.index(i))
            score = score + valueList.index(i)
        
print(str(score)+" value")