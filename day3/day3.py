def val(char):
    if ord(char) in list(range(97, 123)):
        return ord(char) - 96
    else:
        return ord(char) - 38

def part1():
    f = open("input.txt")
    d = f.readlines()
    f.close()
    shared_symbols = []
    for pack in d:
        midpoint = len(pack) // 2
        shared_symbols.append(max([i for i in pack[:midpoint] if i in pack[midpoint:]]))

    # print(shared_symbols)
    print(sum(map(val, shared_symbols)))


def part2():
    with open("input.txt", "r") as f:
        d = f.readlines()

    def get_groups(all):
        n_groups = len(all) // 3
        for i in range(n_groups):
            yield all[3 * i : (3 * i) + 3]

    common = []
    for group in get_groups(d):
        common.append(max(i for i in group[0] if i in group[1] and i in group[2]))

    print(sum(val(i) for i in common))

part1()
part2()


