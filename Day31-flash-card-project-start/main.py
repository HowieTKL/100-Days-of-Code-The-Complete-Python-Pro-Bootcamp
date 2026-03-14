import random
import tkinter as tk
import pandas as p

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = p.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = p.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
word_pair = {}
flip_timer = None

def remove():
    global to_learn, word_pair
    try:
        to_learn.remove(word_pair)
    except ValueError:
        pass
    else:
        # p.DataFrame.from_records(to_learn).to_csv("data/words_to_learn.csv", index=False)
        p.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    random_fr_word()

def random_fr_word():
    global word_pair, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    word_pair = random.choice(to_learn)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word_pair["French"], fill="black")
    flip_timer = window.after(3000, func=show_en_word)

def show_en_word():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="yellow")
    canvas.itemconfig(card_word, text=word_pair["English"], fill="yellow")

window = tk.Tk()
window.title("My Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

no_image = tk.PhotoImage(file="images/wrong.png")
no_button = tk.Button(image=no_image, command=random_fr_word, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
no_button.grid(row=1, column=0)

yes_image = tk.PhotoImage(file="images/right.png")
yes_button = tk.Button(image=yes_image, command=remove, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
yes_button.grid(row=1, column=1)

window.mainloop()
