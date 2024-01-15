import numpy as np


people = np.array([
        'Surbhit',
        'Ulzii',
        'Pietro',
        'Lorenzo',
        'Echo',
        'Toni',
        'Janko',
        'Kanaan',
        'Cornelius'
])

pairings = np.random.permutation(np.arange(len(people)))
paired_people = people[pairings]

for i, pair in enumerate(paired_people[:-1].reshape(-1, 2)):
    print(f'Room {i}: {pair[0]}, {pair[1]}')

print('Leftout: ', paired_people[-1])

