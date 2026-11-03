import requests #for Python to communicate with websites.
from bs4 import BeautifulSoup #for Python to read and extract information from HTML

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
    price = book.find("p", class_="price_color").text 
        #extracts the price.
    price = price.replace("£", "")#replace the euro with nothing so i can convert to int 
    price = float(price)
    #print(type(price))
    #print(type(title)) #for both to confirm data type is okay
    #print(title, price, end="\n\n")   # i wanted a new line btwn each book
    book_list.append({
        "Book Title": title,
        "Price (GBP)": price
    })
    #print(book_list)# turned to a list so i can make changes etc like adding other books..must be inside the loop to ensure that all books are added
currency_converter = input("Enter the currency to convert to (KES, USD, EUR): ").upper()
url = "https://console.fastforex.io/currencies/listing.json?key=f4ff6419e9-46aaa81474-tnx2jc/latest/GBP"
response = requests.get(url)
print(f"Server replied with: {response.status_code}")
#print(response.text)


#df = pd.DataFrame(book_list) #data frame creates a table 
#df.index = df.index + 1 # to have it start at one, instead of 0 , to note this does not change how python njumbers
#print(df)
#df.to_csv("books_prices.csv", index = False)
#print(df) # on csv file the index column is not there but appears here

#df.to_csv("books_prices.csv", index = True)
#print(df)# the index c appears on csv file, not recommneded 

#df.to_csv("books_prices.csv") 
#print(df)

#make sure to close excel so you dont get permision denied.



   


