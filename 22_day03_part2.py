# Initialise Array
myValues=[]
score=0
counter=0
myVal=None
# Read lines into the array
inputFile='22_day03_input.txt'
#inputFile='22_day03_input_test.txt'
valueList=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

with open(inputFile) as f:
    for line in f:
       # print(line.strip())
        myValues.append(line.strip())
#print(len(myValues))

# Step though array
for x in myValues:
   # print(x)
    #half = int((len(x))/2)
    #print(half)
   # left = x[:half]
   # leftSet = set(left)
   # right = x[half:]
   # rightSet = set(right)
   # print(left)
   # print(right)
    if counter == 0:
        first = set(x)
        counter = counter +1
    elif counter == 1:
        second = set(x)
        counter = counter+1
    elif counter == 2:
        third = set(x)
        counter = 0
        for i in third:
            if i in first and i in second:
                score = score + valueList.index(i)

        
print(str(score)+" value")