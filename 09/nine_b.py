import itertools

cities = set()
travel = []
distances = []
total = 0

with open('nine_raw.txt', 'r') as f:
    for line in f:
        t, d = line.strip().split('=')
        t = [x.strip() for x in t.split('to')]
        distances.append(t)
        travel.append(int(d))
        for i in t:
            cities.add(i)

for route in itertools.permutations(cities):
    dist = 0
    for index, city in enumerate(route):
        if index+1 < len(route):
            if [city, route[index+1]] in distances:
                dist += travel[distances.index([city, route[index+1]])]
            else:
                dist += travel[distances.index([route[index+1], city])]

    if dist > total:
        total = dist

print(total)
