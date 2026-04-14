import json, re

header = """import json
try:
    with open("lang.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        LANG = config.get("lang", "hi")
except Exception:
    LANG = "hi"

def _(text):
    if LANG == "hi":
        translations = {
            "LOGIN": "लॉग इन",
            "Logout": "लॉग आउट",
            "Search": "खोजें",
            "Total": "कुल",
            "Generate": "जनरेट",
            "Clear": "साफ करें",
            "Exit": "बाहर निकलें",
            "Are you sure you want to exit?": "क्या आप वाकई बाहर निकलना चाहते हैं?",
            "Add To Cart": "कार्ट में डालें",
            "Remove": "हटाएं",
            "The login is successful": "लॉगिन सफल रहा",
            "The login is successful.": "लॉगिन सफल रहा।",
            "Incorrect username or password.": "गलत यूज़र नेम या पासवर्ड।",
            "Are you sure you want to logout?": "क्या आप वाकई लॉग आउट करना चाहते हैं?",
            "Login Page": "लॉगिन पेज",
            "Login": "लॉगिन",
            "Error": "त्रुटि",
            "Oops!": "उफ़!",
            "Oops!!": "उफ़!!",
            "Success!!": "सफलता!!",
            "Bill Generated": "बिल जनरेट किया गया",
            "Inventory": "इन्वेंटरी",
            "Employees": "कर्मचारी",
            "Invoices": "चालान (इनवॉइस)",
            "About Us": "हमारे बारे में",
            "ADD PRODUCT": "उत्पाद जोड़ें",
            "UPDATE PRODUCT": "उत्पाद अपडेट करें",
            "DELETE PRODUCT": "उत्पाद हटाएं",
            "ADD": "जोड़ें",
            "UPDATE": "अपडेट करें",
            "Retail Management System": "रिटेल मैनेजमेंट सिस्टम",
            "Confirm": "पुष्टि करें",
        }
        return translations.get(text, text)
    return text
"""

for fn in ["employee.py", "admin.py"]:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Check if already translated to avoid double translations
    if "def _(text):" not in text:
        text = text.replace('from tkinter import scrolledtext as tkst', 'from tkinter import scrolledtext as tkst\n' + header)
        
        # Translate button text attrs format """TEXT"""
        text = re.sub(r'text="""([^"]+)"""', r'text=_("""\1""")', text)
        
        # Translate Label simple text formatting text="TEXT"
        text = re.sub(r'text="([^"]+)"', lambda m: f'text=_("{m.group(1)}")' if not m.group(1).startswith("In Stock:") else m.group(0), text)
        
        # Translate messagebox texts
        for msg_type in ['askyesno', 'showinfo', 'showerror']:
            text = re.sub(r'messagebox\.' + msg_type + r'\("([^"]+)",\s*"([^"]+)"([^)]*)\)', 
                           r'messagebox.' + msg_type + r'(_("\1"), _("\2")\3)', text)
        
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(text)

print("Translation strings successfully injected.")
