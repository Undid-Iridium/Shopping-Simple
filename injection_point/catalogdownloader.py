# -*- coding: utf-8 -*-
import json
import re
import simplejson
from lxml import html
# import requests
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# from injection_point import SHOPPING_LIST
from injection_point.constants import SHOPPING_LIST, SHOPRITE
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    print("catalog_main")


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)



INVALID_TAGS = ["aria-live", "list", "cart", "Add ", "Remove", "Increase", "Decrease", "Your cart has been updated", \
                "Decrease ", "to  list", "Item "]


class CatalogDownloader:
    def __init__(self):
        print("Initalized catalog_downloader")

    def get_page_info_shoprite(self, page: str):
        # tree = html.fromstring(page.content)
        # object_names = tree.xpath('//a [@class="product__detailsLink"]/text()')
        # print(object_names)
        # span_names = tree.xpath('//span[@class="show-for-sr"]/text()')
        # print(span_names)
        req = urllib.request.Request(
            page,
            headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()  # urlopen(req).read()
        # jsonResponse = json.loads(urllib.request.urlopen(req).json())
        # print(jsonResponse)
        # print(webpage)
        soup = BeautifulSoup(webpage, 'html.parser')
        # print(soup.prettify())
        # results = soup.find_all('span', class_="show-for-sr")
        results = []
        for span in soup.find_all("span", attrs={'class', 'show-for-sr'}):
            if not any(subString in str(span) for subString in INVALID_TAGS):
                results.append(span)

        # results = soup.body.find('a', attrs={'class', 'product__detailsLink'})
        for result in results:  # results.span.find_all('span', recursive=False):
            print(remove_html_tags(str(result)))
            # current_result = remove_html_tags(str(result)).upper()
            # for element in SHOPPING_LIST:
            #    print(element, current_result)
            #    if element.upper() in current_result:
            #        print(remove_html_tags(str(result)))
            # print("HUH", remove_html_tags(str(result)))

    def driveShoprite(self):
        # webdriver.Chrome()
        browser = webdriver.Firefox()
        browser.get(SHOPRITE)
        time.sleep(1)

        elem = browser.find_element_by_tag_name("body")

        no_of_pagedowns = 76  # 76-77

        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            no_of_pagedowns -= 1

        post_elems = browser.find_elements_by_class_name("product__detailsLink")


        results = {}
        results1 = []

        for post in post_elems:
            # print(str(post.text))
            if not any(subString in str(post.text) for subString in INVALID_TAGS):
                print(str(post.text))
                if not post.text:
                    continue
                #results[str(post.text)] = counter
                results1.append(str(post.text))

                # results.append(str(post.text))
                # results.append(json.loads(post.text))

        post_elems = browser.find_elements_by_class_name("productPriceInfo")
        results2 = []
        for post in post_elems:
            # print(str(post.text))
            # print(str(post.text))
            if "was" in str(post.text) or "$" in str(post.text):
                print(str(post.text))
                if "Price" in str(post.text):
                    results2.append(str(post.text))
                    continue
                results2.append(str(post.text).partition("\n")[0])
                # results.append(json.loads(post.text))

        print(len(results1), len(results2))
        for counter, value in enumerate(results1):
            print(value)
            results[value] = results2[counter]

        json_dump_of_results = json.dumps(results)
        with open('listfile.txt', 'w') as fileHandler:
            # fileHandler.write('%s\n' % item)
            fileHandler.write(simplejson.dumps(simplejson.loads(json_dump_of_results), indent = 4, sort_keys=False))

        browser.quit()
        # print(results)
