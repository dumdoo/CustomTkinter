import tkinter
import customtkinter

# customtkinter.DrawEngine.preferred_drawing_method = "font_shapes"


def to_scollbar(*args, **kwargs):
    tk_textbox_scrollbar.set(*args, **kwargs)
    ctk_textbox_scrollbar.set(*args, **kwargs)
    ctk_textbox_scrollbar.update_idletasks()
    tk_textbox_scrollbar.update_idletasks()
    print("to_scollbar:", args, **kwargs)


def from_scrollbar(*args, **kwargs):
    tk_textbox.yview(*args, **kwargs)
    print("from_scrollbar:", args, **kwargs)


app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

tk_textbox = tkinter.Text(app)
tk_textbox.grid(row=0, column=0, sticky="nsew")

ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app, command=from_scrollbar, fg_color="red")
ctk_textbox_scrollbar.grid(row=0, column=1, padx=0, sticky="ns")

tk_textbox_scrollbar = tkinter.Scrollbar(app, command=from_scrollbar)
tk_textbox_scrollbar.grid(row=0, column=2, padx=1, sticky="ns")

tk_textbox.configure(yscrollcommand=to_scollbar)

tk_textbox.insert("insert", "\n".join([str(i) for i in range(100)]))

app.mainloop()