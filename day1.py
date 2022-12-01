print(max([sum(j) for j in list(map(lambda x: [int(y) for y in x], [i.splitlines() for i in open('aoc1.txt', 'r').read().split('\n\n')]))]))

print(sum(sorted([sum(j) for j in list(map(lambda x: [int(y) for y in x], [i.splitlines() for i in open('aoc1.txt', 'r').read().split('\n\n')]))], reverse=True)[:3]))
