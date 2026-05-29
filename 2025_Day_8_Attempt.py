import sys

def product(n):
    p = 1
    for i in n:
        p *= i
    return p

def distance(p1, p2):
    d = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5
    return d

file = "C:\\Users\\DANGO\\Documents\\Coding and Programming Folder\\2025 Day 8 Advent of Code Input.txt"

with open(file, 'rt') as f:
    junctions = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

circuits = []
found_min_dist = []
counter = 0
exception_reached = False
while True:
    circuit_found = False
    if exception_reached:
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
            exception_reached = True
            break
        for j, n2 in enumerate(junctions):
            if circuit_found:
                break
            if distance(n1, n2) == min_dist:    
                if len(circuits) > 0:
                    for k, c in enumerate(circuits):
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

                if len(circuits) == 0:
                    circuits.append((n1, n2))
                    found_min_dist.append((n1, n2, min_dist))
                    found_min_dist.append((n2, n1, min_dist))
                    circuit_found = True
                    break
    counter += 1
print(circuits)
