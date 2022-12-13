import logging

logging.basicConfig(level=logging.INFO)


def walk_dirs(tr, nm, sizes):
    size = 0
    for node_name, node_val in tr.items():
        if isinstance(node_val, dict):
            size += walk_dirs(node_val, nm + "/" + node_name, sizes)
        else:
            size += node_val

    logging.debug("Found %s with size %i" % (nm, size))
    sizes.append(size)

    return size

def part1():
    with open("day7.txt", "r") as f:
        d = f.read().splitlines()

    d.append("")
    dir_tree = {}
    csr: dict = {}
    stk = []

    ls_bfr: list[tuple[str, int]] = []
    reading_ls = False
    logging.info("Parsing %i lines for part 1" % len(d))
    for line in d:
        if not line or line[0] == "$":
            # Handle previous LS outputs
            if reading_ls:
                logging.debug("Handling previous ls output lines")
                logging.debug("Creating new nodes %s" % str(ls_bfr))
                # Create files as nodes with their size
                for fname, fsz in ls_bfr:
                    csr[fname] = fsz

                reading_ls = False
                ls_bfr.clear()

            cmd_txt = line[2:]
            if cmd_txt.startswith("cd"):
                command, dest = cmd_txt.split(" ")
            elif cmd_txt.startswith("ls"):
                command, dest = "ls", None
            elif not cmd_txt:
                continue
            else:
                raise ValueError("Unseen command %s" % cmd_txt)

            logging.debug("Found command %s (destination %s)" % (command, dest))
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
                logging.debug("Detected ls command")
            else:
                raise ValueError("Unknown command %s" % command)
        else:
            if line.startswith("dir"):
                # Create an empty directory
                csr[line.replace("dir ", "")] = {}
            else:
                sz, name = line.split(" ")
                ls_bfr.append((name, int(sz)))

    dir_sizes = []
    walk_dirs(dir_tree, "", dir_sizes)
    small_dirs = [i for i in dir_sizes if i <= 100_000]
    logging.debug("count: %i" % len(small_dirs))
    logging.info("Final total %i" % sum(small_dirs))

def part2():
    with open("day7.txt", "r") as f:
        d = f.read().splitlines()

    d.append("")
    dir_tree = {}
    csr: dict = {}
    stk = []

    ls_bfr: list[tuple[str, int]] = []
    reading_ls = False

    for line in d:
        if not line or line[0] == "$":
            # Handle previous LS outputs
            if reading_ls:
                logging.debug("Handling previous ls output lines")
                logging.debug("Creating new nodes %s" % str(ls_bfr))
                # Create files as nodes with their size
                for fname, fsz in ls_bfr:
                    csr[fname] = fsz

                reading_ls = False
                ls_bfr.clear()

            cmd_txt = line[2:]
            if cmd_txt.startswith("cd"):
                command, dest = cmd_txt.split(" ")
            elif cmd_txt.startswith("ls"):
                command, dest = "ls", None
            elif not cmd_txt:
                continue
            else:
                raise ValueError("Unseen command %s" % cmd_txt)

            logging.debug("Found command %s (destination %s)" % (command, dest))
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
                logging.debug("Detected ls command")
            else:
                raise ValueError("Unknown command %s" % command)
        else:
            if line.startswith("dir"):
                # Create an empty directory
                csr[line.replace("dir ", "")] = {}
            else:
                sz, name = line.split(" ")
                ls_bfr.append((name, int(sz)))

    dir_sizes = []
    walk_dirs(dir_tree, "", dir_sizes)

    device_used_space = max(dir_sizes)
    device_required_space = 30000000
    device_total_storage = 70000000
    device_free_space = device_total_storage - device_used_space
    device_space_to_free = device_required_space - device_free_space

    logging.info("Delete directory with size %i to free enough space" % min([i for i in dir_sizes if i >= device_space_to_free]))


part1()
part2()