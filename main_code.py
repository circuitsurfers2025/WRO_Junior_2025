import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv
import os

# Define a class to hold product information
class Product:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

# Function to scrape product data from a website
def scrape_products(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    items = soup.find_all('div', class_='product-item')
    
    for item in items:
        name = item.find('h2', class_='product-title').text.strip()
        price = item.find('span', class_='price').text.strip()
        rating = item.find('span', class_='rating').text.strip()
        products.append(Product(name, price, rating))
    
    return products

# Function to save product data to a CSV file
def save_to_csv(products, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Rating'])
        for product in products:
            writer.writerow([product.name, product.price, product.rating])

# Function to load product data from a CSV file
def load_from_csv(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            products.append(Product(row[0], row[1], row[2]))
    return products

# Function to visualize product data
def visualize_data(products):
    names = [product.name for product in products]
    prices = [float(product.price.strip('$')) for product in products]
    ratings = [float(product.rating) for product in products]
    
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Products')
    ax1.set_ylabel('Price', color=color)
    ax1.plot(names, prices, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Rating', color=color)
    ax2.plot(names, ratings, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.xticks(rotation=90)
    plt.show()

# Main function to orchestrate scraping, saving, loading, and visualizing
def main():
    url = 'https://example.com/products'
    csv_file = 'products.csv'

    if not os.path.exists(csv_file):
        products = scrape_products(url)
        save_to_csv(products, csv_file)
    else:
        products = load_from_csv(csv_file)

    visualize_data(products)

if __name__ == "__main__":
    main()
