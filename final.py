# Step 1: Import the necessary libraries
import tkinter as tk
from tkinter import messagebox

# Step 2: Create a Tkinter window with the title "TIC-TAC-TOE"
root = tk.Tk()
root.title("TIC-TAC-TOE")

# Step 3: List of numbers 1 to 9 representing the available board positions
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Step 4: Initialize the mark variable (holds current player's symbol, X or O)
mark = ''

# Step 5: Track the number of moves made so far
count = 0

# Step 6: List of 10 elements - index 0 is an unused placeholder so that
# panels[1] through panels[9] line up with the board positions 1-9
panels = ['panel', '', '', '', '', '', '', '', '', '']


# --- Supporting pieces needed by checker() ---------------------------------
# The checker() function below refers to button1..button9 and a win()
# function, so both are defined here first.

def win(mark):
    """Return True if the given mark ('X' or 'O') occupies a winning line."""
    combos = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),   # rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),   # columns
        (1, 5, 9), (3, 5, 7),              # diagonals
    ]
    for a, b, c in combos:
        if panels[a] == panels[b] == panels[c] == mark:
            return True
    return False


# Step 1: Define the checker function with a single parameter, digit
def checker(digit):
    # Step 2: Declare count, mark, and digits as global variables
    global count, mark, digits

    # Step 3 & 4: Handle digit 1 - check the condition and that it's still available
    if digit == 1 and 1 in digits:
        # Step 5: Remove the digit from the digits list
        digits.remove(1)
        # Step 6: Determine the current player's mark based on count (even/odd)
        mark = 'X' if count % 2 == 0 else 'O'
        # Step 7: Update the corresponding button with the current mark
        button1.config(text=mark)
        panels[1] = mark
        # Step 8: Increment the count of moves made
        count += 1
        # Step 9 & 10: Check for a win and announce the winner if found
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Step 11: Repeat steps 3-10 for digit 2
    if digit == 2 and 2 in digits:
        digits.remove(2)
        mark = 'X' if count % 2 == 0 else 'O'
        button2.config(text=mark)
        panels[2] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Repeat for digit 3
    if digit == 3 and 3 in digits:
        digits.remove(3)
        mark = 'X' if count % 2 == 0 else 'O'
        button3.config(text=mark)
        panels[3] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Repeat for digit 4
    if digit == 4 and 4 in digits:
        digits.remove(4)
        mark = 'X' if count % 2 == 0 else 'O'
        button4.config(text=mark)
        panels[4] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Repeat for digit 5
    if digit == 5 and 5 in digits:
        digits.remove(5)
        mark = 'X' if count % 2 == 0 else 'O'
        button5.config(text=mark)
        panels[5] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Repeat for digit 6
    if digit == 6 and 6 in digits:
        digits.remove(6)
        mark = 'X' if count % 2 == 0 else 'O'
        button6.config(text=mark)
        panels[6] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Repeat for digit 7
    if digit == 7 and 7 in digits:
        digits.remove(7)
        mark = 'X' if count % 2 == 0 else 'O'
        button7.config(text=mark)
        panels[7] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Repeat for digit 8
    if digit == 8 and 8 in digits:
        digits.remove(8)
        mark = 'X' if count % 2 == 0 else 'O'
        button8.config(text=mark)
        panels[8] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Repeat for digit 9
    if digit == 9 and 9 in digits:
        digits.remove(9)
        mark = 'X' if count % 2 == 0 else 'O'
        button9.config(text=mark)
        panels[9] = mark
        count += 1
        if win(mark) and mark == 'X':
            messagebox.showinfo("Game Over", "Player1 wins")
            root.destroy()
        elif win(mark) and mark == 'O':
            messagebox.showinfo("Game Over", "Player2 wins")
            root.destroy()

    # Step 12 & 13: Check for a tie - all 9 moves made and nobody has won
    if count > 8 and not win('X') and not win('O'):
        messagebox.showinfo("Game Over", "Match Tied")
        root.destroy()


# --- Step 1: Labels displaying the players' symbols ------------------------
label1 = tk.Label(root, text="Player1 : X", font=('Arial', 12, 'bold'), fg='blue')
label1.grid(row=3, column=0, columnspan=2)

label2 = tk.Label(root, text="Player2 : O", font=('Arial', 12, 'bold'), fg='red')
label2.grid(row=3, column=1, columnspan=2)

# --- Step 2: Board buttons (checker() from Step 3 updates these) -----------
button1 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(1))
button1.grid(row=0, column=0)

button2 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(2))
button2.grid(row=0, column=1)

button3 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(3))
button3.grid(row=0, column=2)

button4 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(4))
button4.grid(row=1, column=0)

button5 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(5))
button5.grid(row=1, column=1)

button6 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(6))
button6.grid(row=1, column=2)

button7 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(7))
button7.grid(row=2, column=0)

button8 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(8))
button8.grid(row=2, column=1)

button9 = tk.Button(root, text='', width=10, height=4, command=lambda: checker(9))
button9.grid(row=2, column=2)

# --- Step 5: Run the app to test it out -------------------------------------
root.mainloop()
