import requests
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification

current_joke = {"setup": "", "punchline": ""}

# --- Functions ---
def get_joke():
    global current_joke
    try:
        joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        current_joke = joke
        setup_label.config(text=joke["setup"])
        punchline_label.config(text="")
        # Reveal punchline with animation
        root.after(2000, lambda: reveal_punchline(joke["punchline"]))
    except Exception as e:
        setup_label.config(text="😢 Oops! Could not fetch a joke.")
        punchline_label.config(text=str(e))


def reveal_punchline(punchline, alpha=0):
    """Gradually show the punchline (fade-in effect)"""
    punchline_label.config(foreground=f"#{int(102 + alpha * 153):02x}{int(102 + alpha * 153):02x}{int(102 + alpha * 153):02x}")
    punchline_label.config(text=punchline)
    if alpha < 1:
        root.after(50, lambda: reveal_punchline(punchline, alpha + 0.05))


def save_joke():
    if current_joke["setup"] and current_joke["punchline"]:
        with open("saved_jokes.txt", "a", encoding="utf-8") as f:
            f.write(f"{current_joke['setup']} - {current_joke['punchline']}\n")

        ToastNotification(
            title="Joke Saved!",
            message="✅ Your joke was saved successfully.",
            duration=2000,
            bootstyle=SUCCESS
        ).show_toast()
    else:
        ToastNotification(
            title="Nothing to Save",
            message="⚠️ You need to fetch a joke first.",
            duration=2000,
            bootstyle=WARNING
        ).show_toast()


# --- UI Setup ---
root = ttk.Window(themename="superhero")
root.title("😂 Daily Joke App")
root.geometry("520x360")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=BOTH, expand=True)

title_label = ttk.Label(main_frame, text="Daily Fun App", font=("Arial Rounded MT Bold", 20))
title_label.pack(pady=10)

setup_label = ttk.Label(main_frame, text="Click below to get a joke!", font=("Arial", 14), wraplength=480, justify=CENTER)
setup_label.pack(pady=20)

punchline_label = ttk.Label(main_frame, text="", font=("Comic Sans MS", 12, "italic"), wraplength=480, justify=CENTER)
punchline_label.pack(pady=10)

btn_frame = ttk.Frame(main_frame)
btn_frame.pack(pady=10)

btn_get = ttk.Button(btn_frame, text="🎲 Get Joke", command=get_joke, bootstyle=PRIMARY, width=14)
btn_get.grid(row=0, column=0, padx=10)

btn_save = ttk.Button(btn_frame, text="💾 Save Joke", command=save_joke, bootstyle=SUCCESS, width=14)
btn_save.grid(row=0, column=1, padx=10)

footer_label = ttk.Label(main_frame, text="Made with ❤️ by Vasileios", font=("Arial", 9), foreground="#aaa")
footer_label.pack(side=BOTTOM, pady=5)

root.mainloop()
