import tkinter as tk
import tkinter.messagebox as messagebox

# Initialize the main application window
root = tk.Tk()
root.title("TIC-TAC-TOE")
root.geometry("320x350")

# Initialize game variables
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark = ''
count = 0
panels = ['panel', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Define winning patterns for the game
win_patterns = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]]

# Define a function to check for a win condition
def win(panels, current_mark):
    for pattern in win_patterns:
        if (panels[pattern[0]] == current_mark and 
            panels[pattern[1]] == current_mark and 
            panels[pattern[2]] == current_mark):
            return True
    return False

# Define a function to reset the game state
def reset_game():
    global count, mark, digits, panels
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mark = ''
    count = 0
    panels = ['panel', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Clear the board and make every square available for the new game.
    for button in buttons:
        button.config(text='', state=tk.NORMAL)

# Define a function to enable all buttons in the game
def enable_all_buttons():
    for btn in buttons:
        btn.config(text='', state=tk.NORMAL)

# Define a function to disable all buttons in the game
def disable_all_buttons():
    for btn in buttons:
        btn.config(state=tk.DISABLED)

# Central Checker Function
def checker(digit):
    global count, mark, digits, panels

    if digit in digits:
        digits.remove(digit)
        
        # Assign turn symbol based on count
        if count % 2 == 0:
            mark = 'X'
            panels[digit] = 'X'
        else:
            mark = 'O'
            panels[digit] = 'O'
            
        # Update button UI & disable clicked box
        buttons[digit - 1].config(text=mark, state=tk.DISABLED)
        
        # Increment move counter
        count += 1

        # Victory Check
        if win(panels, mark):
            winner = "Player 1 (X)" if mark == 'X' else "Player 2 (O)"
            messagebox.showinfo("Result", f"Congratulations! {winner} wins!")
            disable_all_buttons()
            return

        # Draw/Tie Check
        if count > 8:
            messagebox.showinfo("Result", "Match Tied!")
            disable_all_buttons()


# Create 3x3 Button Grid Layout
buttons = []
for i in range(1, 10):
    row = (i - 1) // 3
    col = (i - 1) % 3
    btn = tk.Button(
        root, 
        text='', 
        font=('Arial', 20, 'bold'), 
        width=5, 
        height=2,
        command=lambda d=i: checker(d)
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(btn)

# Reset / New Game Button
reset_btn = tk.Button(
    root, 
    text="Reset / New Game", 
    font=('Arial', 12, 'bold'), 
    command=reset_game
)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", padx=5, pady=10)

root.mainloop()


