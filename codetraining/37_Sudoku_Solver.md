### 37 Sudoku Solver

---

> * 问题
> * 代码
> * 思路

---

## 问题

解数独

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。

数字 1-9 在每一列只能出现一次。

数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

空白格用 '.' 表示。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。

你可以假设给定的数独只有唯一解。

给定数独永远是 9x9 形式的。

## 代码

```python
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solveSudokuDFS(board,0,0)
    def solveSudokuDFS(self,board,row,column):
        if row==len(board): 
            return True
        if column>=len(board[row]):
            return self.solveSudokuDFS(board,row+1,0)
        if board[row][column]==".":
            for num in range(9):
                board[row][column]=str(num+1)
                if self.isValid(board,row,column):
                    if self.solveSudokuDFS(board,row,column+1):
                        return True
                board[row][column]="."
        else : 
            return self.solveSudokuDFS(board,row,column+1)
        return False    
    def isValid(self,board,row,column):
        numset=set()
        for i in range(len(board[row])):
            if board[row][i] in numset and board[row][i]!=".":
                return False
            else: 
                numset.add(board[row][i])
        numset.clear()
        for i in range(len(board)):
            if board[i][column] in numset and board[i][column]!=".":
                return False
            else: 
                numset.add(board[i][column])
        numset.clear()
        for i in range(3):
            for j in range(3):
                if board[row//3*3+i][column//3*3+j] in numset and board[row//3*3+i][column//3*3+j]!=".":
                    return False
                else:
                    numset.add(board[row//3*3+i][column//3*3+j])
        return True
            
sl=Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
sl.solveSudoku(board)
print(board)
```

## 思路

对于每个需要填数字的格子带入1到9，每代入一个数字都判定其是否合法，如果合法就继续下一次递归，结束时把数字设回'.'，判断新加入的数字是否合法时，只需要判定当前数字是否合法，不需要判定这个数组是否为数独数组，因为之前加进的数字都是合法的，这样可以使程序更加高效一些