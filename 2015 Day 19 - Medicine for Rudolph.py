import re

def unique_molecules(elements, molecule):
    key_list = list(elements.keys()) # An iterable list of all dictionary keys.
    uniques = [] # A list in which unique molecules will be placed
    for i in range(len(key_list)): # i is the index for a particular key
        for j in range(len(elements[key_list[i]])): # Each value in the dict is a list. j is the index for that list.
            start = 0 # This is the starting point for the string search. It's initialized to 0 when the while loop completes.
            while molecule.find(key_list[i], start) != -1: # Loop runs until the particular key isn't found.
                index = molecule.find(key_list[i], start) # Search begins from start and finds the index of the key
                mol_l = molecule[:index] # Slice the left side of string
                mol_r = molecule[index + len(key_list[i]):] # Slice the right side past the key
                new_mol = mol_l + (elements[key_list[i]][j]) + mol_r #insert a value from the value list into a new string
                if new_mol not in uniques:      # if the new string isn't in uniques, it's added.
                    uniques.append(new_mol)
                start = index + len(key_list[i]) # start is updated to an index past the original instance of the key.
    return len(uniques)

def mol_path_len(compounds, molecule):
    steps = 0
    compound_list = list(compounds.keys())
    while len(molecule) > 1:   
        for compound in compound_list:
            steps += len(re.findall(compound, molecule))
            molecule = re.sub(compound, compounds[compound], molecule)
        print(molecule)
    return steps
    
elements = dict()
compounds = dict()
while True:    
    rows = input().split(' => ')
    if rows == ['']:
        break
    if rows[0] not in elements.keys():
        elements[rows[0]] = [rows[1]]
    else:
        elements[rows[0]].append(rows[1])
    if rows[1] not in compounds.keys():
        compounds[rows[1]] = rows[0]

molecule = input("Enter initial molecular formula: ")
print(mol_path_len(compounds, molecule))