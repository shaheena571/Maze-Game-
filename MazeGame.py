import tkinter as tk
import time

# Maze configuration (1 = path, 0 = wall)
MAZE = [
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1]
]

ROWS = len(MAZE)
COLS = len(MAZE[0])
CELL_SIZE = 60
DELAY = 0.25  # Animation delay in seconds


class MazeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Escape Game - Backtracking Visualization")
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Start Solving", command=self.start_solving,
                                      bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
        self.start_button.pack(pady=10)

        self.draw_maze()

    def draw_maze(self):
        """Draws the maze grid on canvas"""
        for i in range(ROWS):
            for j in range(COLS):
                color = "white" if MAZE[i][j] == 1 else "black"
                self.canvas.create_rectangle(
                    j * CELL_SIZE, i * CELL_SIZE,
                    (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE,
                    fill=color, outline="gray"
                )

    def color_cell(self, i, j, color):
        """Colors a specific cell"""
        self.canvas.create_rectangle(
            j * CELL_SIZE, i * CELL_SIZE,
            (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE,
            fill=color, outline="gray"
        )
        self.root.update()
        time.sleep(DELAY)

    def start_solving(self):
        """Starts maze solving process"""
        self.start_button.config(state="disabled")
        path = [[0] * COLS for _ in range(ROWS)]
        if self.solve_maze(0, 0, path):
            print("Maze Solved!")
        else:
            print("No Path Found!")
        self.start_button.config(state="normal")

    def is_safe(self, x, y):
        """Checks if current move is within bounds and valid"""
        return 0 <= x < ROWS and 0 <= y < COLS and MAZE[x][y] == 1

    def solve_maze(self, x, y, path):
        """Backtracking algorithm to solve maze"""
        # Goal condition: reached bottom-right corner
        if x == ROWS - 1 and y == COLS - 1:
            self.color_cell(x, y, "green")
            return True

        if self.is_safe(x, y) and path[x][y] == 0:
            # Mark cell as part of path
            path[x][y] = 1
            self.color_cell(x, y, "skyblue")

            # Move in 4 directions: down, right, up, left
            moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for move_x, move_y in moves:
                new_x, new_y = x + move_x, y + move_y
                if self.solve_maze(new_x, new_y, path):
                    return True

            # Backtrack
            self.color_cell(x, y, "red")
            path[x][y] = 0

        return False


if __name__ == "__main__":
    root = tk.Tk()
    app = MazeGUI(root)
    root.mainloop()
