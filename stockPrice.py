#!/usr/bin/python3

import bs4
import requests

def getQuote(url):
    try:
        res = requests.get(url) #use this website https://web.tmxmoney.com/getquote.php
        if res.raise_for_status() != None:
            print(res.raise_for_status())
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        parent_tag = soup.find('span', class_='price')
        price_tag = parent_tag.findChildren('span', recursive=False)
        price = price_tag[0].string
        return price
    except Exception as exc:
        print('An error has occured: %s' % exc)
        return False

def main():
    url = input('Enter the quote URL: ')
    while(True):
        price = getQuote(url)
        if not price:
            break
        print(price)

if __name__ == '__main__':
    main()
