from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.amazon.com/s?k=samsung+galaxy+s23+ultra&crid=3O06YC4YE9SDV&sprefix=samsung+%2Caps%2C151&ref=nb_sb_ss_ts-doa-p_3_8"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0"

# Headers for request
# ({'User-Agent','Accept-Language'})
HEADERS = ({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0','Accept-Language':'en-US, en;q=0.5'})

webpage = requests.get(url, headers=HEADERS)

##scrape the content
soup = BeautifulSoup(webpage.content, "html.parser")

links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


link = links[0].get('href')

product_list = "https://amazon.com"+ link


##scarping the product webpage by getting product name , price etc
new_webpage = requests.get(product_list, headers=HEADERS)
new_soup = BeautifulSoup(new_webpage.content, "html.parser")

##get information from these pages

product_name = new_soup.find("span",attrs={'id':'productTitle','class':'a-size-large product-title-word-break'}).text.strip()

product_price = new_soup.find("span",attrs={'class':'a-price-whole'}).text.strip('.')

product_rating = new_soup.find("span",attrs={'class':'a-icon-alt'}).text

product_review = new_soup.find("span",attrs={'id':'acrCustomerReviewText'}).text

print(product_review)
















