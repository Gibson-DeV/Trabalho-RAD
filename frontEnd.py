from tkinter import END, Button, Entry, Listbox, Scrollbar, StringVar

import customtkinter as ctk
from CTkListbox import CTkListbox

import backend as backend

# System, Dark, Light
ctk.set_appearance_mode("Dark")

mode = ctk.get_appearance_mode()

selected_tuple = None

def get_selected_row(selected_option):
    global selected_tuple
    selected_tuple = selected_option
    for index, value in enumerate(selected_option):
        if index > 0:
            entry = globals().get(f"e{index}")
            entry.delete(0, END)
            entry.insert(END, value)

def search_command():
    list1.delete("all")
    data = backend.select(task_name=row_title.get(), responsible=row_responsible.get())
    lenght = len(data)
    for index, row in enumerate(data):
        list1.insert(END if index == lenght else index, row)

def add_command(_):
    backend.insertData(task_name_col=row_title.get(), responsible_col=row_responsible.get(), status_col=row_status.get(), date_col=row_date.get())
    list1.delete("all")
    for row in backend.select():
        list1.insert(END, row)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def delete_command():
    backend.delete(selected_tuple[0])
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    search_command()


def update_command():
    backend.update(selected_tuple[0], task_name=row_title.get(), responsible=row_responsible.get(), status=row_status.get(), date=row_date.get())
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    search_command()


root = ctk.CTk()
root.title("**** TASKS LIST *****")
width = 630
height = 335

# coletando informações do monitor
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)

# tamanho da janela principal
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# Labels
l1 = ctk.CTkLabel(root, text="Tarefa")
l1.grid(row=0, column=0, pady=10, sticky="e")
l2 = ctk.CTkLabel(root, text="Responsável")
l2.grid(row=0, column=2, sticky="e")
l3 = ctk.CTkLabel(root, text="Status")
l3.grid(row=2, column=0, sticky="e")
l4 = ctk.CTkLabel(root, text="Data")
l4.grid(row=2, column=2, sticky="e")

# Entries
row_title = StringVar()
e1 = ctk.CTkEntry(root, 165, 24, textvariable=row_title, corner_radius=4, border_width=1)
e1.grid(row=0, column=1)
row_responsible = StringVar()
e2 = ctk.CTkEntry(root, 165, 24, textvariable=row_responsible, corner_radius=4, border_width=1)
e2.grid(row=0, column=3, padx=10, sticky="e")
row_status = StringVar()
e3 = ctk.CTkEntry(root, 165, 24, textvariable=row_status, corner_radius=4, border_width=1)
e3.grid(row=2, column=1)
row_date = StringVar()
e4 = ctk.CTkEntry(root, 165, 24, textvariable=row_date, corner_radius=4, border_width=1)
e4.grid(row=2, column=3, padx=10, sticky="e")

# Listbox
color = "#1b1f22" if mode == "Light" else "#fff"
list1 = CTkListbox(root, 220, 400, text_color=color, border_width=1)
list1.grid(columnspan=3, padx=10, pady=10)
list1.configure(command=get_selected_row)

# Buttons
b1 = ctk.CTkButton(root, 165, text="Incluir", corner_radius=1, fg_color="#198754", hover_color="#157347", text_color="#fff", command=add_command)
b1.grid(row=3, column=3, pady=10, sticky="n")

b2 = ctk.CTkButton(root, 165, text="Atualizar Selecionado", corner_radius=1, fg_color="#f8f9fa", hover_color="#d3d4d5", text_color="#494949", command=update_command)
b2.grid(row=3, column=3, pady=46, sticky="n")

b3 = ctk.CTkButton(root, 165, text="Exibir todos", corner_radius=1, fg_color="#f8f9fa", hover_color="#d3d4d5", text_color="#494949", command=search_command)
b3.grid(row=3, column=3, pady=82, sticky="n")

b4 = ctk.CTkButton(root, 165, text="Deletar Selecionado", corner_radius=1, fg_color="#dc3545", hover_color="#bb2d3b", text_color="#fff", command=delete_command)
b4.grid(row=3, column=3, pady=118, sticky="n")

b5_font = ctk.CTkFont(size=18)
b5 = ctk.CTkButton(root, 165, text="Fechar", corner_radius=1, fg_color="#6c757d", hover_color="#5c636a", text_color="#fff", font=b5_font, command=root.destroy)
b5.grid(row=3, column=3, pady=15, ipady=10, sticky="s")

root.mainloop()
