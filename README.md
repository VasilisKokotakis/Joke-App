# Daily Joke App

Tired of bugs in your code?
Need a quick laugh before you throw your laptop out the window?

Look no further. This little app serves you **fresh random jokes** with style smooth animations, modern UI, and even a save feature for your favorites.
It’s basically a stand-up comedian in Python. 

---

## Features

*  **Random Jokes** - straight from the Official Joke API.
*  **Smooth Punchline Reveal** - fades in dramatically like a pro comedian.
*  **Save Your Favorites** - every saved joke lands in `saved_jokes.txt`.
*  **Toasts for Feedback** - sleek pop-ups tell you when jokes are saved or missing.
*  **Modern UI** - built with `ttkbootstrap` and a fresh `"superhero"` theme.
*  **Compact & Cross-Platform** - runs anywhere Python does.

---

## How to Run

1. Clone this repo:

   ```bash
   git clone https://github.com/VasilisKokotakis/Joke-App.git
   cd Joke_App
   ```

2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Linux/Mac
   env\Scripts\activate     # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install requests ttkbootstrap
   ```

4. Run the app:

   ```bash
   python app.py
   ```

---

## Saved Jokes

Every time you hit **Save Joke**, your current joke is appended to `saved_jokes.txt`.
Slowly but surely, you’ll build your **personal comedy archive**, one laugh at a time. 

---

## Tech Stack

* **Python 3**
* **ttkbootstrap** for the modern UI
* **Requests** for fetching jokes from the API

---

## Why?

Because debugging is hard.
Laughing is easy.

---

## Contribute

Got ideas?
Add dark mode auto-detection, new joke sources, or even a **roast-me** button.
Pull requests are always welcome 

---

## Screenshots

<img width="518" height="384" alt="image" src="https://github.com/user-attachments/assets/f38330f3-12dd-4313-acd8-17b64a65d10b" />

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.


