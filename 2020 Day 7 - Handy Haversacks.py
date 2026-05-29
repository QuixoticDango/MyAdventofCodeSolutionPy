import re
import networkx as nx

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2020 Day 7 Advent of Code Input.txt"

with open(file) as f:
    graph_rules = nx.DiGraph()
    rules = {}
    edges = []
    for line in f.readlines():
        parent = re.match(r"(.+?) bags contain", line).group(1)
        children = list(map(lambda t: (int(t[0]), t[1]), re.findall(r"(\d+) (.+?) bags?", line)))
        graph_rules.add_edges_from([(parent, child) for child in children])

shiny_gold_nodes = [node for node in graph_rules.nodes if 'shiny gold' in node]
for node in shiny_gold_nodes:
    # print(nx.descendants(graph_rules.reverse(), node))
    print(f"Predecessors: {nx.predecessor(graph_rules, node)}")
print(f"Part 1: {sum(len(nx.descendants(graph_rules.reverse(), node))
                     for node in shiny_gold_nodes)}")
# print(nx.ancestors(graph_rules, shiny_gold_nodes[-1]))
# print(sum(len(nx.ancestors(graph_rules, node)) for node in shiny_gold_nodes) + 1)