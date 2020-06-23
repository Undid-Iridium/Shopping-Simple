from injection_point.start import main
from injection_point.catalogdownloader import CatalogDownloader
#import injection_point.catalogdownloader as x
if __name__ == '__main__':
    main()
    catalog_obj = CatalogDownloader()
    catalog_obj.get_page_info_shoprite("https://shop.shoprite.com/store/9eae826/weekly-specials")
