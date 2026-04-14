__author__ = "macaw"
import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("Big Bazaar")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()

def show_help():
    help_window = Toplevel(main)
    help_window.geometry("600x400")
    help_window.title("Application Help & Tutorial")
    help_window.resizable(0, 0)
    help_window.configure(bg="#ffffff")
    
    title_lbl = Label(help_window, text="Welcome to Big Bazaar System!", font=("Helvetica", 16, "bold"), bg="#ffffff", fg="#D2463E")
    title_lbl.pack(pady=20)
    
    text_content = """This application allows you to manage the retail store easily.

1. Employee Mode: 
Allows cashiers to bill items to customers, search for products
in the inventory, and generate invoices.

2. Admin Mode:
Allows the store manager to manage the inventory (Add/Update/Delete products),
manage employee details and accounts, and view all system invoices.

To begin, click on either Employee or Admin from the main menu, 
and login using your credentials."""
    
    info_lbl = Label(help_window, text=text_content, font=("Helvetica", 12), bg="#ffffff", fg="#333333", justify=LEFT)
    info_lbl.pack(padx=20, pady=10, fill=BOTH, expand=True)
    
    close_btn = Button(help_window, text="Close", font=("Helvetica", 12, "bold"), bg="#D2463E", fg="white", relief="flat", cursor="hand2", command=help_window.destroy)
    close_btn.pack(pady=20, ipadx=30, ipady=5)

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

button3 = Button(main)
button3.place(relx=0.85, rely=0.05, width=150, height=40)
button3.configure(relief="flat", overrelief="flat", activebackground="#D2463E")
button3.configure(cursor="hand2", foreground="#ffffff", background="#D2463E")
button3.configure(font="-family {Helvetica} -size 12 -weight bold")
button3.configure(borderwidth="0", text="Help / Tutorial")
button3.configure(command=show_help)

main.mainloop()
