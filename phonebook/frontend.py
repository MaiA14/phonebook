"""
A program that stores
Names, Surnames, Addresss, phones

User can:
View all records
Search an entry
Update entry
delete
close
"""

from tkinter import *
from backend import Database

database=Database("books.db")

def get_selected_row(event):
        try:
            global selected_tuple
            index=list1.curselection()
            selected_tuple=list1.get(index)
        except IndexError:
            pass


def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(Name_text.get(),Surname_text.get(),Address_text.get(),Phone_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(Name_text.get(),Surname_text.get(),Address_text.get(),Phone_text.get())
    list1.delete(0,END)
    list1.insert(END,(Name_text.get(),Surname_text.get(),Address_text.get(),Phone_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],Name_text.get(),Surname_text.get(),Address_text.get(),Phone_text.get())



window=Tk()

window.wm_title("Phonebook")

l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="Surname")
l2.grid(row=0,column=2)

l3=Label(window,text="Address")
l3.grid(row=1,column=0)

l4=Label(window,text="Phone")
l4.grid(row=1,column=2)

Name_text=StringVar()
e1=Entry(window,textvariable=Name_text)
e1.grid(row=0,column=1)

Surname_text=StringVar()
e2=Entry(window,textvariable=Surname_text)
e2.grid(row=0,column=3)

Address_text=StringVar()
e3=Entry(window,textvariable=Address_text)
e3.grid(row=1,column=1)

Phone_text=StringVar()
e4=Entry(window,textvariable=Phone_text)
e4.grid(row=1,column=3)

list1=Listbox(window, heigh=6,width=35, selectmode=MULTIPLE)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure()
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
