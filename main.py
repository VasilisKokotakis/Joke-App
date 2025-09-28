import requests
import tkinter as tk
from tkinter import messagebox

def get_joke():
    try:
        joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        setup_label.config(text=joke["setup"])
        punchline_label.config(text="")
        punchline_label.after(5000, lambda: punchline_label.config(text=joke["punchline"]))
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch joke: {e}")

# GUI Setup
root = tk.Tk()
root.title("Daily Fun App")

setup_label = tk.Label(root, text="Click the button for a joke!", font=("Arial", 14), wraplength=400, justify="center")
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=400, justify="center")
punchline_label.pack(pady=20)

btn = tk.Button(root, text="Get Joke", command=get_joke, font=("Arial", 12))
btn.pack(pady=10)

root.mainloop()
