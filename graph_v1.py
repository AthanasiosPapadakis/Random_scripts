from pyvis.network import Network

net = Network("500px", "500px")

#add this to html file, inside #mynetwork , to set the town as background
#background-image: url("towntest.jpg");

static_nodes = [(365,35), (365,105), (365,175), (365,245), (365,315),
                (295,35), (295,155), (295,315),
                (225,35), (225,155), (225,315),
                (155,35), (155,155), (155,315),
                (85,35), (85,245), (85,315), (85,245), (85,315),
                (25,35), (25,245), (25,315),(25,175), (25,245)]
                
                
print(static_nodes[0][1])

net.repulsion(node_distance=100, spring_length=105)

net.add_nodes([1, 2, 3, 4, 5], value=[10, 10, 10, 10, 10],
    title=['SN1 (365,35)','SN2 (365,105)','SN3 (365,175)','SN4 (365,245)','SN5 (365,315)'],
    x=[static_nodes[0][0], static_nodes[1][0], static_nodes[2][0], static_nodes[3][0], static_nodes[4][0]],
    y=[static_nodes[0][1], static_nodes[1][1], static_nodes[2][1], static_nodes[3][1], static_nodes[4][1]],
    label=['SN1','SN2','SN3','SN4','SN5'],
    color=['#3da831', '#3da831', '#3da831', '#3da831', '#3da831'])
    
net.add_nodes([6, 7, 8], value=[10, 10, 10],
    title=['SN6 (295,35)','SN7 (295,155)','SN8 (295,315)'],
    x=[static_nodes[5][0], static_nodes[6][0], static_nodes[7][0]],
    y=[static_nodes[5][1], static_nodes[6][1], static_nodes[7][1]],
    label=['SN6','SN7','SN8'],
    color=['#9a31a8', '#9a31a8', '#9a31a8'])
    
net.add_nodes([9, 10, 11], value=[10, 10, 10],
    title=['SN9','SN10','SN11'],
    x=[static_nodes[8][0], static_nodes[9][0], static_nodes[10][0]],
    y=[static_nodes[8][1], static_nodes[9][1], static_nodes[10][1]],
    label=['SN9','SN10','SN11'],
    color=['#3155a8', '#3155a8', '#3155a8'])

net.add_nodes([12, 13, 14], value=[10, 10, 10],
    title=['SN12','SN13','SN14'],
    x=[static_nodes[11][0], static_nodes[12][0], static_nodes[13][0]],
    y=[static_nodes[11][1], static_nodes[12][1], static_nodes[13][1]],
    label=['SN12','SN13','SN14'],
    color=['#eb4034', '#eb4034', '#eb4034'])

net.add_nodes([15, 16, 17, 18, 19], value=[10, 10, 10, 10, 10],
    title=['SN15','SN16','SN17','SN18','SN19'],
    x=[static_nodes[14][0], static_nodes[15][0], static_nodes[16][0], static_nodes[17][0], static_nodes[18][0]],
    y=[static_nodes[14][1], static_nodes[15][1], static_nodes[16][1], static_nodes[17][1], static_nodes[18][1]],
    label=['SN15','SN16','SN17','SN18','SN19'],
    color=['#FF7F24', '#FF7F24', '#FF7F24', '#FF7F24', '#FF7F24'])    

net.add_nodes([20, 21, 22, 23, 24], value=[10, 10, 10, 10, 10],
    title=['SN20','SN21','SN22','SN23','SN24'],
    x=[static_nodes[19][0], static_nodes[20][0], static_nodes[21][0], static_nodes[22][0], static_nodes[23][0]],
    y=[static_nodes[19][1], static_nodes[20][1], static_nodes[21][1], static_nodes[22][1], static_nodes[23][1]],
    label=['SN20','SN21','SN22','SN23','SN24'],
    color=['#CAFF70', '#CAFF70', '#CAFF70', '#CAFF70', '#CAFF70'])  

  

net.add_edges([(1, 2),(1, 6)])
net.add_edges([(2, 6), (2, 3), (2, 7)])
net.add_edges([(3, 7), (3, 4)])
net.add_edges([(4, 7), (4, 5)])
net.add_edges([(5, 8)]) 
#net.add_edges([(6, 9)])
#net.add_edges([(7, 10)])
#net.add_edges([(8, 11)])

#Set specific length at the edges
net.add_edge(9,6, length = 150)
net.add_edge(10,7, length = 150)
net.add_edge(11,8, length = 150)

#Set specific length at the edges
net.add_edge(12,9, length = 150)
net.add_edge(13,10, length = 150)
net.add_edge(14,11, length = 150)


#net.add_edges([(9, 12)])
#net.add_edges([(10, 13)])
#net.add_edges([(11, 14)])
net.add_edges([(12, 15)])

net.add_edge(13,17, length = 105)
net.add_edge(13,16, length = 200)
net.add_edge(13,18, length = 200)

#net.add_edges([(13, 16), (13, 17), (13, 18)]) 

net.add_edges([(14, 19)])
net.add_edges([(15, 16), (15, 20)])
net.add_edges([(16, 17)])
net.add_edges([(17, 18)])
net.add_edges([(18, 19)])
net.add_edges([(19, 24)])
net.add_edges([(20, 21)])
net.add_edges([(21, 22)])
net.add_edges([(22, 23)])
net.add_edges([(23, 24)])

#net.show_buttons(filter_=True)
net.show('mygraph.html')