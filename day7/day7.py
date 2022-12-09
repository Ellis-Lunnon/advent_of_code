from collections import defaultdict
import logging
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)


def dir_size(tree: dict) -> int:
    size = 0
    for _, val in tree.items():
        if isinstance(val, int):
            size += val
        else:
            size += dir_size(val)

    return size

def walk(tree, total):
    size = dir_size(tree)
    logging.debug("current directory size %i" % size)
    if size < 100000:
        logging.debug("updating total")
        total += size
    for nn, node in tree.items():
        if isinstance(node, dict):
            logging.debug("walking subdir %s" % nn)
            updated_total = walk(node, total)
            logging.debug("Result of walking %s: new total %i" % (nn, updated_total))
            total += updated_total

    return total


def part1():
    with open("day7.txt", "r") as f:
        d = f.read().splitlines()

    dir_tree = {}
    csr: dict = None
    stk = []

    ls_bfr: list[tuple[str, int]] = []
    reading_ls = False

    for line in d:
        if line[0] == "$":
            # Handle previous LS outputs
            if reading_ls:
                logging.info("Creating new nodes in tree based on previous output")
                logging.debug(str(ls_bfr))
                # Create files as nodes with their size
                for fname, fsz in ls_bfr:
                    csr[fname] = fsz

                reading_ls = False
                ls_bfr.clear()

            cmd_txt = line[2:]
            if cmd_txt.startswith("cd"):
                dir = cmd_txt.replace("cd ", "")
                command, dest = "cd", dir

            elif cmd_txt.startswith("ls"):
                command, dest = "ls", None
            else:
                raise ValueError("Unseen command %s" % cmd_txt)

            logging.info("Found command %s (destination %s)" % (line, dest))
            # Handle changing directory
            if command == "cd":
                if dest == "/":
                    csr = dir_tree
                    stk.clear()
                elif dest == "..":
                    csr = stk.pop()
                else:
                    assert dest in csr and isinstance(csr[dest], dict)
                    stk.append(csr)
                    csr = csr[dest]
            elif command == "ls":
                reading_ls = True
        else:
            if line.startswith("dir"):
                # Create an empty directory
                csr[line.split(" ")[1]] = {}
            else:
                sz, name = line.split(" ")
                ls_bfr.append((name, int(sz)))

    pprint(dir_tree)
    pprint(walk(dir_tree, 0))


def sz(tree, cnt):
    logging.debug("current_size %d" % cnt)
    ttl = 0
    for nn, size in tree.items():
        logging.debug("parsing node %s" % nn)
        if isinstance(size, dict):
            ttl += sz(size, cnt)
        else:
            ttl += size

    logging.debug("directory scan finished with size %d", ttl)
    if ttl < 100_000:
        logging.debug("new total %d" % (ttl + cnt))
        return ttl + cnt
    else:
        logging.debug("directory too large (%d), skipping" % ttl)
        return cnt







# part1()
test_case = {                   # sum 284_000
        "file1": 100000,
        "dir1": {               # sum 29_000
            "file2": 2000,
            "file3": 3000,
            "dir2": {           # sum 4_000
                "file4": 4000,
            },
            "dir3": {           # sum 20_000
                "file6": 20000
            }
        },
        "dir4": {               # sum 155_000
            "file7": 30000,
            "file8": 100000,
            "dir5": {           # sum 25_000
                "file9": 25000
            }
        }
    }

                                # answer 78_000

logging.info("test case %i" % sz(test_case, 0))




