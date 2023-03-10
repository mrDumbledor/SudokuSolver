
#  Sudoku Solver with Forward Checking

This code solves Sudoku puzzles using the Backtracking algorithm with Forward Checking heuristic. It reads a Sudoku puzzle from a file and solves it, then prints the solved puzzle.

### Usage
  

The code can be run from the command line using the following syntax:


`python forward_checking.py <puzzle_file>`


Where `<puzzle_file>` is the path to a file containing a Sudoku puzzle in the following format:

  

* Each row of the puzzle is represented by a line of digits.

* Each digit represents a number in the puzzle.

* Empty squares are represented by a 0.

  

For example, for the following puzzle:

  

```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079 
```
Program gives output:
```
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - - - - - - - - - - - 
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
- - - - - - - - - - - - - 
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9
```  

Should be saved in a file and passed to the script as follows:

  

python forward_checking.py example_puzzle.txt

  

### Implementation

  

The `ForwardCheck` class implements the Backtracking algorithm with `Forward Checking heuristic`. The `forward_checking()` method initializes the domains for each variable (empty square) and calls the `backtrack()` method to solve the puzzle. The `check_constraints()` method checks if a value can be assigned to a variable without violating any of the constraints. The `backtrack()`method recursively assigns values to variables, and uses Forward Checking to reduce the domains of neighboring variables. The `get_neighbors()`method returns the neighbors of a variable. The `print_puzzle()` method prints the solved puzzle. The `match_digits()` function extracts digits from a string. The `main()` function reads the puzzle from a file, creates an instance of ForwardCheck, and prints the solved puzzle.
