cities = list(map(int,input().split()));print('\n'.join([''.join([str([sum(cities[start:end]),sum(cities[end:start])][end<start]) for end in range(5)]) for start in range(5)]))