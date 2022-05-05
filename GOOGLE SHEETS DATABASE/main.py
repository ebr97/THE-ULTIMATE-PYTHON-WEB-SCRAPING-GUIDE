# importing the libraries

import gspread # the API that we'll use to manipulate data into Google Sheets using Python

import requests # the library we use to send requests to the server
from bs4 import BeautifulSoup # the library used to pull data out from HTML files

from datetime import date


# retriving our links from the URL column in Google Sheets
gc = gspread.service_account(filename='creds.json')
sh = gc.open('gsscraper').sheet1


list_all_links = sh.col_values(2)   # we retriving all the links from column URL 
list_all_links.pop(0)   # getting rid of the column header

row_no=2    # from row 2 we have data in our Google Sheet
list_to_be_scraped = []     # in this list we'll store only the links that hasn't previously been scraped
for link in list_all_links:
    if sh.cell(row_no,1).value.replace('.','-') == str(date.today().strftime('%d-%m-%Y')):      # in this case we supposed that all the links from previous days were scraped and we only want to scrape the links from current day
        list_to_be_scraped.append(link)
    row_no += 1

row_no = len(list_all_links) - len(list_to_be_scraped) + 2   # from this position we want to update our Google Sheets
# making our request to the server and retriving the HTML of the webpages

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'}
for url in list_to_be_scraped:
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'lxml')

# getting the Title, Price, Rating and Stock data

    title = soup.find('h1').text.strip()
    price = soup.find('p', class_='product-new-price').text.strip().replace('Lei','').strip()
    rating = soup.find('span', class_='star-rating-text gtm_rp101318 semibold text-gray-dark EOSMKP-90955-b hidden').text[:4].strip()
    stock = soup.find('span', class_='label label-in_stock').text.strip()

# creating our dictionary of product 

    product = {
        'title': title,
        'price': price,
        'rating': rating,
        'stock':stock
    }

    print(product)

# updating the Google Sheet

    gc = gspread.service_account(filename='creds.json')
    sh = gc.open('gsscraper').sheet1

    sh.update_cell(row_no,3, product['title'])
    sh.update_cell(row_no,4, product['price'])
    sh.update_cell(row_no,5, product['rating'])
    sh.update_cell(row_no,6, product['stock'])

    row_no += 1 # we increase the row number after each url is fully scraped to preserv the order and accuracy of the information