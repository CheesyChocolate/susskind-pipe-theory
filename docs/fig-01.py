import matplotlib.pyplot as plt
import numpy as np

# Define the maze grid size
rows, cols = 5, 5

# Define a simple maze manually
# 0: empty, 1: horizontal pipe, 2: vertical pipe, 3: corner (right-down), 4: corner (down-left),
# 5: corner (left-up), 6: corner (up-right), 7: T-junction (up), 8: T-junction (down),
# 9: T-junction (left), 10: T-junction (right), 11: cross-junction
maze = [
    [0, 0,  2,  0, 0],
    [1, 1,  3,  2, 2],
    [0, 4,  1, 10, 0],
    [2, 0,  2,  3, 0],
    [0, 0,  1,  1, 0]
]

maze = [
    [1, 2,  3,  4, 5],
    [6, 7,  8,  9, 10],
    [11, 0,  0, 0, 0],
    [0, 0,  0,  0, 0],
    [0, 0,  0,  0, 0]
]

# Define input and output locations (row, col)
inputs = [(1, 0)]
outputs = [(4, 2)]

# Plotting the maze
fig, ax = plt.subplots(figsize=(8, 8))

# Draw the grid
for i in range(rows + 1):
    ax.plot([0, cols], [i, i], color='black')
    ax.plot([i, i], [0, rows], color='black')

# Draw the pipes
for r in range(rows):
    for c in range(cols):
        if maze[r][c] == 1:  # horizontal pipe
            ax.plot([c, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)
        elif maze[r][c] == 2:  # vertical pipe
            ax.plot([c+0.5, c+0.5], [r, r+1], color='blue', linewidth=5)
        elif maze[r][c] == 3:  # corner (right-down)
            ax.plot([c+0.5, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)
            ax.plot([c+0.5, c+0.5], [r+0.5, r+1], color='blue', linewidth=5)
        elif maze[r][c] == 4:  # corner (down-left)
            ax.plot([c, c+0.5], [r+0.5, r+0.5], color='blue', linewidth=5)
            ax.plot([c+0.5, c+0.5], [r+0.5, r+1], color='blue', linewidth=5)
        elif maze[r][c] == 5:  # corner (left-up)
            ax.plot([c, c+0.5], [r+0.5, r+0.5], color='blue', linewidth=5)
            ax.plot([c+0.5, c+0.5], [r, r+0.5], color='blue', linewidth=5)
        elif maze[r][c] == 6:  # corner (up-right)
            ax.plot([c+0.5, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)
            ax.plot([c+0.5, c+0.5], [r, r+0.5], color='blue', linewidth=5)
        elif maze[r][c] == 7:  # T-junction (up)
            ax.plot([c+0.5, c+0.5], [r, r+1], color='blue', linewidth=5)
            ax.plot([c, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)
        elif maze[r][c] == 8:  # T-junction (down)
            ax.plot([c+0.5, c+0.5], [r, r+1], color='blue', linewidth=5)
            ax.plot([c, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)
        elif maze[r][c] == 9:  # T-junction (left)
            ax.plot([c+0.5, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)
            ax.plot([c+0.5, c+0.5], [r, r+1], color='blue', linewidth=5)
        elif maze[r][c] == 10:  # T-junction (right)
            ax.plot([c+0.5, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)
            ax.plot([c+0.5, c+0.5], [r, r+1], color='blue', linewidth=5)
        elif maze[r][c] == 11:  # cross-junction
            ax.plot([c+0.5, c+0.5], [r, r+1], color='blue', linewidth=5)
            ax.plot([c, c+1], [r+0.5, r+0.5], color='blue', linewidth=5)

# Mark the input and output locations
for (r, c) in inputs:
    ax.plot(c + 0.5, r + 0.5, 'go', markersize=15)  # green circle for inputs

for (r, c) in outputs:
    ax.plot(c + 0.5, r + 0.5, 'ro', markersize=15)  # red circle for outputs

# Add labels and title
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Water Pipe Maze")

plt.show()
