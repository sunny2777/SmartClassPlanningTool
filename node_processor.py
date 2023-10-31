from Node import Node
import networkx as nx
#import matplotlib.pyplot as plt

def extract_pre_requisite(input):
    path_lines = []
    fall = []
    spring = []
    summer = []

    nodes_list = []
    with open(input, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # store each line in the path_lines list
            path_lines.append(line)
    graph = nx.DiGraph()
    for i in path_lines:
        if (i.endswith("\n")):
            i = i[:-1]
            temp_store = i.split(",",3)
        else:
            temp_store = i.split(",",3)
        #print(temp_store)
        if(temp_store[3] == "None"):
            pre_req = [""]
        else:
            pre_req = (temp_store[3].split("-"))[1].split(",")
        #print(pre_req)
        node1 = Node(temp_store[0],temp_store[1],temp_store[2],pre_req)
        #print(node1.pre)
        nodes_list.append(node1)
        if("Fa" in temp_store[2] and (temp_store[1] not in fall)):
            fall.append(temp_store[0]+" "+temp_store[1])
        if("Sp" in temp_store[2] and (temp_store[1] not in spring)):
            spring.append(temp_store[0]+" "+temp_store[1])
        if("Su" in temp_store[2] and (temp_store[1] not in summer)):
            summer.append(temp_store[0]+" "+temp_store[1])
        graph.add_node(node1.number)
        if(len(node1.pre) == 1 and node1.pre[0] == ""):
            continue
        else:
            #print(len(node1.pre))
            if(len(node1.pre) == 1):
                graph.add_edges_from([(node1.pre[0],node1.number)])
            else:
                for j in node1.pre:
                    graph.add_edges_from([(j,node1.number)])
    print("The properties of the DAG graph are:\t",graph)
    print("The nodes in the graph are:\n",graph.nodes)
    print("------------------------------------------")

    return [graph,fall,spring,summer]



#input_processing2("input_test.txt")
#print(l)