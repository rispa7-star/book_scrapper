import requests

URL = "https://books.toscrape.com/"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36 contact:rispa.7@gmail.com"
}

response = requests.get(URL, headers=headers, timeout=10)

print(response.status_code)