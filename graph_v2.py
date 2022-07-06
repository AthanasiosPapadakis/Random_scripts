from pyvis.network import Network

#add this to html file, inside #mynetwork , to set the town as background
#background-image: url("towntest.jpg");

net = Network("750px", "900px",directed=True)

static_nodes = [(365,35), (365,105), (365,175), (365,245), (365,315),
                (295,35), (295,175), (295,315),
                (225,35), (225,175), (225,315),
                (155,35), (155,175), (155,315),
                (85,35), (85,245), (85,315), (85,245), (85,315),
                (25,35), (25,245), (25,315),(25,175), (25,245)]

#How many vehicle are in the experiment
vehicle = 10
#We have created an array with sorted_data[2*vehicle+1][][]
#The firt "vehicle" rows are the timestayed array
#The second "vehicle" rows are the sequence array
#The final row (if it is added) is the pings array
#print(sorted_data[11][0])
sorted_data = []
#Helps to create multiple nodes
counter=0

# Input file and separate the items via ' '
for line in open('sorted1.txt', 'r'):
    sorted_data.append(line.strip().split(' ')) 


while True:

    value = input("Please enter the Mobile Node you want to visualize:\n")
    value = int(value)
    #Helps to pick the proper row
    proper_row = vehicle+(value-1)
    #Helps for the loop
    row_len= len(sorted_data[proper_row])

    try:
        print("Showing Mobile node ", value)
        for i in range (row_len):
            
            if int(sorted_data[proper_row][counter]) != 0:
                #print(sorted_data[proper_row][counter])
                net.add_node(sorted_data[proper_row][counter], value=sorted_data[value-1][counter],
                    x=[static_nodes[int(sorted_data[proper_row][counter])-1][0]],
                    y=[static_nodes[int(sorted_data[proper_row][counter])-1][1]],
                    color=['#0000ff'])
                if counter != 0:
                    net.add_edge(sorted_data[proper_row][counter-1], sorted_data[proper_row][counter], length = 150)
                counter=counter+1                
    except ValueError:
        print("Error! This is not a number. Try again.")
        
    else:
        #print("All ok!")
        break

net.show_buttons(filter_=True)
net.show('mygraph.html')