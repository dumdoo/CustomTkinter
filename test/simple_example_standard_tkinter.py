import tkinter
import tkinter.ttk as ttk

app = tkinter.Tk()
app.geometry("400x300")
app.title("Standard Tkinter Test")


def button_function():
    print("button pressed")


def slider_function(value):
    progressbar_1["value"] = value


y_padding = 6

frame_1 = tkinter.Frame(master=app, width=300, height=260, bg="lightgray")
frame_1.pack(padx=60, pady=20, fill="both", expand=True)

label_1 = tkinter.Label(master=frame_1, text="Label", bg="lightgray")
label_1.pack(pady=y_padding, padx=10)

progressbar_1 = ttk.Progressbar(master=frame_1,style='black.Horizontal.TProgressbar', length=150)
progressbar_1.pack(pady=y_padding, padx=10)
progressbar_1["value"] = 50

button_1 = tkinter.Button(master=frame_1, command=button_function, text="Button", highlightbackground="lightgray")
button_1.pack(pady=y_padding, padx=10)

slider_1 = tkinter.Scale(master=frame_1, command=slider_function, orient="horizontal", bg="lightgray", length=150)
slider_1.pack(pady=y_padding, padx=10)

entry_1 = tkinter.Entry(master=frame_1, highlightbackground="lightgray", width=10)
entry_1.pack(pady=y_padding, padx=10)

checkbox_1 = tkinter.Checkbutton(master=frame_1, bg=frame_1.cget("bg"), text="CheckButton")
checkbox_1.pack(pady=y_padding, padx=10)

app.mainloop()
