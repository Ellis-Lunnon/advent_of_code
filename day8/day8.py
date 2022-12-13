from typing import Generator, TypeVar


ArrayData = TypeVar("ArrayData", int, float)
TArr = list[list[ArrayData]]

class Arr:
    def __init__(self, data: TArr) -> None:
        self._data = data

    def __repr__(self) -> str:
        return "\n".join(["".join(str(j) for j in i) for i in self._data])

    @property
    def shape(self) -> tuple[int, int]:
        rows = len(self._data)
        cols = len(self._data[0])
        return rows, cols

    def iterrow(self, idx) -> Generator[TArr, None, None]:
        for item in self._data[idx]:
            yield item

    def itercol(self, idx) -> Generator[TArr, None, None]:
        for row in self._data:
            yield row[idx]

    def get(self, row, col) -> TArr:
        return self._data[row][col]

    def set(self, value, row, col) -> None:
        self._data[row][col] = value

    
    def transpose(self):
        rows, cols = self.shape
        assert rows == cols

        newArr = self.fromShape(self.shape)
        for rIdx, row in enumerate(self._data):
            for cIdx, col in enumerate(row):
                newArr.set(col, (cols-1)-cIdx, (rows-1)-rIdx)

        return newArr


    def defined(self) -> int:
        flat = [j for i in self._data for j in i]
        return sum(flat)

    @staticmethod
    def fromShape(shape: tuple[int, int]) -> 'Arr':
        return Arr([[0] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def getViewDist(view_height, view) -> int:
        view_dist = 0
        for tree in view:
            view_dist += 1
            if tree >= view_height:
                break
        return view_dist
            

    def sceincScore(self, rowIdx, colIdx) -> int:
        rowMin, rowMax = 0, len(self._data) - 1
        colMin, colMax = 0, len(self._data[1]) - 1
        if rowIdx in [rowMin, rowMax] or colIdx in [colMin, colMax]:
            return 0

        row = list(self.iterrow(rowIdx))
        col = list(self.itercol(colIdx))
        # Search right, left, down, up
        view_dist_r = self.getViewDist(row[colIdx], row[colIdx+1:])
        view_dist_l = self.getViewDist(row[colIdx], row[:colIdx][::-1])
        view_dist_d = self.getViewDist(col[rowIdx], col[rowIdx+1:])
        view_dist_u = self.getViewDist(col[rowIdx], col[:rowIdx])

        return (
            view_dist_u *
            view_dist_d *
            view_dist_l * 
            view_dist_r
        )

def getArr() -> Arr:
    with open("day8.txt", "r") as f:
        d = Arr([[int(j) for j in i] for i in f.read().splitlines()])

    # d = Arr([[int(j) for j in i] for i in ["30373", "25512", "65332", "33549", "35390"]])
    return d

    
def part1():
    arr = getArr()
    mask = Arr.fromShape(arr.shape)

    rows, cols = arr.shape
    maxRow = rows-1
    maxCol = cols-1
    rowRange = range(arr.shape[0])
    colRange = range(arr.shape[1])

    for rowIdx in rowRange:
        tallestTree = arr.get(rowIdx, 0)
        mask.set(1, rowIdx, 0)
        for colIdx, treeHeight in enumerate(arr.iterrow(rowIdx)):
            if treeHeight > tallestTree:
                mask.set(1, rowIdx, colIdx)
                tallestTree = treeHeight

    for colIdx in colRange:
        tallestTree = arr.get(0, colIdx)
        mask.set(1, 0, colIdx)
        for rowIdx, treeHeight in enumerate(arr.itercol(colIdx)):
            if treeHeight > tallestTree:
                mask.set(1, rowIdx, colIdx)
                tallestTree = treeHeight

    for rowIdx in rowRange[::-1]:
        tallestTree = arr.get(rowIdx, maxCol)
        mask.set(1, rowIdx, maxCol)
        col = list(enumerate(arr.iterrow(rowIdx)))
        for colIdx, treeHeight in col[::-1]:
            if treeHeight > tallestTree:
                mask.set(1, rowIdx, colIdx)
                tallestTree = treeHeight

    for colIdx in colRange[::-1]:
        tallestTree = arr.get(maxRow, colIdx)
        mask.set(1, maxRow, colIdx)
        row = list(enumerate(arr.itercol(colIdx)))
        for rowIdx, treeHeight in row[::-1]:
            if treeHeight > tallestTree:
                mask.set(1, rowIdx, colIdx)
                tallestTree = treeHeight

    print(mask.defined())

def part2():
    arr = getArr()
    rows, cols = arr.shape
    scores = []
    for rowIdx in range(rows):
        for colIdx in range(cols):
            scores.append(arr.sceincScore(rowIdx, colIdx))

    print(max(scores))

if __name__ == "__main__":
    part1()
    part2()
