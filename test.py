import operator
def process_input():
    input1 = input()
    input1 = input1.split(' ')
    node_size = int(input1[0])
    edge_size= int(input1[-1])
    all_nodes = []
    
    nodes = {}
    edges = {}
    input2 = input()
    input2 = input2.split(' ')
    for i in range(0, node_size+1):
        nodes['name'] = i
        if i > 0:
            nodes['priority'] = int(input2[i-1])
        nodes['connections'] = []
        all_nodes.append(nodes.copy())
        nodes={}
    network = []
    for j in range(0, edge_size):
        edge = input()
        edge = edge.split(' ')
        node1 = edge[0]
        node2=edge[1]
        weight = edge[2]

        curr_node = all_nodes[int(node1)]
        temp = all_nodes[int(node2)]
        temp['weight'] = weight
        curr_node['connections'].append(temp) 
        network.append(curr_node.copy())
    return network[0]

def choose_path(node):
    highest_prio=0
    node_to_r = node
    for i in range(0, len(node['connections'])):
        if node['connections'][i]['priority'] > highest_prio:
            highest_prio = node['connections'][i]['priority']
            node_to_r = node['connections'][i]
        elif node['connections'][i]['priority'] == highest_prio:
            if node['connections'][i]['weight'] > node_to_r['weight']:
                node_to_r = node['connections'][i]
    return node_to_r

def traverse_node(node):
    path = [node]
    total_distance = 0
    while len(node['connections'])>0:
        node=choose_path(node)
        total_distance+=int(node['weight'])
        traverse_node(node)
        path.append(node)
    return total_distance
    #highest_prio = max(connection.iteritems(), key=operator.itemgetter(1))[0]


node = process_input()
dist=traverse_node(node)
print(dist)