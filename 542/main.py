from typing import List
# THE MINESWEEPER PROBLEM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        fake = [[0,0,0],[0,1,0],[0,0,0]]
        rows = len(mat)
        print(f'Rows: {rows}')
        cols = len(mat[0])
        print(f'Columns: {cols}')
        vector = []
        x_counter = 0
        y_counter = 0
        for r in mat:
            for c in r:
                if c == 0:
                    vector.append(c)
                else:
                    vector.append(1)
        return vector



def main():
    input1 = [[0,0,0],[0,1,0],[0,0,0]]
    input2 = [[0,0,0],[0,1,0],[1,1,1]]
    s = Solution()
    return s.updateMatrix(input2)

if __name__ == "__main__":
    print(main())
