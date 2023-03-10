import re
import sys
from math import sqrt
from typing import List

class ForwardCheck:
    #this is default constructor
    def __init__(self, puzzle: List[List[int]], size :int):
        self.puzzle = puzzle
        self.domains = {}
        self.size = size
       
        
    def forward_checking(self) -> List[List[int]]:
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    self.domains[(i, j)] = set(range(1, self.size + 1))
                else:
                    self.domains[(i, j)] = set([self.puzzle[i][j]])
        self.backtrack()
        return self.puzzle

    def check_constraints(self, coord, val):
        row, col = coord

        for i in range(self.size):
            if self.puzzle[row][i] == val or self.puzzle[i][col] == val:
                return False

        square_row, square_col = int(sqrt(self.size)) * (row // int(sqrt(self.size))), int(sqrt(self.size)) * (col // int(sqrt(self.size)))
        for i in range(square_row, square_row + int(sqrt(self.size))):
            for j in range(square_col, square_col + int(sqrt(self.size))):
                if self.puzzle[i][j] == val:
                    return False
        return True

    def backtrack(self):
        unassigned_vars = [(i, j) for i in range(self.size) for j in range(self.size) if self.puzzle[i][j] == 0]
        if not unassigned_vars:
            return True  
        var = min(unassigned_vars, key=lambda x: len(self.domains[x]))
        values = self.domains[var]
        for val in values:
            if self.check_constraints(var, val):
                self.puzzle[var[0]][var[1]] = val
                self.domains[var] = set([val])
                for neighbor in self.get_neighbors(var):
                    if val in self.domains[neighbor]:
                        self.domains[neighbor].remove(val)
                if self.backtrack():
                    return True
                self.puzzle[var[0]][var[1]] = 0
                self.domains[var] = values
                for neighbor in self.get_neighbors(var):
                    self.domains[neighbor].add(val)
        return False


    def get_neighbors(self,coord):
        row, col = coord
        neighbors = set()
        for i in range(9):
            if self.puzzle[row][i] == 0:
                neighbors.add((row, i))
            if self.puzzle[i][col] == 0:
                neighbors.add((i, col))
        square_row, square_col = int(sqrt(self.size)) * (row // int(sqrt(self.size))), int(sqrt(self.size)) * (col // int(sqrt(self.size)))
        for i in range(square_row, square_row + int(sqrt(self.size))):
            for j in range(square_col, square_col + int(sqrt(self.size))):
                if self.puzzle[i][j] == 0:
                    neighbors.add((i, j))
        return neighbors


    def print_puzzle(self) -> None:
        for i in range(len(self.puzzle)):
            if i % int(sqrt(self.size)) == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(self.puzzle[0])):
                if j % int(sqrt(self.size)) == 0 and j != 0:
                    print(" | ", end="")

                if j == self.size - 1:
                    print(self.puzzle[i][j])
                else:
                    print(str(self.puzzle[i][j]) + " ", end="")


def match_digits(line: str) -> list[int]:
    return [int(digit) for digit in re.findall(r"\d", line)]


def main():
    if len(sys.argv) != 2:
        print("Usage: python forward_checking.py <puzzle_file>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        line = f.readlines()
    puzzle = [match_digits(line) for line in line]
    forward_check = ForwardCheck(puzzle, 9)
    size = forward_check.size
    if puzzle is None:
        print("Invalid puzzle file or invalid file format.")
        sys.exit(1)
    if len(puzzle) != size or len(puzzle[0]) != size:
        print("Puzzle must be a square.")
        sys.exit(1)

    print("Puzzle:")
    
    forward_check.forward_checking()
    forward_check.print_puzzle()

if __name__ == "__main__":
    main()
