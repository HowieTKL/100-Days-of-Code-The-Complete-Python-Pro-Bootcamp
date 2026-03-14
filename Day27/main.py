import tkinter as tk

FONT=("Courier New", 12)

my_window = tk.Tk()
my_window.title("Mile to Km Converter")
my_window.minsize(400, 300)
my_window.config(padx=20, pady=20)

my_entry = tk.Entry(my_window, width=7, font=FONT)
my_entry.grid(column=1, row=0)

miles_label = tk.Label(my_window, text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to_label = tk.Label(my_window, text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)
distance_label = tk.Label(my_window, text="xxx", font=FONT)
distance_label.grid(column=1, row=1)

km_label = tk.Label(my_window, text="Km", font=FONT)
km_label.grid(column=2, row=1)

def button_clicked():
    distance_label.config(text=format(float(my_entry.get()) * 1.6, ".2f"), font=FONT)
my_button = tk.Button(my_window, text="Calculate", font=FONT, command=button_clicked)
my_button.grid(column=1, row=3)


my_window.mainloop()
