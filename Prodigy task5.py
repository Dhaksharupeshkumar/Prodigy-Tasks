import requests
from bs4 import BeautifulSoup
import csv

def get_product_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_info = []

    # Extracting product names, prices, and ratings
    for product in soup.find_all('div', class_='sg-col-inner'):
        name = product.find('span', class_='a-size-medium').text.strip()
        price = product.find('span', class_='a-price-whole').text.strip()
        rating = product.find('span', class_='a-icon-alt').text.strip().split(' ')[0]

        product_info.append([name, price, rating])

    return product_info

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product Name', 'Price ($)', 'Rating'])
        writer.writerows(data)

def main():
    url = 'https://www.amazon.com/s?k=laptop'  # URL of the Amazon search page for laptops
    product_info = get_product_info(url)
    save_to_csv(product_info, 'amazon_laptops.csv')
    print("Data has been scraped and saved to amazon_laptops.csv")

if __name__ == "__main__":
    main()
