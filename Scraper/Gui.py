import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io
from Scraper.utils import books_list

def search_book(Search_Window, book_name):
    Search_Window.destroy()
    if book_name:
        found_books = []
        for book in books_list:
            if book_name.lower() in book['title'].lower():
                found_books.append(book)
        if found_books:
            display_results(found_books)
        else:
            messagebox.showinfo("Search Results", "No books found with that name.")
    else:
        messagebox.showinfo("Search Results", "No book name entered.")

def display_results(found_books):
    result_window = tk.Toplevel()
    result_window.title("Search Window")
    result_window.geometry("500x500")
    result_window.configure(bg="Light Blue")

    tk.Label(result_window, text="Search Results", font=("Helvetica", 20), bg="Light Blue").pack(pady=10)

    canvas = tk.Canvas(result_window, bg="Light Blue")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(result_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    frame = tk.Frame(canvas, bg="Light Blue")
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Dictionary to hold image references
    image_refs = {}

    for book in found_books:
        try:
            img_response = requests.get(book['image_url'], stream=True)
            img_response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            img_data = img_response.raw.read()
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((100, 150), Image.LANCZOS)  # Use LANCZOS for high-quality resizing
            img = ImageTk.PhotoImage(img)

            # Store image reference to prevent garbage collection
            image_refs[book['title']] = img

            img_label = tk.Label(frame, image=img, bg="Light Blue")
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack(pady=10)

            result_text = f"Title: {book['title']}\nPrice: {book['price']}\nAvailability: {book['availability']}\nRating: {book['rating']}\n\n"
            text_label = tk.Label(frame, text=result_text, bg="Light Blue", justify=tk.LEFT, anchor='w')
            text_label.pack(pady=10)

        except requests.exceptions.RequestException as e:
            error_label = tk.Label(frame, text=f"Error loading image for {book['title']}", bg="Light Blue")
            error_label.pack(pady=10)
        except Exception as e:
            error_label = tk.Label(frame, text=f"Error processing image for {book['title']}", bg="Light Blue")
            error_label.pack(pady=10)

    # Fix the button frame creation by removing invalid position parameter
    button_frame = tk.Frame(result_window, bg="Light Blue")
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    tk.Button(button_frame, text="Close", command=result_window.destroy).pack()

def search_window():
    Search_Window = tk.Toplevel()
    Search_Window.title("Search Books")
    Search_Window.geometry("500x500")
    Search_Window.configure(bg="Light Blue")

    tk.Label(Search_Window, text="Search Books", font=("Helvetica", 20), bg="Light Blue").pack(pady=10)

    search_entry = tk.Entry(Search_Window, width=50)
    search_entry.pack(pady=10)

    tk.Button(Search_Window, text="Search Book",command=lambda: search_book(Search_Window, search_entry.get())).pack(pady=10)
