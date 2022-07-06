# import everything from tkinter module
from tkinter import *
import numpy as np
import math 

#Open the file with the data
f1 = open("raw5_2.txt", "r") 

#Open file to write
f2 = open('sequence5_1.txt', 'w')
f3 = open('.txt', 'w')

#Set number of vehicles
vehicles = 5
static_nodes = 24
entries = 500
columns = 10
sum = 1

#---------------INITIALIZATIONS START-----------------------------------------------------------------
#Create an array for storing the time spend in each Static Nodes visited by each Mobile node 1
mn1_timestayed = np.array(range(static_nodes*columns))
mn1_timestayed = mn1_timestayed.reshape(static_nodes,columns)

#Create an array for storing the time spend in each Static Nodes visited by each Mobile node 2
mn2_timestayed = np.array(range(static_nodes*columns))
mn2_timestayed = mn2_timestayed.reshape(static_nodes,columns)

#Create an array for storing the time spend in each Static Nodes visited by each Mobile node 3
mn3_timestayed = np.array(range(static_nodes*columns))
mn3_timestayed = mn3_timestayed.reshape(static_nodes,columns)

#Create an array for storing the time spend in each Static Nodes visited by each Mobile node 4
mn4_timestayed = np.array(range(static_nodes*columns))
mn4_timestayed = mn4_timestayed.reshape(static_nodes,columns)

#Create an array for storing the time spend in each Static Nodes visited by each Mobile node 5
mn5_timestayed = np.array(range(static_nodes*columns))
mn5_timestayed = mn5_timestayed.reshape(static_nodes,columns)

#Create an array for storing the time spend in each Static Nodes visited by each Mobile node
timestayed = np.array(range(vehicles*entries))
timestayed = timestayed.reshape(vehicles,entries)

#Create an array for storing the Static Nodes visited by each Mobile node
sequence = np.array(range(vehicles*entries))
sequence = sequence.reshape(vehicles,entries)

#Create an array for storing how many differentvisits we have to each Static Node by each Mobile node
differentvisits = np.array(range(vehicles*sum))
differentvisits = differentvisits.reshape(vehicles,sum)

#Create an array to store the sum of time stayed each mobile node to each static node
sumtimestayed = np.array(range(vehicles*static_nodes))
sumtimestayed = sumtimestayed.reshape(vehicles,static_nodes)

#Create an array to store the sum of time visited each mobile node to each static node
sumtimesvisited = np.array(range(vehicles*static_nodes))
sumtimesvisited = sumtimesvisited.reshape(vehicles,static_nodes)

#Create an array to store the average of time stayed each mobile node to each static node
averagetimestayed = np.array(range(vehicles*static_nodes))
averagetimestayed = averagetimestayed.reshape(vehicles,static_nodes)

#Create an array to store the mean of time stayed each mobile node to each static node
meantimestayed = np.array(range(vehicles*static_nodes))
meantimestayed = meantimestayed.reshape(vehicles,static_nodes)

#Create an array to store the standard deviation of time stayed each mobile node to each static node
standarddeviationtimestayed = np.array(range(vehicles*static_nodes))
standarddeviationtimestayed = standarddeviationtimestayed.reshape(vehicles,static_nodes)

#Create an array with the perfect changes
perfectchanges = np.array(range(250*2))
perfectchanges = perfectchanges.reshape(250,2)

#Initialize the array with zeros since there wont be Static node = 0
for a in range (static_nodes):
    for b in range (0, columns):
        mn1_timestayed[a][b]=0
        mn2_timestayed[a][b]=0
        mn3_timestayed[a][b]=0
        mn4_timestayed[a][b]=0
        mn5_timestayed[a][b]=0

#Initialize the array with zeros since there wont be Static node = 0
for a in range (vehicles):
    for b in range (entries):
        timestayed[a][b]=0
        sequence[a][b]=0

#Initialize the array with zeros
for a in range (vehicles):
    for b in range (sum):
        differentvisits[a][b]=0
#print(differentvisits)

#Initialize the array with zeros
for a in range (0, vehicles):
    for b in range (0, static_nodes):
        sumtimestayed[a][b]=0
        sumtimesvisited[a][b]=0
        averagetimestayed[a][b]=0
        meantimestayed[a][b]=0
        standarddeviationtimestayed[a][b]=0
        
#Initialize the array with zeros
for a in range (250):
    for b in range (2):
        perfectchanges[a][b]=0

#counter for perfectchanges array
perfectcounter=0

#---------------INITIALIZATIONS END----------------------------------------------------------------------
 
#Check every line from CARLA output
for line in f1:
    
    #Input the line to data
    data=line.split()
    
    for y in range (1,vehicles+1):
        #print(y)
        if int(data[0]) == y :
            if differentvisits[y-1]==0:
                #Store the first Static node and the first timestamp
                timestayed[y-1][differentvisits[y-1]] = data[1]
                #Store the first Static node and the first timestamp
                sequence[y-1][differentvisits[y-1]] = data[2]
                #Step
                differentvisits[y-1] = differentvisits[y-1] + 1
                #perfectchanges array
                perfectchanges[perfectcounter][0] = data[0]
                perfectchanges[perfectcounter][1] = data[1]
                perfectcounter = perfectcounter + 1
            
            #Check if the next static node is different from the previous
            elif (int(data[2]) != sequence[y-1][differentvisits[y-1]-1]):
                #Calculate the time stayed in this Static node
                timestayed[y-1][differentvisits[y-1]-1] = int(data[1]) - timestayed[y-1][differentvisits[y-1]-1]
                #We are using the next slot to store the previous timestamp essencially the timestayed[y-1][differentvisits[y-1]] == timestayed[y-1][differentvisits[y-1]-1] for the next loop
                timestayed[y-1][differentvisits[y-1]] = int(data[1])
                #Store the new Static node
                sequence[y-1][differentvisits[y-1]] = data[2]
                #Step
                differentvisits[y-1] = differentvisits[y-1] + 1
                #perfectchanges array
                perfectchanges[perfectcounter][0] = data[0]
                perfectchanges[perfectcounter][1] = data[1]
                perfectcounter = perfectcounter + 1
                
f1.close()

#printing the 2D-sequence
print("\nThe 2D-sequence is:")
for i in sequence:
    for j in i:
        if j !=0:
            print(j, end=" ")
    print()

#printing the 2D-timestayed
print("\nThe 2D-timestayed is:")
for i in timestayed:
    for j in i:
        if j !=0:
            print(j, end=" ")
    print()

#we dont want to calculate the last visit
for i in range (0, vehicles):
    differentvisits[i] = int(differentvisits[i]) - 1

#printing the differentvisits len(sequence[1-vehicles])
print("\nThe differentvisits are:")
for i in differentvisits:
    print(i, end=" ")
print()

#Calculate the sum time stayed each mobile node at each static node
for i in range (0, vehicles):
    for j in range (0, static_nodes):
        for z in range (0, int(differentvisits[i])):
            if int(sequence[i][z]) == j+1 :
                sumtimestayed[i][j] = sumtimestayed[i][j] + timestayed[i][z]
                sumtimesvisited[i][j] = sumtimesvisited[i][j] + 1
print("\nThe 2D-sumtimestayed is:")
print(sumtimestayed)
print("\nThe 2D-sumtimesvisited is:")
print(sumtimesvisited)

#Calculate the averagetimestayed each mobile node at each static node
for i in range (0, vehicles):
    for j in range (0, static_nodes):
        if ( sumtimesvisited[i][j] != 0):
            averagetimestayed[i][j] = sumtimestayed[i][j] / sumtimesvisited[i][j]
print("\nThe 2D-averagetimestayed is:")
print(averagetimestayed)

#Create the time sequence for each visit of each mobile node
for i in range (0, vehicles):
    for j in range (0, int(differentvisits[i])):
        for z in range (0, 2500):
            if i == 0 :
                if (int(mn1_timestayed[sequence[i][j]-1][z]) == 0):
                    mn1_timestayed[sequence[i][j]-1][z] = timestayed[i][j]
                    break
            elif i == 1:
                if (int(mn2_timestayed[sequence[i][j]-1][z]) == 0):
                    mn2_timestayed[sequence[i][j]-1][z] = timestayed[i][j]
                    break
            elif i == 2:
                if (int(mn3_timestayed[sequence[i][j]-1][z]) == 0):
                    mn3_timestayed[sequence[i][j]-1][z] = timestayed[i][j]
                    break
            elif i == 3:
                if (int(mn4_timestayed[sequence[i][j]-1][z]) == 0):
                    mn4_timestayed[sequence[i][j]-1][z] = timestayed[i][j]
                    break
            elif i == 4:
                if (int(mn5_timestayed[sequence[i][j]-1][z]) == 0):
                    mn5_timestayed[sequence[i][j]-1][z] = timestayed[i][j]
                    break

#printing the 2D-mnX_timestayed
print("\nThe mn1_timestayed is:")
print(mn1_timestayed)
print("\nThe mn2_timestayed is:")
print(mn2_timestayed)
print("\nThe mn3_timestayed is:")
print(mn3_timestayed)
print("\nThe mn4_timestayed is:")
print(mn4_timestayed)
print("\nThe mn5_timestayed is:")
print(mn5_timestayed)

#Calculate the meantimestayed each mobile node at each static node
print("\nThe meantimestayed is:")
for i in range (0, vehicles):
    for j in range (0, static_nodes-1):
        for z in range (0, int(sumtimesvisited[i][j])):
            if i==0:
                meantimestayed[i][j] = meantimestayed[i][j] + (mn1_timestayed[j][z] - averagetimestayed[i][j])**2
            if i==1:
                meantimestayed[i][j] = meantimestayed[i][j] + (mn2_timestayed[j][z] - averagetimestayed[i][j])**2
            if i==2:
                meantimestayed[i][j] = meantimestayed[i][j] + (mn3_timestayed[j][z] - averagetimestayed[i][j])**2
            if i==3:
                meantimestayed[i][j] = meantimestayed[i][j] + (mn4_timestayed[j][z] - averagetimestayed[i][j])**2
            if i==4:
                meantimestayed[i][j] = meantimestayed[i][j] + (mn5_timestayed[j][z] - averagetimestayed[i][j])**2
print(meantimestayed)

#Calculate the standarddeviationtimestayed each mobile node at each static node
print("\nThe standarddeviationtimestayed is:")
for i in range (0, vehicles):
    for j in range (0, static_nodes-1):
        if ((int(sumtimesvisited[i][j])-1) != 0):
            standarddeviationtimestayed[i][j] = math.sqrt((int(meantimestayed[i][j])) / (int(sumtimesvisited[i][j])-1))
print(standarddeviationtimestayed)

print(perfectchanges)

#------------------------------GUI START---------------------------------------

#------------------------------GUI END-----------------------------------------

"""
#for i in range(0, 5):
    #for j in range(0, 24):
        #print('%s' % (i+1) + ' %s' % (j+1) + ' %s' % timestayed[i][j] + ' %s' % sequence[i][j])
"""