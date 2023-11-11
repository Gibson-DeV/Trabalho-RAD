import sqlite3

# Create a database "RAD.db", tables if not exist and connect to database.
def connectDb():
    db = sqlite3.connect("RAD.db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks_tb(id INTEGER PRIMARY KEY, task_name_col text, responsible_col text, status_col text, date_col text)")
    db.commit()
    db.close()

#Insert data in table task_tb
def insertData(task_name_col, responsible_col, status_col, date_col):
    connectDb = sqlite3.connect("RAD.DB")
    cursor = connectDb.cursor()
    cursor.execute("INSERT INTO tasks_tb VALUES(NULL,?,?,?,?)",(task_name_col,responsible_col, status_col, date_col))
    connectDb.commit()
    connectDb.close()

#Find for task_name and responsible
def select(task_name=None, responsible=None):
    connectDb = sqlite3.connect("RAD.db")
    cursor = connectDb.cursor()

    if not task_name:
        task_name = None

    if not responsible:
        responsible = None

    query = "SELECT * FROM tasks_tb"
    parameters = []

    if task_name or responsible:
        query += " WHERE"

    if task_name is not None:
        query += " task_name_col = ?"
        parameters.append(task_name)

    if responsible is not None:
        if task_name is not None:
            query += " OR"

        query += " responsible_col = ?"
        parameters.append(responsible)

    cursor.execute(query, tuple(parameters))

    #Recover all rows
    allRows = cursor.fetchall()
    connectDb.close()
    return allRows

#Delete task for id
def delete(id):
    connectDb = sqlite3.connect("RAD.DB")
    cursor = connectDb.cursor()
    cursor.execute("DELETE FROM tasks_tb WHERE id=?",(id,))
    connectDb.commit()
    connectDb.close()

#update data in table task_tb
def update(id, task_name, responsible, status, date):
    connectDb = sqlite3.connect("RAD.db")
    cursor = connectDb.cursor()
    cursor.execute("UPDATE tasks_tb SET task_name_col=?, responsible_col=?, status_col=?,date_col=? WHERE id=?",
                   (task_name,responsible,status,date,id))
    connectDb.commit()
    connectDb.close()

#Call function connectDb
connectDb()






