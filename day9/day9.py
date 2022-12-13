from typing import Generator


def getSeq() -> Generator[str, None, None]:
    with open("day9.txt", "r") as f:
        d = f.read().splitlines()

    for i in d:
        # print(i)
        yield i


def monitor(cycle, reg, storage):
    

def part1():
    instructions = getSeq()

    reg = 0
    cycle = 0
    add_bfr = 0
    bfr_isLive = False
    storage = []

    while True:
        cycle += 1
        print(cycle)
        if bfr_isLive:
            # print("buffer is live")
            reg += add_bfr
            bfr_isLive = False
            continue
            
        try:
            ins = next(instructions)
        except StopIteration:
            cycle -= 1
            break

        if ins == "noop":
            continue
        elif ins.startswith("addx"):
            _, val = ins.split(" ")
            add_bfr = int(val)
            bfr_isLive = True
            # print("add %i" % add_bfr)
            continue

    print(reg)

if __name__ == "__main__":
    part1()

