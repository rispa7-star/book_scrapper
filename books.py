import requests #Allows Python to communicate with websites.
from bs4 import BeautifulSoup #Allows Python to read and extract information from HTML

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

for book in books[:10]: 
    #Take the first 10 books 
    title = book.h3.a["title"] 
    #extracts the book title.
    price = book.find("p", class_="price_color").text 
        #extracts the price.
    price = price.replace("£", "")#replace the euro with nothing so i can convert to int 
    price = float(price)
    #print(type(price))
    #print(type(title)) #for both to confirm data type is okay
    #print(title, price, end="\n\n")   # i wanted a new line btwn each book
    book_list = []
    book_list.append({
        "Book Title": title,
        "Price (GBP)": price
    })
    print(book_list)# turned to a list so i can make changes etc like adding other books..must be inside the loop to ensure that all books are added

   


