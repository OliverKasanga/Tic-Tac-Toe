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

# Define winning patterns
win_patterns = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


# Check for a winner
def win(panels, current_mark):
    for pattern in win_patterns:
        if (panels[pattern[0]] == current_mark and
            panels[pattern[1]] == current_mark and
            panels[pattern[2]] == current_mark):
            return True

    return False


# Reset the game
def reset_game():
    global count, mark, digits, panels

    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mark = ''
    count = 0
    panels = ['panel', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Clear all buttons
    for button in buttons:
        button.config(
            text='', state=tk.NORMAL)


# Ask the player whether to continue
def game_finished(message):
    answer = messagebox.askyesno("Game Finished", message + "\n\nWould you like to play again?")

    if answer:
        reset_game()
    else:
        root.destroy()


# Disable all buttons
def disable_all_buttons():
    for btn in buttons:
        btn.config(state=tk.DISABLED)


# Main checker function
def checker(digit):
    global count, mark, digits, panels

    if digit in digits:

        # Remove selected position
        digits.remove(digit)

        # Determine player
        if count % 2 == 0:
            mark = 'X'
            panels[digit] = 'X'
        else:
            mark = 'O'
            panels[digit] = 'O'

        # Change button appearance
        if mark == 'X':
            buttons[digit - 1].config(text='X')
        else:
            buttons[digit - 1].config(text='O')

        # Disable selected button
        buttons[digit - 1].config(state=tk.DISABLED)

        # Increase move count
        count += 1

        # Check for winner
        if win(panels, mark):

            if mark == 'X':
                winner = "Player 1 (X)"
            else:
                winner = "Player 2 (O)"

            disable_all_buttons()

            game_finished(
                "Congratulations!\n" + winner + " wins!"
            )

            return

        # Check for tie
        if count == 9:

            disable_all_buttons()

            game_finished("Match Tied!")

            return


# Create 3x3 button grid
buttons = []

for i in range(1, 10):

    row = (i - 1) // 3
    col = (i - 1) % 3

    btn = tk.Button(
        root, text='',
        font=('Arial', 20, 'bold'),
        width=5, height=2, relief=tk.RAISED, borderwidth=3, command=lambda d=i: checker(d))

    btn.grid(row=row, column=col, padx=5, pady=5)

    buttons.append(btn)


# Reset / New Game button
reset_btn = tk.Button(root, text="RESET / NEW GAME", command=reset_game)

reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", padx=5, pady=10)


# Start the application
root.mainloop()