import json
import os
from dotenv import load_dotenv
from injection_point.start import main
from injection_point.catalogdownloader import CatalogDownloader
from injection_point.constants import *

# import injection_point.catalogdownloader as x


if __name__ == '__main__':
    main()
    catalog_obj = CatalogDownloader()
    set_shopping_list()
    print(get_shopping_list(), SHOPRITE)
    # catalog_obj.get_page_info_shoprite(SHOPRITE)

    catalog_obj.driveStopNShop()
    #catalog_obj.driveShoprite()
