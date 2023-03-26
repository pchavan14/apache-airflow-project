from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


def get_title(soup):

    try:
        #return the title
        title_string = soup.find("span",attrs={'id':'productTitle'}).text.strip()

    except AttributeError:

        title_string = ""

    return title_string

def get_price(soup):

    try:
        #return the title
        price = soup.find("span",attrs={'class':'a-price-whole'}).text.strip('.')

    except AttributeError:

        price = ""

    return price

def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

def get_review(soup):

    try:
        #return the title
        reviews = soup.find("span",attrs={'id':'acrCustomerReviewText'}).text

    except AttributeError:

        reviews = ""

    return reviews


if __name__ == '__main__':
    #URL
    URL = "https://www.amazon.com/s?k=samsung+galaxy+s23+ultra&crid=3O06YC4YE9SDV&sprefix=samsung+%2Caps%2C151&ref=nb_sb_ss_ts-doa-p_3_8"

    #HEADERS
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0','Accept-Language':'en-US, en;q=0.5'})

    # HTTP Request
    webpage = requests.get(URL,headers=HEADERS)

    # Create a SOUP object containing all the data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    # Store the links in a list
    links_list = []

    for link in links:
        links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[]}

    # Loop for extracting product details
    for link in links_list:
        new_webpage = requests.get("https://amazon.com"+link,headers=HEADERS)
        
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review(new_soup))     


    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("/Users/prachichavan/Documents/scrape-amazon-data/amazon_data.csv", header=True, index=False)
    


