# Proyecto 2
#Rodrigo Benavente 
#Ana Minchaca
#Rodrigo Sibaja
#Fernando Garrote
#Karen Morgado
import numpy as np
from itertools import chain, combinations

print("Note: The text file with the NFA must be located in the same directory as the program")
document = input("Enter the name of the text file: ")
#print(document)

#test = open(document + ".txt","r")#Opens the text file where the NFA is found
test = open(document+".txt","r") #The text file has to be in the same directory as the python code
content = test.read()#content now has the values of the text file
content = [content.split(')')[0] for content in content.split('(') if ')' in content]#We separete all the values
table = np.zeros((len(content),3),'U2')#This is where we create our array
vocabulario = []#We create an array called vocabulario 
estados = []#We create an array called estados 
powerSeterino = []


#prueba = len(content)
#print(content[1])

def getVal(content, i):
    global table
    inputDatum = ""
    vI = ""
    vJ = ""
    flag = 0
    for k in range(len(content[i])):
        if content[i][k] == ",":
            flag = flag +1
            k = k+1
            
        elif flag == 0 and content[i] not in inputDatum:
            inputDatum = inputDatum + content[i][k]
            
        elif flag == 1 and content[i] not in vI:
            vI = vI + content[i][k]
        elif flag == 2 and content[i] not in vJ:    
            vJ = vJ + content[i][k]
    #print(inputDatum)
    #print(vI)
    #print(vJ)    
    #inputDatum = content[i][0]#This is where we check if the thingies have a connection or not
    #vI = content[i][2]#First thingy 
    #vJ = content[i][4]#Second thingy
    table[i][0] = vI
    table[i][1] = inputDatum
    table[i][2] = vJ
    for i in range(len(inputDatum)):#In this for we fill vocabulario
        if inputDatum[i] not in vocabulario:
            vocabulario.append(inputDatum[i])
    #for i in range(len(vI)):#We fill estados
    if vI not in estados:
        estados.append(vI)
    if vJ not in estados:
        estados.append(vJ)
    #print(inputDatum)
    #print(vI)
    #print(vJ)

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


for i in range(len(content)):
    getVal(content, i)
    
powerSeterino = list(powerset(estados))

finalTable = np.zeros((len(powerSeterino),(len(vocabulario))),'U10')
#for i in range(len(powerSeterino)):
 #   finalTable[i][0] = 

def union(valor, vocabV):
    concat = ""
    valor = ''.join(valor)
    #print(valor)
    #print(vocabV)
    #print(len(table))
    for n in range(len(valor)):
        for i in range(len(table)):
            #print(n)
            #print("Tablei0: "+table[i][0]+" ValorN: "+valor[n:n+len(table[i][0])]+" Tablei1: "+table[i][1]+" VocabV: "+vocabV)
            if table[i][0] == valor[n:n+len(table[i][0])] and table[i][1] == vocabV:
                concat = concat + table[i][2]
                #print(concat)
                    
    if len(estados[0]) <= 1:
        concat = ''.join(sorted(set(concat), key=concat.index))
    #print(concat)
    return (concat)        


for y in range(len(powerSeterino)):
    for x in range(len(vocabulario)):
        finalTable[y][x]=union(powerSeterino[y], vocabulario[x])

f = open("DFA.txt", "w")
f.write("{")
for y in range(len(powerSeterino)):
    for x in range(len(vocabulario)):
        valor = ''.join(powerSeterino[y])
        f.write("("+vocabulario[x]+","+valor+","+finalTable[y][x]+"),")     
f.write("}")
f.close()

print()
print("The produced DFA has been stored in the file DFA.txt ")
print()

input("Press any key to end the program")

#print(estados)
#print(table)
#print(vocabulario)
#print(powerSeterino)
#print(finalTable)