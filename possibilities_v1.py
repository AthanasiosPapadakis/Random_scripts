from pyvis.network import Network
net = Network("750px", "900px",directed=True)
#How many static nodes are in the experiment
static_nodes = 24
#Maximum number of connections that a static node has
max_transactions = 62
#Set number of vehicles
vehicles = 5

# All the pairs between the static nodes, each line has the transactions from one static node to another
# transactions [61][0]// transactions [61][1]
transactions = [(1,2), (1,6),
				(2,1), (2,6), (2,3), (2,4),
				(3,2), (3,6), (3,4),
				(4,3), (4,7), (4,5),
				(5,4), (5,8),
				(6,1), (6,2), (6,9),
				(7,2), (7,3), (7,4), (7,10),
				(8,5), (8,11),
				(9,6), (9,12),
				(10,7), (10,13),
				(11,8), (11,14),
				(12,9), (12,15),
				(13,10), (13,16), (13,17), (13,18),
				(14,11), (14,19),
				(15,12), (15,16), (15,20),
				(16,15), (16,13), (16,17),
				(17,16), (17,13), (17,18),
				(18,17), (18,13), (18,19),
				(19,18), (19,24), (19,14),
				(20,21), (20,15),
				(21,20), (21,22),
				(22,21), (22,23),
				(23,22), (23,24),
				(24,23), (24,19)]

#How many times a static node was visited by a specific vehicle
#print(visits[23][23][49])
visits = [[[0 for slice in range(vehicles)] for col in range(static_nodes)] for row in range(static_nodes)]

#How many times a static node was visited by a specific vehicle
#print(visit_sum[35][20]) = vehicle:36 & static node:21
visit_sum = [[0 for col in range(static_nodes)] for row in range(vehicles)]

#Create an array for storing the Static Nodes visited by each Mobile node
sequence = []

#Input file and separate the items via ' '
for line in open('visits5_1.txt', 'r'):
    sequence.append(line.strip().split(' ')) 

#Calculate the total visits for each mobile node to every static node
#print(visit_sum[35][20]) = vehicle:36 & static node:21
for row in range(vehicles):
    for col in range (len(sequence[row])):
        for i in range (1, static_nodes+1):
            if int(sequence[row][col]) == i:
                visit_sum [row][i-1] = visit_sum [row][i-1] + 1

#We have to start from the second value in the sequence array to see how many times went to 
#a specific pair of static nodes
for row in range(vehicles):
    for col in range(1,len(sequence[row])):  
        for i in range (1, static_nodes+1):
            if int(sequence[row][col]) == i:
                for a in range(max_transactions):
                    if int(sequence[row][col-1]) == int(transactions[a][0]):
                        #visits[y][x][vehicle] = (x,y)
                        visits[int(sequence[row][col])-1][int(sequence[row][col-1])-1][row] = visits[int(sequence[row][col])-1][int(sequence[row][col-1])-1][row] + 1
                        break

"""
#visits[y][x][vehicle] = (x,y)
print(visits[1][0][35])
print(visits[5][0][35])
#print(visit_sum[35][20]) = vehicle:36 & static node:21
print(visit_sum[35][0])
"""

while True:

    value = input("Please enter the Mobile Node you want to visualize:\n")
    value = int(value) - 1

    try:
        print("Showing Mobile node ", value+1)
        #First we have to create all the Static nodes
        for i in range(static_nodes):
            net.add_node(i+1, color=['#0000ff'])
        
        #Then we have to create the weighted edges
        for i in range(1, static_nodes+1):
            for j in range(1, static_nodes+1):
                if int(visits[i-1][j-1][value])!=0:
                    percentage = int(visits[i-1][j-1][value])/int(visit_sum[value][j-1])
                    #percentage_1 = int(visits[i-1][j-1][value])/int(visit_sum[value][j-1])
                    #percentage_2 = int(visits[j-1][i-1][value])/int(visit_sum[value][j-1])
                    print('From %s' % j + ' to %s' % i + ' with weight %s' %percentage)
                    net.add_edge(j, i, title=[percentage]) 
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        print("All ok!")
        break

#print(visits[1][0][49])
#print(visits[5][0][49])
#print(visit_sum[49][0])

net.show_buttons(filter_=True)
net.show('possibilities.html')