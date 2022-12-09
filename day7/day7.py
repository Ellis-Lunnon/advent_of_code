import logging

logging.basicConfig(level=logging.DEBUG)


def walk_dirs(tr, nm, sizes):
    size = 0
    for node_name, node_val in tr.items():
        if isinstance(node_val, dict):
            size += walk_dirs(node_val, nm + "/" + node_name, sizes)
        else:
            size += node_val

    logging.info("Found %s with size %i" % (nm, size))
    if size <= 100_000:
        sizes.append(size)
    return size

def part1():
    # with open("day7example.txt", "r") as f:
    #     d = f.read().splitlines()
    with open("day7.txt", "r") as f:
        d = f.read().splitlines()

    dir_tree = {}
    csr: dict = {}
    stk = []

    ls_bfr: list[tuple[str, int]] = []
    reading_ls = False

    for line in d:
        if line[0] == "$":
            # Handle previous LS outputs
            if reading_ls:
                logging.debug("Creating new nodes %s" % str(ls_bfr))
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
                csr[line.replace("dir ", "")] = {}
            else:
                sz, name = line.split(" ")
                ls_bfr.append((name, int(sz)))

    dir_sizes = []
    walk_dirs(dir_tree, "", dir_sizes)

    logging.info("Final total %i" % sum(dir_sizes))

part1()



