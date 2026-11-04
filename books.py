import pandas as pd
import requests #for Python to communicate with websites.
from bs4 import BeautifulSoup #for Python to read and extract information from HTML

#web scrapping
URL = "https://books.toscrape.com/"

headers = { #provides information about the type of browser making the request.
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 contact:rispa.7@gmail.com"
}

response = requests.get(URL, headers=headers, timeout=10)
#requests.get - tells Python to visit the website and gets the html

#print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")
#bs reads the HTML.
#"html.parser" tells Python to use its built-in HTML parser
#print(soup)
books = soup.find_all("article", class_="product_pod")
#or soup.find_all("p", class_="price_color")

book_list = []# create this empty list b4 loop so that they are saved here
for book in books[:10]: 
    #Take the first 10 books 
    title = book.h3.a["title"] 
    #extracts the book title.
    price_text= book.find("p", class_="price_color").text 
        #extracts the price.
    #replace the euro with nothing so i can convert to int 
    price_gbp = float(
        price_text.replace("£", ""))
    #print(type(price))
    #print(type(title)) #for both to confirm data type is okay
    #print(title, price, end="\n\n")   # i wanted a new line btwn each book
    book_list.append({
        "Book Title": title,
        "Price (GBP)": price_gbp
    })
    #print(book_list)# turned to a list so i can make changes etc like adding other books..must be inside the loop to ensure that all books are added
print("\n--- Currency Conversion ---")
currency_converter = input("Enter the currency to convert to (KES, USD, EUR): ").upper()

if currency_converter not in ["KES", "USD", "EUR"]:
    print("Invalid currency selected.")

else:
    api_url = "https://v6.exchangerate-api.com/v6/39b91c0d70a8e0f4284892fa/latest/GBP"

api_response = requests.get(api_url)

print("Status code:", api_response.status_code)

api_response.raise_for_status()

currency_data = api_response.json()

exchange_rate = currency_data["conversion_rates"][currency_converter]
print("Exchange rate:", exchange_rate)

for book in book_list:
    converted_price = book["Price (GBP)"] * exchange_rate

    book[f"Price ({currency_converter})"] = round(converted_price, 2)
print(book["Book Title"], converted_price)    

df = pd.DataFrame(book_list)

print("\n--- Converted Book Prices ---")
print(df)

df.to_csv("converted_book_prices.csv", index=False)

  