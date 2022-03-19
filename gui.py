from tkinter import messagebox
from tkinter import *
from game import Connect4

window = Tk()
window.geometry("320x380")
window.title("Connect 4")
window.configure(background="#FFFFFF")

board = Text(window, bg="#FFFFFF", fg="#99C1B9", selectbackground="#99C1B9", padx=13, pady=6, font=("Ubuntu Mono", 25))


def update_board():
    board.delete("1.0", END)
    board.insert(END, game.get_grid())


def play_game(col):
    if game.game_over or game.check_free_space() == 0:
        answer = messagebox.askyesno(title="Game over", message="Do you want to start a new game?")
        if answer:
            start_game()
    elif game.get_amount_of_filled_cells(col) == 6:
        messagebox.showerror("Try again", "Column is full!")
    else:
        game.make_move(col)
        update_board()
        if game.check_match():
            game.game_over = True
            messagebox.showinfo("Winner", f"Player {game.player} wins!")
        else:
            game.pass_turn()


def start_game():
    global game
    game = Connect4()
    update_board()


game = None
start_game()

column1_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="↓", relief="groove", font=("Ubuntu Mono", 15),
                     command=lambda: play_game(0))
column2_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="↓", relief="groove", font=("Ubuntu Mono", 15),
                     command=lambda: play_game(1))
column3_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="↓", relief="groove", font=("Ubuntu Mono", 15),
                     command=lambda: play_game(2))
column4_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="↓", relief="groove", font=("Ubuntu Mono", 15),
                     command=lambda: play_game(3))
column5_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="↓", relief="groove", font=("Ubuntu Mono", 15),
                     command=lambda: play_game(4))
column6_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="↓", relief="groove", font=("Ubuntu Mono", 15),
                     command=lambda: play_game(5))
column7_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="↓", relief="groove", font=("Ubuntu Mono", 15),
                     command=lambda: play_game(6))
new_game_btn = Button(window, bg="#E8F3F1", fg="#344B47", text="NEW GAME", relief="groove", font=("Ubuntu Mono", 15),
                      command=start_game)

column1_btn.place(x=45, y=35, height=30, width=25)
column2_btn.place(x=79, y=35, height=30, width=25)
column3_btn.place(x=113, y=35, height=30, width=25)
column4_btn.place(x=147, y=35, height=30, width=25)
column5_btn.place(x=181, y=35, height=30, width=25)
column6_btn.place(x=215, y=35, height=30, width=25)
column7_btn.place(x=249, y=35, height=30, width=25)
board.place(x=35, y=75, height=225, width=250)
new_game_btn.place(x=35, y=310, height=35, width=250)

mainloop()
