import tkinter as tk
from tkinter import messagebox

# Function to check for a winner
def check_winner():
    global board, current_player
    # Winning combinations
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
            return True

    # Check for a draw
    if all(cell != "" for cell in board):
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_board()
        return True

    return False

# Function to reset the board
def reset_board():
    global board, current_player
    for button in buttons:
        button.config(text="", state=tk.NORMAL)
    board = [""] * 9
    current_player = "X"

# Function to handle button clicks
def on_button_click(index):
    global board, current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, state=tk.DISABLED)

        if not check_winner():
            current_player = "O" if current_player == "X" else "X"  # Switch turns

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

board = [""] * 9
current_player = "X"

buttons = []

# Create the 3x3 grid of buttons
for i in range(9):
    button = tk.Button(root, text="", font=("Helvetica", 20), height=2, width=5,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Run the Tkinter main loop
root.mainloop()


