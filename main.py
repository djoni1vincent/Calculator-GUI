import tkinter 

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) # 5
column_count = len(button_values[0]) # 4

warm_beige = "#EBD5AB" # Main body/casing
avocado_green = "#658C58" # Function keys, accents, display background
burnt_orange = "#E67E22" # Accent color for "equals" button
coffee_brown = "#5B532C" # Text, primary symbols, outline

# window setup

window = tkinter.Tk() # create the window
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 48), background=warm_beige,
                      foreground=coffee_brown,)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial, 30"),
                                width=column_count - 1, height=1,
                                command=lambda value=value:button_clicked(value))
        button.grid(row=row+1, column=column)


frame.pack()

def button_clicked (value):
    pass

window.mainloop()