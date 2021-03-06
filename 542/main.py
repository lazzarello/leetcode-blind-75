from typing import List
# THE MINESWEEPER PROBLEM
# this is very helpful and prolly all the info I need to work this
# https://www.humaneer.org/blog/creating-matrices-in-python-tutorial/

# This problem should be called a Breadth First Search. Not sure why yet.
class Solution:
    def __init__(self):
        self.rows = 0
        self.columns = 0

    def get_column(self, matrix, col):
        return [matrix_i[col] for matrix_i in matrix]

    def get_row(self, matrix, row):
        return matrix[row]

    def get_size(self, matrix):
        num_rows = len(matrix)
        num_columns = len(matrix[0])
        return num_rows, num_columns

    def get_distance(self, vector):
        result = []
        counter = 0
        for item in vector:
            if item == 1:
                counter += 1
            else:
                counter = 0
            result.append(counter)
        return result

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_distance = []
        col_distance = []
        size = self.get_size(mat)
        self.rows = size[0]
        self.columns = size[1]
        col_counter = 0
        row_counter = 0
        # lulz, didn't know about range(int)
        for row in mat:
            print(f'Row {row_counter}: {row}')
            row_distance.append(self.get_distance(row))
            row_counter += 1
        for col in mat:
            c = self.get_column(mat, col_counter)
            print(f'Column {col_counter}: {c}')
            col_distance.append(self.get_distance(c))
            col_counter += 1

        result = [list(reversed(col)) for col in zip(*col_distance)]
        return result
        # return row_distance, col_distance

    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        fake = [[0,0,0],[0,1,0],[0,0,0]]
        rows = len(mat)
        print(f'Rows: {rows}')
        cols = len(mat[0])
        print(f'Columns: {cols}')
        vector = []
        x_counter = 0
        y_counter = 0
        # notice how for both problems you started with a nested loop
        # but it wasn't necessary for the solution?
        for r in mat:
            for c in r:
                if c == 0:
                    # notice how for both problems you transformed the matrix
                    # into a vector but that made it more complicated?
                    vector.append(c)
                else:
                    vector.append(1)
        return vector
    '''

def main():
    input1 = [[0,0,0],[0,1,0],[0,0,0]]
    input2 = [[0,0,0],[0,1,0],[1,1,1]]
    s = Solution()
    results = s.updateMatrix(input2)
    for row in range(s.rows):
        print(f'Distance Row {row}: {results[0][row]}')
    for col in range(s.columns):
        print(f'Distance Column {col}: {results[1][col]}')
    # looks like my column distance calculation works for both test cases
    d = results[1]
    # rotate 90 degrees counter clockwise. Discover why those -1 argumens do something interesting.
    # result = [[d[j][i] for j in range(len(d))] for i in range(len(d[0])-1,-1,-1)] 
    # rotate 90 degrees clockwise. WTF does zip() do?
    # reversed() is an iterator object that...reverses a list!
    # zip is wacky. it's an iterable that looks like it rotates a matrix
    # counter clockwise.
    result = [list(reversed(col)) for col in zip(*d)]
    return result

if __name__ == "__main__":
    print(main())
