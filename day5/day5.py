import re
from pprint import pprint


def unwrap(lst, idx):
    if idx >= len(lst):
        return ""
    return lst[idx]

def getcol(data: list[str], idx: int):
    return list(filter(lambda x: bool(x) and x != " ", [unwrap(i, idx) for i in data]))[:-1][::-1]

def parsecols(cols):
    return [getcol(cols, (i * 4)+1) for i in range(0, 9)]

def parsemove(mv: str):
    match = re.match(r'move (\d+) from (\d+) to (\d+)', mv)
    n = int(match.group(1))
    origin = int(match.group(2)) - 1
    dest = int(match.group(3)) - 1
    return n, origin, dest

def part1():
    with open("day5.txt", "r") as f:
        lines = f.read().splitlines()

    sep = lines.index("")
    start_state = lines[:sep]
    cols = parsecols(start_state)
    input = (parsemove(i) for i in lines[sep+1:])
    pprint(cols)
    for n, start, end in input:
        for _ in range(n):
            cols[end].append(cols[start].pop())

    pprint("".join([i[len(i)-1] for i in cols]))

def part2():
    with open("day5.txt", "r") as f:
        lines = f.read().splitlines()

    sep = lines.index("")
    start_state = lines[:sep]
    cols = parsecols(start_state)
    input = (parsemove(i) for i in lines[sep+1:])
    pprint(cols)
    for n, start, end in input:
        tmp = []
        for _ in range(n):
            tmp.append(cols[start].pop())
        cols[end] += tmp[::-1]

    pprint("".join([i[len(i)-1] for i in cols]))



part1()
part2()