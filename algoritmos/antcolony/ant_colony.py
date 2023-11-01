# https://python.plainenglish.io/ant-colony-optimization-for-finding-the-optimal-well-trajectory-d673b86cf7a1

from collections import Counter
import numpy as np
import pandas as pd
import ast


df_init = pd.read_csv('/home/gtzuc/Documents/code/python-edu/algoritmos/antcolony/sample_rockmech.csv')

# add Pheromone column in df, it will be updated as the algorithm runs
df_init['Pheromone'] = 1

# simple tweaking to convert "str" type to "list" type
next_path = [ast.literal_eval(a) for a in df_init['Next Possible Path']]
df_init['Next Possible Path'] = next_path

paths = []
for i in df_init.index:
    path_init = df_init['Possible Path'].iloc[i]
    new_var=path_init.lower()    
    globals()[new_var] = df_init.iloc[i].values.tolist()
    paths.append(df_init.iloc[i].values.tolist())


# Calculate sum of distances and UCS values for all paths
sum_dist = sum(path[2] for path in paths)
sum_ucs = sum(path[3] for path in paths)

# Calculate length for multiple objectives (distance and UCS)
def length(ant):
    summ = 0
    for i in ant:
        for j in paths:
            if i == j[0]:
                sums = (j[2]/sum_dist + j[3]/sum_ucs)/2
                summ += sums
    return summ

# probabiity calculation for each path
def probabs(adja):
    pher_path_quality = []
    for i in adja:
        for j in paths:
            if j[0] == i:
                # Calculate pheromone and path quality for "distance"
                dis_pher_pq = j[4]*(1/(j[2]))
                dis_pher_pq = dis_pher_pq/sum_dist

                # Calculate pheromone and path quality for "ucs"
                ucs_pher_pq= j[4]*(1/(j[3]))
                ucs_pher_pq = ucs_pher_pq/sum_ucs

                pher_pq = (dis_pher_pq + ucs_pher_pq)/2
                pher_path_quality.append(pher_pq)

    # Calculate probability for each path
    summ = sum(pher_path_quality)
    probs = [pher_pq/summ for pher_pq in pher_path_quality]
    
    return probs

# randomly choosing path based on probability roulette
def choose_paths(adja):
    probab = probabs(adja)
    thresholds = np.cumsum(probab)
    r = np.random.random()

    for i, threshold in enumerate(thresholds):
        if r < threshold:
            return adja[i]

    return adja[-1]

# initiate the ant to pass the random path
def ant(init_path_1, init_path_2):
    path = []

    starter = choose_paths([init_path_1[0],init_path_2[0]])
    path.append(starter)

    for i in paths:
        if path[-1] == i[0]:
            adj = i[1]
            if len(adj)==0:
                break
            else:
                adj_random = choose_paths(adj)
                path.append(adj_random)
    return path


# pheromone evaporation
def evaporation(constant):
    for i in paths:
        i[4] = i[4] * (1 - constant)

# pheromone update
def update_pherom(ants):
    for i in ants:
        pherom = 1 / (length(i))
        for j in i:
            for k in paths:
                if k[0] == j:
                    k[4] = k[4] + pherom

# running the algorithm
def full_aco(iter_number, ant_number, init_path_1, init_path_2, evap_constant=0.3):
    """
    Runs the full Ant Colony Optimization (ACO) algorithm.

    Args:
    - iter_number (int): number of iterations to run the algorithm
    - ant_number (int): number of ants to use in each iteration
    - init_path_1 (tuple): initial path 1
    - init_path_2 (tuple): initial path 2
    - evap_constant (float): evaporation constant for pheromone evaporation

    Returns:
    - paths (list): list of all edges with their attributes, including the final pheromone levels
    - ants (list): list of all the paths taken by each ant in the final iteration
    """

    for i in range(iter_number):
        evaporation(constant=evap_constant)
        ants = []
        for j in range(ant_number):
            path = ant(init_path_1, init_path_2)
            ants.append(path)
        update_pherom(ants)
    return paths, ants

ac = ['AC', ['CD', 'CE'], 80, 83, 1]
ab = ['AB', ['BC', 'BD'], 100, 80, 1]
paths, ants = full_aco(iter_number = 100, ant_number = 100, init_path_1 = ac, init_path_2 = ab) 

print('\n Choosen path after running full algorithm')
print(Counter([str(i) for i in ants]).most_common())
