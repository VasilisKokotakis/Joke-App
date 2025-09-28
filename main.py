import tkinter as tk
import requests

current_joke = {"setup": "", "punchline": ""}  # To store the current joke

def get_joke():
    global current_joke
    try:
        # Fetch a random joke
        joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        current_joke = joke  # Save it for later use
        setup_label.config(text=joke["setup"])
        punchline_label.config(text="")  # Clear old punchline
        # Reveal punchline after 5 seconds
        punchline_label.after(5000, lambda: punchline_label.config(text=joke["punchline"]))
    except Exception as e:
        setup_label.config(text="Oops! Could not fetch a joke 😢")
        punchline_label.config(text=str(e))

def save_joke():
    if current_joke["setup"] and current_joke["punchline"]:
        with open("saved_jokes.txt", "a", encoding="utf-8") as f:
            f.write(f"{current_joke['setup']} - {current_joke['punchline']}\n")
        status_label.config(text="✅ Joke saved!", fg="green")
    else:
        status_label.config(text="⚠️ No joke to save.", fg="red")

# --- UI Setup ---
root = tk.Tk()
root.title("😂 Daily Joke App")
root.geometry("500x350")
root.config(bg="#f4f4f9")

title_label = tk.Label(root, text="Daily Fun App", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
title_label.pack(pady=10)

setup_label = tk.Label(root, text="Click the button to get a joke!", font=("Arial", 14), wraplength=450, bg="#f4f4f9")
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="#666", wraplength=450, bg="#f4f4f9")
punchline_label.pack(pady=20)

btn_frame = tk.Frame(root, bg="#f4f4f9")
btn_frame.pack(pady=10)

btn_get = tk.Button(btn_frame, text="Get Joke", command=get_joke, font=("Arial", 12), bg="#007BFF", fg="white")
btn_get.grid(row=0, column=0, padx=10)

btn_save = tk.Button(btn_frame, text="Save Joke", command=save_joke, font=("Arial", 12), bg="#28a745", fg="white")
btn_save.grid(row=0, column=1, padx=10)

status_label = tk.Label(root, text="", font=("Arial", 10), bg="#f4f4f9")
status_label.pack(pady=5)

root.mainloop()
