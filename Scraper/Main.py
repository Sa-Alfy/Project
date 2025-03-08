import tkinter as tk
from Scraper.utils import fetch_books
from Gui import search_window

def main():
    root = tk.Tk()
    root.title("Books Scraper")
    root.geometry("500x500")
    root.configure(bg = "Light Blue")

    tk.Label(root, text = "Books Search", bg='Light blue', font=('Helvetica', 20)).pack()

    Button_frame = tk.Frame(root, bg='Light blue')
    Button_frame.pack(pady=20)

    tk.Button(Button_frame, text="Find Books", command=search_window).grid(row=0, column=0, padx=10)
    tk.Button(Button_frame, text="Exit", command=root.quit).grid(row=0, column=1, padx=10)

    fetch_books()
    root.mainloop()

if __name__ == "__main__":
    main()
