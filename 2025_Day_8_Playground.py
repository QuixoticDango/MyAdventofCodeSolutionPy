import sys

def product(n):
    p = 1
    for i in n:
        p *= i
    return p

def distance(p1, p2):
    d = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5
    return d

file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 8 Advent of Code Input.txt"

with open(file, 'rt') as f:
    junctions = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

circuits = []
found_min_dist = []
counter = 0
# for counter in range(len(junctions)):
    # min_dist = min(distance(n1, n2) 
    #                for i, n1 in enumerate(junctions) 
    #                for j, n2 in enumerate(junctions) 
    #                if i != j and distance(n1, n2) not in found_min_dist)
exception_reached = False
while True:
    circuit_found = False
    # print('while')
    if exception_reached:
        # print("exception")
        break
    for i, n1 in enumerate(junctions):
        if circuit_found:
            break
        try:
            min_dist = min(distance(n1, n2) 
                    for i, n1 in enumerate(junctions) 
                    for j, n2 in enumerate(junctions)
                    if i != j and (n1, n2, distance(n1, n2)) not in found_min_dist)
        except:
            # print(f"{n1=}")
            exception_reached = True
            break
        for j, n2 in enumerate(junctions):
            # print('second for loop')
            if circuit_found:
                break
            if distance(n1, n2) == min_dist:    
                if len(circuits) > 0:
                    # print('made it to circuits > 0')
                    for k, c in enumerate(circuits):
                        # print(f"{k=} and {c=}")
                        if n1 not in c and n2 not in c:
                            circuits.append((n1, n2))
                            found_min_dist.append((n1, n2, min_dist))
                            found_min_dist.append((n2, n1, min_dist))
                            circuit_found = True
                            break
                        
                        if n1 in c and n2 not in c:
                            circuits[k] += (n2,)
                            found_min_dist.append((n1, n2, min_dist))
                            found_min_dist.append((n2, n1, min_dist))
                            circuit_found = True
                            break
                        
                        if n1 not in c and n2 in c:
                            circuits[k] += (n1,)
                            found_min_dist.append((n1, n2, min_dist))
                            found_min_dist.append((n2, n1, min_dist))
                            circuit_found = True
                            break

                        if (n1, n2, distance(n1, n2)) in found_min_dist\
                              or (n2, n1, distance(n1, n2)) in found_min_dist:

                if len(circuits) == 0:
                    # print("made it to first condition")
                    circuits.append((n1, n2))
                    found_min_dist.append((n1, n2, min_dist))
                    found_min_dist.append((n2, n1, min_dist))
                    circuit_found = True
                    break
    counter += 1
# circuits.sort(key=lambda c: len(c), reverse=True)
print(circuits)


# circuits = []
# found_min_dist = []
# min_dist = sys.maxsize - 1
# count = 0
# # print(any(len(c) < 2 for c in circuits))
# while min_dist < sys.maxsize:
# # while count < 6:
#     if count == 0:
#         circuits = []
#     min_dist = sys.maxsize
#     for i, n1 in enumerate(junctions):
#         for j, n2 in enumerate(junctions):
#             if i != j and distance(n1, n2) < min_dist and distance(n1, n2) not in found_min_dist:
#                 min_dist = distance(n1, n2)

#     found_min_dist.append(min_dist)
#     # print(found_min_dist)
#     circuit_added = False

#     for i, n1 in enumerate(junctions):
#         if circuit_added:
#             break
#         for j, n2 in enumerate(junctions):
#             if circuit_added:
#                 break
#             if i != j and distance(n1, n2) == min_dist:
#                 for k, circuit in enumerate(circuits):
#                     # print(f"{circuit=}")
#                     if n1 in circuits[-1] and not n2 in circuits[-1]:
#                         # print(f"1st condition")
#                         circuits[k] += n2,
#                         # print(f"After 1st condition: {circuit=}")
#                         # print(f"After 1st condtion: {circuits=}")
#                         circuit_added = True
#                         break
#                     if n2 in circuits[-1] and not n1 in circuits[-1]:
#                         # print(f"2nd condition")
#                         circuits[k] += n1,
#                         circuit_added = True
#                         break
#                 if not any(n1 in circuits[i] for i in range(len(circuits))) and \
#                 not any(n2 in circuits[i] for i in range(len(circuits))):
#                     # print("No break before this point")
#                     circuits.append((n1, n2))
#                     circuit_added = True
#                     break
#     count += 1
# print(circuits)
# circuits.sort(key=lambda c: len(c), reverse=True)
# print(product(len(c) for i, c in enumerate(circuits) if i < 3))




# # min_dist = min(distance(n1, n2) for i, n1 in enumerate(junctions)
# #             for j, n2 in enumerate(junctions)
# #             if i != j and not any(n1 in circuits[i] for i in range(len(circuits)))
# #             or not any(n2 in circuits[j] for j in range(len(circuits))))
# # distance_found = list()
# # for i, n1 in enumerate(junctions):
# #     circuit = set()
# #     min_dist = min(distance(n1, n2) for i, n1 in enumerate(junctions)
# #             for j, n2 in enumerate(junctions)
# #             if i != j and not any(n1 in circuits[i] for i in range(len(circuits)))
# #             or not any(n2 in circuits[j] for j in range(len(circuits))))
# #     for j, n2 in enumerate(junctions):
# #         if distance(n1, n2) == min_dist:
# #             circuit.add(n1)
# #             circuit.add(n2)
# #             circuits.append(circuit)
# # print(circuits)
#         # if i != j and not ((node1, node2, distance(node1, node2)) in distance_found \
#         #                    or (node2, node1, distance(node1, node2)) in distance_found):
#         #     distance_found.append((node1, node2, distance(node1, node2)))

# # distance_found.sort(key=lambda s: s[2])
# # circuits = list((distance_found[0][0], distance_found[0][1]))
# # for i, data1 in enumerate(distance_found):
# #     n1, n2, d = data1
# #     node_connected = False
# #     for j, data2 in enumerate(distance_found):
# #         if i == j:
# #             continue
# #         n3, n4, d = data2
# #         if n3 in data1:
