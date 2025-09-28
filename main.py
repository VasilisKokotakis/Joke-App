import tkinter as tk
import requests

def get_joke():
    try:
        # Fetch a random joke
        joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        setup_label.config(text=joke["setup"])
        punchline_label.config(text="")  # Clear old punchline
        # Reveal punchline after 5 seconds
        punchline_label.after(5000, lambda: punchline_label.config(text=joke["punchline"]))
    except Exception as e:
        setup_label.config(text="Oops! Could not fetch a joke 😢")
        punchline_label.config(text=str(e))

# --- UI Setup ---
root = tk.Tk()
root.title("😂 Daily Joke App")
root.geometry("500x300")
root.config(bg="#f4f4f9")

title_label = tk.Label(root, text="Daily Fun App", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
title_label.pack(pady=10)

setup_label = tk.Label(root, text="Click the button to get a joke!", font=("Arial", 14), wraplength=450, bg="#f4f4f9")
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="#666", wraplength=450, bg="#f4f4f9")
punchline_label.pack(pady=20)

btn = tk.Button(root, text="Get Joke", command=get_joke, font=("Arial", 12), bg="#007BFF", fg="white")
btn.pack(pady=10)

root.mainloop()