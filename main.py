# pip install PyMySQL
# pip install tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


# connection for phpmyadmin
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Pratyush23!!',
        db='mydata',
    )
    return conn


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=10, column=0, columnspan=5, rowspan=13, padx=10, pady=20)


root = Tk()
root.title("Movie Database System")
root.geometry("1080x720")
root.configure(bg='tan1')
my_tree = ttk.Treeview(root)

# placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()


# placeholder set value function
def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)
    if num == 6:
        ph6.set(word)
    if num == 7:
        ph7.set(word)


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * fROM movies")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add():
    movid = str(movidEntry.get())
    movtitle = str(movtitleEntry.get())
    movyear = str(movyearEntry.get())
    movlang = str(movlangEntry.get())
    dirname = str(dirnameEntry.get())
    cast = str(castEntry.get())
    rating = str(ratingEntry.get())

    if (movid == "" or movid == " ") or (movtitle == "" or movtitle == " ") or (movyear == "" or movyear == " ") or (
            movlang == "" or movlang == " ") or (dirname == "" or dirname == " ") or (cast == "" or cast == " ") or (rating == "" or rating == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO movies VALUES ('" + movid + "','" + movtitle + "','" + movyear + "','" + movlang + "','" + dirname + "','" + cast + "','" + rating + "') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Movie ID already exist")
            refreshTable()

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision !="yes":
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE fROM movies")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()


def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE fROM movies WHERE movid='" + str(deleteData) + "'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()


def select():
    try:
        selected_item = my_tree.selection()[0]
        movid = str(my_tree.item(selected_item)['values'][0])
        movtitle = str(my_tree.item(selected_item)['values'][1])
        movyear = str(my_tree.item(selected_item)['values'][2])
        movlang = str(my_tree.item(selected_item)['values'][3])
        dirname = str(my_tree.item(selected_item)['values'][4])
        cast = str(my_tree.item(selected_item)['values'][5])
        rating = str(my_tree.item(selected_item)['values'][6])

        setph(movid, 1)
        setph(movtitle, 2)
        setph(movyear, 3)
        setph(movlang, 4)
        setph(dirname, 5)
        setph(cast, 6)
        setph(rating, 7)
    except:
        messagebox.showinfo("Error", "Please select a data row")


def search():
    movid = str(movidEntry.get())
    movtitle = str(movtitleEntry.get())
    movyear = str(movyearEntry.get())
    movlang = str(movlangEntry.get())
    dirname = str(dirnameEntry.get())
    cast = str(castEntry.get())
    rating = str(ratingEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * fROM movies WHERE movid='" +
                   movid + "' or movtitle='" +
                   movtitle + "' or movyear='" +
                   movyear + "' or movlang='" +
                   movlang + "' or dirname='" +
                   dirname + "' or cast='" +
                   cast + "' or rating='" +
                   rating + "' ")

    try:
        result = cursor.fetchall()

        for num in range(0, 7):
            setph(result[0][num], (num + 1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")


def update():
    selectedmovid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedmovid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    movid = str(movidEntry.get())
    movtitle = str(movtitleEntry.get())
    movyear = str(movyearEntry.get())
    movlang = str(movlangEntry.get())
    dirname = str(dirnameEntry.get())
    cast = str(castEntry.get())
    rating = str(ratingEntry.get())

    if (movid == "" or movid == " ") or (movtitle == "" or movtitle == " ") or (movyear == "" or movyear == " ") or (
            movlang == "" or movlang == " ") or (dirname == "" or dirname == " ") or (cast == "" or cast == " ") or (rating == "" or rating == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE movies SET movid='" +
                           movid + "', movtitle='" +
                           movtitle + "', movyear='" +
                           movyear + "', movlang='" +
                           movlang + "', dirname='" +
                           dirname + "', cast='" +
                           cast + "', rating='" +
                           rating + "' WHERE movid='" +
                           selectedmovid + "' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Movie ID already exist")
            return

    refreshTable()


label = Label(root, text="Movie Database System", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

movidLabel = Label(root, text="Movie ID", font=('Arial', 15))
movtitleLabel = Label(root, text="Title", font=('Arial', 15))
movyearLabel = Label(root, text="Year", font=('Arial', 15))
movlangLabel = Label(root, text="Language", font=('Arial', 15))
dirnameLabel = Label(root, text="Director", font=('Arial', 15))
castLabel = Label(root, text="Cast", font=('Arial', 15))
ratingLabel = Label(root, text="Rating", font=('Arial', 15))

movidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
movtitleLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
movyearLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
movlangLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
dirnameLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)
castLabel.grid(row=8, column=0, columnspan=1, padx=50, pady=5)
ratingLabel.grid(row=9, column=0, columnspan=1, padx=50, pady=5)

movidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph1)
movtitleEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph2)
movyearEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph3)
movlangEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph4)
dirnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)
castEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph6)
ratingEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph7)

movidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
movtitleEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
movyearEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
movlangEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
dirnameEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)
castEntry.grid(row=8, column=1, columnspan=4, padx=5, pady=0)
ratingEntry.grid(row=9, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84f894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8f8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg='red', command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#f4fE82", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#f398ff", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Movie ID", "Title", "Year", "Language", "Director", "Cast", "Rating")

my_tree.column("#0", width=0, stretch=YES)
my_tree.column("Movie ID", anchor=W, width=100)
my_tree.column("Title", anchor=W, width=200)
my_tree.column("Year", anchor=W, width=100)
my_tree.column("Language", anchor=W, width=140)
my_tree.column("Director", anchor=W, width=210)
my_tree.column("Cast", anchor=W, width=200)
my_tree.column("Rating", anchor=W, width=90)

my_tree.heading("Movie ID", text="Movie ID", anchor=W)
my_tree.heading("Title", text="Title", anchor=W)
my_tree.heading("Year", text="Year", anchor=W)
my_tree.heading("Language", text="Language", anchor=W)
my_tree.heading("Director", text="Director", anchor=W)
my_tree.heading("Cast", text="Cast", anchor=W)
my_tree.heading("Rating", text="Rating", anchor=W)

refreshTable()

root.mainloop()