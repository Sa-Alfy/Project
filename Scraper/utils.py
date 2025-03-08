import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

books_list = []
url = 'https://books.toscrape.com/'

def fetch_books():
    global books_list
    books_list.clear()
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        exit()

    soup = BeautifulSoup(response.text, 'html.parser')
    book_containers = soup.find_all('article', class_='product_pod')

    for book in book_containers:
        book_title = book.find('h3').find('a')['title']
        book_price = book.find('div', class_='product_price').find('p', class_='price_color').text
        book_availability = book.find('p', class_='instock availability').text.strip()
        book_rating = book.find('p', class_='star-rating')['class'][1]
        image_url = url + book.find('div', class_='image_container').find('img')['src'].replace('../', '')
        books_list.append({
            'title': book_title,
            'price': book_price,
            'availability': book_availability,
            'rating': book_rating,
            'image_url': image_url
        })
