# -*- coding: utf-8 -*-
import json

from lxml import html
#import requests
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def main():
    print("catalog_main")


class CatalogDownloader:
    def __init__(self):
        print("Initalized catalog_downloader")

    def get_page_info_shoprite(self, page: str):
        #tree = html.fromstring(page.content)
        #object_names = tree.xpath('//a [@class="product__detailsLink"]/text()')
        #print(object_names)
        #span_names = tree.xpath('//span[@class="show-for-sr"]/text()')
        #print(span_names)
        req = urllib.request.Request(
            page,
            headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read() #urlopen(req).read()
        #jsonResponse = json.loads(urllib.request.urlopen(req).json())
        #print(jsonResponse)
        #print(webpage)
        soup = BeautifulSoup(webpage, 'html.parser')
        print(soup.prettify())
        results = soup.find_all('span', class_="show-for-sr")
        for result in results:
            print(result, "\n")