from tkinter import END, Tk, Label, StringVar, Entry, Listbox, Scrollbar, Button
import backend as backend

selected_tuple = None

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def search_command():
    list1.delete(0, END)
    for row in backend.select(task_name=row_title.get(), responsible=row_responsible.get()):
        list1.insert(END, row)

def add_command():
    backend.insertData(taskt_name_col=row_title.get(), responsible_col=row_responsible.get(), status_col=row_status.get(), date_col=row_date.get())
    list1.delete(0, END)
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
   

def update_command():
    backend.update(selected_tuple[0], task_name=row_title.get(), responsible=row_responsible.get(), status=row_status.get(), date=row_date.get())
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
   

root = Tk()
root.title("**** TASKS LIST *****")
width = 840
height = 260

# coletando informações do monitor
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)

# tamanho da janela principal
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg='#91a38f')

l1 = Label(root, text="Tarefa", bg='#91a38f', fg='#6006ff')
l1.grid(row=0, column=0)
l2 = Label(root, text="Responsável", bg='#91a38f', fg='#6006ff')
l2.grid(row=0, column=2)
l3 = Label(root, text="Status", bg='#91a38f', fg='#6006ff')
l3.grid(row=2, column=0)
l4 = Label(root, text="Data", bg='#91a38f', fg='#6006ff')
l4.grid(row=2, column=2)

row_title = StringVar()
e1 = Entry(root, textvariable=row_title)
e1.grid(row=0, column=1)
row_responsible = StringVar()
e2 = Entry(root, textvariable=row_responsible)
e2.grid(row=0, column=3)
row_status = StringVar()
e3 = Entry(root, textvariable=row_status)
e3.grid(row=2, column=1)
row_date = StringVar()
e4 = Entry(root, textvariable=row_date)
e4.grid(row=2, column=3)

list1 = Listbox(root, height=8, width=55)
list1.grid(row=6, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(root)
sb1.grid(row=6, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(root, text="Exibir todos", width=22,
            bg="snow", command=search_command)
b1.grid(row=6, column=4)

b3 = Button(root, text="Incluir", width=22, bg="royal blue1", command=add_command)
b3.grid(row=5, column=4)

b4 = Button(root, text="Atualizar Selecionado",
            width=22, bg="snow", command=update_command)
b4.grid(row=5, column=5)

b5 = Button(root, text="Deletar Selecionado",
            bg="firebrick4", width=22, command=delete_command)
b5.grid(row=6, column=5)

b6 = Button(root, text="Fechar", width=22, bg="red", command=root.destroy)
b6.grid(row=8, column=5)

root.mainloop()
