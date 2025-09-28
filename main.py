import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

current_joke = {"setup": "", "punchline": ""}  # To store the current joke

def get_joke():
    global current_joke
    try:
        joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        current_joke = joke
        setup_label.config(text=joke["setup"])
        punchline_label.config(text="")
        # Reveal punchline after 5 seconds
        punchline_label.after(5000, lambda: punchline_label.config(text=joke["punchline"]))
    except Exception as e:
        setup_label.config(text="Oops! Could not fetch a joke 😢")
        punchline_label.config(text=str(e))

def save_joke():
    if current_joke["setup"] and current_joke["punchline"]:
        with open("saved_jokes.txt", "a", encoding="utf-8") as f:
            f.write(f"{current_joke['setup']} - {current_joke['punchline']}\n")
        status_label.config(text="✅ Joke saved!", foreground="green")
    else:
        status_label.config(text="⚠️ No joke to save.", foreground="red")

# --- UI Setup ---
root = ttk.Window(themename="cosmo")  # modern theme, try "flatly", "cyborg", "minty", etc.
root.title("😂 Daily Joke App")
root.geometry("500x350")

title_label = ttk.Label(root, text="Daily Fun App", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

setup_label = ttk.Label(root, text="Click the button to get a joke!", font=("Arial", 14), wraplength=450)
setup_label.pack(pady=20)

punchline_label = ttk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=450, foreground="#666")
punchline_label.pack(pady=20)

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

btn_get = ttk.Button(btn_frame, text="Get Joke", command=get_joke, bootstyle=PRIMARY)
btn_get.grid(row=0, column=0, padx=10)

btn_save = ttk.Button(btn_frame, text="Save Joke", command=save_joke, bootstyle=SUCCESS)
btn_save.grid(row=0, column=1, padx=10)

status_label = ttk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

root.mainloop()
