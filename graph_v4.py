from pyvis.network import Network
import numpy as np

#add this to html file, inside #mynetwork , to set the town as background
#background-image: url("towntest.jpg");

net = Network("750px", "900px",directed=True)

#How many static nodes are there
static_node = 24

static_nodes = [(365,35), (365,105), (365,175), (365,245), (365,315),
                (295,35), (295,175), (295,315),
                (225,35), (225,175), (225,315),
                (155,35), (155,175), (155,315),
                (85,35), (85,105), (85,175), (85,245), (85,315),
                (25,35), (25,105), (25,175),(25,245), (25,315)]

#How many vehicle are in the experiment
vehicle = 50

#We have created an array with sorted_data[2*vehicle+1][][]
#The firt "vehicle" rows are the timestayed array
#The second "vehicle" rows are the sequence array
#The final row (if it is added) is the pings array

#Print(sorted_data[11][0])
sorted_data = []

#Helps to create multiple nodes
counter=0

# Input file and separate the items via ' '
for line in open('sorteddata50_1.txt', 'r'):
    sorted_data.append(line.strip().split(' ')) 

while True:

    value = input("Please enter the Mobile Node you want to visualize:\n")
    value = int(value)
    
    #Helps to pick the sequence row
    row_sequence = vehicle+(value-1)
    
    #Helps for the loop
    row_len= len(sorted_data[row_sequence])
    #To eliminate the last huge input at the timestayed
    row_len = row_len-1
  
    #Create an array to store the total sum of the seconds a vehicle stayed to a specific static node
    timestayed_sum = np.array(range(vehicle*static_node))
    timestayed_sum = timestayed_sum.reshape(static_node,vehicle)
    timestayed_sum = [[0 for col in range(vehicle)] for row in range(static_node)]

    #Before creating the graph we have to sum the total seconds a vehicle stayed to a specific static node
    for i in range (row_len):
        for j in range (1, static_node):
            if int(sorted_data[row_sequence][i])==j:
                timestayed_sum[j-1][value-1] = int(timestayed_sum[j-1][value-1]) + int(sorted_data[value-1][i])
    
    try:
        print("Showing Mobile node ", value)
        for i in range (row_len):
            if int(sorted_data[row_sequence][counter]) != 0:
                net.add_node(sorted_data[row_sequence][counter], value=int(timestayed_sum[int(sorted_data[row_sequence][counter])-1][value-1]),
                    #Set as a title the value hence how many seconds was the specific vehicle in 
                    title=[int(timestayed_sum[int(sorted_data[row_sequence][counter])-1][value-1])],
                    x=[static_nodes[int(sorted_data[row_sequence][counter])-1][0]],
                    y=[static_nodes[int(sorted_data[row_sequence][counter])-1][1]],
                    color=['#0000ff'])
                if counter != 0:
                    net.add_edge(sorted_data[row_sequence][counter-1], sorted_data[row_sequence][counter], length = 150)
                counter=counter+1                
    except ValueError:
        print("Error! This is not a number. Try again.")
        
    else:
        #print("All ok!")
        break

net.show_buttons(filter_=True)
net.show('mygraph.html')