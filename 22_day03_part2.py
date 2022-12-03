# Initialise Values
myValues=[]
score=0
counter=0
valueList=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Datafiles
inputFile='22_day03_input.txt'
#inputFile='22_day03_input_test.txt'

with open(inputFile) as f:
    for line in f:
        myValues.append(line.strip())

# Step though array
for x in myValues:
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