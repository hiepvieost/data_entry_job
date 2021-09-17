import requests
from bs4 import BeautifulSoup

URL = "https://www.zillow.com/oakland-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.38812446594238%2C%22east%22%3A-122.11827278137207%2C%22south%22%3A37.73677016318329%2C%22north%22%3A37.90453580039865%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A13072%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept-Language": "en,en-US;q=0.9,de;q=0.8"
}
reponse = requests.get(URL,headers=header)
web_html = reponse.text

soup = BeautifulSoup(web_html, "html.parser")
# list_price = []
# list_address = []
# list_link = []

prices = soup.find_all(name="div" ,class_="list-card-price")
addresses = soup.find_all(name="address" ,class_="list-card-addr")
links = soup.find_all(name="a" ,class_="list-card-link list-card-link-top-margin")
list_price = [price.getText() for price in prices]
list_address = [address.getText() for address in addresses]
list_link = [link.get("href") for link in links]
print(list_price)
n = 0
for _ in range(len(list_price)):
    if n <= len(list_price):
        n += 1
        print(list_price[n])

