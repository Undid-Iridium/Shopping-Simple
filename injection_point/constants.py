import json
import os

from dotenv import load_dotenv

load_dotenv()
SHOPRITE = os.getenv("SHOPRITE")
STOPNSHOP = os.getenv("STOPNSHOP")
SHOPPING_LIST_FILE = os.getenv("LIST_FILE")

SHOPPING_LIST = []


def set_shopping_list():
    print(os.getcwd())
    print(os.getenv("LIST_FILE"))
    with open(SHOPPING_LIST_FILE) as json_file:
        data = json.load(json_file)
        for item in data['ALL_ITEMS']['DESIRED']:
            SHOPPING_LIST.append(item)
    print("Defined and associated items to shop for. ")

def get_shopping_list():
    return SHOPPING_LIST