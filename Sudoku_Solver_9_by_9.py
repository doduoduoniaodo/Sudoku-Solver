import tkinter as tk

def run():
    global sudoku_grid
    sudoku_grid = []
    for i in entries:
        e = []
        for j in i:
            e.append(j.get().strip())
        sudoku_grid.append(e)
    if solve_sudoku(0, 0):
        result_window()
    else:
        tk.Label(s, text='This sudoku has no solution', fg='red').place(x=120, y=315)

def result_window():
    result = tk.Toplevel(s)
    result.title('Result')
    result.geometry('400x400')
    j = 0
    for i in range(50, 320, 30):
        tk.Label(result, text='   '.join(sudoku_grid[j])).place(x=110, y=i)
        j += 1

def issafe(r, c, n):
    for x in range(9):
        if sudoku_grid[r][x] == n:
            return False
    for x in range(9):
        if sudoku_grid[x][c] == n:
            return False

    startRow = r - r % 3
    startCol = c - c % 3
    for i in range(3):
        for j in range(3):
            if sudoku_grid[i + startRow][j + startCol] == n:
                return False
            
    return True


def solve_sudoku(r, c):
    if r == 8 and c == 9:
        return True
    if c == 9:
        r += 1
        c = 0
    if sudoku_grid[r][c] != '':
        return solve_sudoku(r, c + 1)
    for num in range(1, 10, 1):
        if issafe(r, c, str(num)):
            sudoku_grid[r][c] = str(num)
            if solve_sudoku(r, c + 1):
                return True
        sudoku_grid[r][c] = ''
    return False
    
    

s = tk.Tk()
s.title('Sudoku Solver')
s.geometry('400x400')
w = tk.Label(s, text='Unknown number leave it blank', fg='blue').place(x=100, y=10)
entries = []
for i in range(50, 320, 30):
    e = []
    for j in range(60, 330, 30):
        entry = tk.Entry(s, width=3, justify='center')
        entry.place(x=j, y=i)
        e.append(entry)
    entries.append(e)
submit = tk.Button(s, text='Submit', width=25, command=run).place(x=100, y=340)

s.mainloop()


    
'''
Sample Input 1

1.45..89.
.963..5.1
53.41....
6......25
2.9...3.7
48......6
....37.54
9.7..563.
.45..12.9

Sample Output 1

124576893
796328541
538419762
671893425
259164387
483752916
862937154
917245638
345681279
'''


'''
Sample Input 2

9...28.57
5...192.3
.3.5...6.
.8.2..395
...7.6...
341..5.2.
.6...7.3.
1.895...4
75.46...9

Sample Output 2

916328457
574619283
832574961
687241395
295736148
341895726
469187532
128953674
753462819
'''
