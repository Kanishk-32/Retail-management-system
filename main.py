__author__ = "macaw"
import os
import json
from tkinter import *
from tkinter import messagebox

# ================== LANGUAGE CONFIG ===================
try:
    with open("lang.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        LANG = config.get("lang", "hi")
except Exception:
    LANG = "hi"

def _(text):
    if LANG == "hi":
        translations = {
            "Help / Tutorial": "सहायता / ट्यूटोरियल",
            "Exit": "बाहर निकलें",
            "Are you sure you want to exit?": "क्या आप वाकई बाहर निकलना चाहते हैं?",
            "Application Help & Tutorial": "एप्लिकेशन सहायता और ट्यूटोरियल",
            "Welcome to Retail System!": "रिटेल सिस्टम में आपका स्वागत है!",
            "Close": "बंद करें"
        }
        if text.startswith("This application"):
            return """यह एप्लिकेशन आपको स्टोर को आसानी से प्रबंधित करने की अनुमति देता है।

1. कर्मचारी मोड (Employee Mode):
कैशियर को ग्राहकों को बिल बनाने, इन्वेंट्री में उत्पादों की 
खोज करने और रसीद (इनवॉइस) जनरेट करने की अनुमति देता है।

2. एडमिन मोड (Admin Mode):
स्टोर मैनेजर को इन्वेंट्री (उत्पाद जोड़ने/अपडेट करने/हटाने),
कर्मचारी खातों को प्रबंधित करने, और सभी सिस्टम रसीद 
देखने की अनुमति देता है।

शुरू करने के लिए, मुख्य मेनू से कर्मचारी या एडमिन पर क्लिक करें, 
और अपने लॉगिन का उपयोग करें।"""
        return translations.get(text, text)
    return text

def toggle_lang():
    global LANG
    LANG = "hi" if LANG == "en" else "en"
    with open("lang.json", "w", encoding="utf-8") as f:
        json.dump({"lang": LANG}, f)
    # Refresh visible labels
    button3.configure(text=_("Help / Tutorial"))

# ======================================================

main = Tk()
main.geometry("1366x768")
main.title("Big Bazaar")
main.resizable(0, 0)

def Exit():
    sure = messagebox.askyesno(_("Exit"), _("Are you sure you want to exit?"), parent=main)
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
    help_window.title(_("Application Help & Tutorial"))
    help_window.resizable(0, 0)
    help_window.configure(bg="#ffffff")
    
    title_lbl = Label(help_window, text=_("Welcome to Retail System!"), font=("Helvetica", 16, "bold"), bg="#ffffff", fg="#D2463E")
    title_lbl.pack(pady=20)
    
    text_content = _("""This application allows you to manage the retail store easily.

1. Employee Mode: 
Allows cashiers to bill items to customers, search for products
in the inventory, and generate invoices.

2. Admin Mode:
Allows the store manager to manage the inventory (Add/Update/Delete products),
manage employee details and accounts, and view all system invoices.

To begin, click on either Employee or Admin from the main menu, 
and login using your credentials.""")
    
    info_lbl = Label(help_window, text=text_content, font=("Helvetica", 12), bg="#ffffff", fg="#333333", justify=LEFT)
    info_lbl.pack(padx=20, pady=10, fill=BOTH, expand=True)
    
    close_btn = Button(help_window, text=_("Close"), font=("Helvetica", 12, "bold"), bg="#D2463E", fg="white", relief="flat", cursor="hand2", command=help_window.destroy)
    close_btn.pack(pady=20, ipadx=30, ipady=5)

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=90)
button1.configure(relief="flat", overrelief="flat", activebackground="#ffffff")
button1.configure(cursor="hand2", foreground="#ffffff", background="#ffffff", borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2, command=emp)

button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=90)
button2.configure(relief="flat", overrelief="flat", activebackground="#ffffff")
button2.configure(cursor="hand2", foreground="#ffffff", background="#ffffff", borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3, command=adm)

button3 = Button(main)
button3.place(relx=0.85, rely=0.05, width=150, height=40)
button3.configure(relief="flat", overrelief="flat", activebackground="#D2463E")
button3.configure(cursor="hand2", foreground="#ffffff", background="#D2463E")
button3.configure(font="-family {Helvetica} -size 12 -weight bold")
button3.configure(borderwidth="0", text=_("Help / Tutorial"), command=show_help)

lang_btn = Button(main)
lang_btn.place(relx=0.03, rely=0.05, width=150, height=40)
lang_btn.configure(relief="flat", overrelief="flat", activebackground="#D2463E")
lang_btn.configure(cursor="hand2", foreground="#ffffff", background="#333333")
lang_btn.configure(font="-family {Helvetica} -size 12 -weight bold")
lang_btn.configure(borderwidth="0", text="English / हिंदी", command=toggle_lang)

main.mainloop()
