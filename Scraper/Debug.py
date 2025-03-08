import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, simpledialog

books_list = []
# URL to scrape
url = 'https://books.toscrape.com/'

def fetch_books():
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        exit()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book containers
    book_containers = soup.find_all('article', class_='product_pod')

    for book in book_containers:
        book_title = book.find('h3').find('a')['title']
        book_price = book.find('div', class_='product_price').find('p', class_='price_color').text
        book_availability = book.find('p', class_='instock availability').text.strip()
        book_rating = book.find('p', class_='star-rating')['class'][1]
        books_list.append({
            'title': book_title,
            'price': book_price,
            'availability': book_availability,
            'rating': book_rating
        })
    print(f"Fetched {len(books_list)} books")  # Debug statement

def search_book(Search_Window, book_name):
    Search_Window.destroy()
    if book_name:
        found_books = []
        for book in books_list:
            if book_name.lower() in book['title'].lower():
                found_books.append(book)
        if found_books:
            result_text = ""
            for book in found_books:
                result_text += f"Title: {book['title']}\nPrice: {book['price']}\nAvailability: {book['availability']}\nRating: {book['rating']}\n\n"
            messagebox.showinfo("Search Results", result_text)
        else:
            messagebox.showinfo("Search Results", "No books found with that name.")
    else:
        messagebox.showinfo("Search Results", "No book name entered.")

def search_window():
    Search_Window = tk.Toplevel()
    Search_Window.title("Search Books")
    Search_Window.geometry("500x500")
    Search_Window.configure(bg = "Light Blue")
    
    tk.Label(Search_Window, text="Search Books", font=("Helvetica", 20), bg="Light Blue").pack(pady=10)
    
    search_entry = tk.Entry(Search_Window, width=50)
    search_entry.pack(pady=10)
    
    tk.Button(Search_Window, text="Search Book", command=lambda: search_book(Search_Window, search_entry.get())).pack(pady=10)

def main():
    root = tk.Tk()
    root.title("Books Scraper")
    root.geometry("500x500")
    root.configure(bg = "Light Blue")

    tk.Label(root, text = "Books Search",bg='Light blue', font=('Helvetica', 20),).pack()

    Button_frame = tk.Frame(root, bg='Light blue')
    Button_frame.pack(pady=20)

    tk.Button(Button_frame, text="Find Books", command=search_window).grid(row=0, column=0, padx=10)
    tk.Button(Button_frame, text = "Exit", command= root.quit).grid(row=0, column=1, padx=10)

    # Fetch books when the application starts
    fetch_books()
    print(books_list)  # Debug statement to verify books_list is populated

    root.mainloop()

if __name__ == "__main__":
    main()