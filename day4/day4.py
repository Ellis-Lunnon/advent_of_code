def part1():
    with open("day4.txt", 'r') as f:
        d = f.read().splitlines()

    def parserange(rng: str) -> tuple[int, int]:
        prs = [int(i) for i in rng.split('-')]
        return list(range(prs[0], prs[1] + 1))

    def rangeisoverlapping(range1, range2) -> bool:
        if all(i in range2 for i in range1) or all(i in range1 for i in range2):
            return True
        return False

    cnt = 0
    for line in d:
        elf1, elf2 = line.split(',')
        rng1 = parserange(elf1)
        rng2 = parserange(elf2)
        if rangeisoverlapping(rng1, rng2):
            cnt += 1

    print(cnt)

def part2():
    with open("day4.txt", 'r') as f:
        d = f.read().splitlines()

    def parserange(rng: str) -> tuple[int, int]:
        prs = [int(i) for i in rng.split('-')]
        return list(range(prs[0], prs[1] + 1))

    def rangeisoverlapping(range1, range2) -> bool:
        if any(i in range2 for i in range1) or any(i in range1 for i in range2):
            return True
        return False

    cnt = 0
    for line in d:
        elf1, elf2 = line.split(',')
        rng1 = parserange(elf1)
        rng2 = parserange(elf2)
        if rangeisoverlapping(rng1, rng2):
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    part1()
    part2()




