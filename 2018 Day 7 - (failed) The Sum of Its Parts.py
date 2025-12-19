import networkx as nx

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 7 Advent of Code Input.txt"

with open(file, 'rt') as f:
    instructions = [[line.strip().split()[1], line.strip().split()[-3]] for line in f.readlines()]

directed_graph = nx.DiGraph()
for s1, s2 in instructions:
    directed_graph.add_edge(s1, s2)
print(directed_graph)
print(''.join(nx.lexicographical_topological_sort(directed_graph)))

n_workers = 5

# Add amount of work for each node
for node in directed_graph.nodes:
    directed_graph.nodes[node]['work'] = 61 + ord(node) - ord('A')

time = 0
while directed_graph.nodes:
    # Find nodes available for work
    available_nodes = [node for node in directed_graph.nodes if directed_graph.in_degree(node) == 0]
    
    # Sort available nodes: Work on nodes with least remaining work
    available_nodes.sort(key=lambda node: directed_graph.nodes[node]['work'])
    
    # Reduce remaining work for n_workers of the available nodes
    for worker, node in zip(range(n_workers), available_nodes):
        # print("{}: Worker {} is on task {}".format(time, worker, node))
        directed_graph.nodes[node]['work'] -= 1

        # Remove finished nodes
        if directed_graph.nodes[node]['work'] == 0:
            # print("{}: Node {} is finished!".format(time, node))
            directed_graph.remove_node(node)

    # Increase time
    time += 1

print("Finishing all the work took {} seconds".format(time))
