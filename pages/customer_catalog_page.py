import re

from pages.BaseClass import BaseClass


class CustomerCatalogPage(BaseClass):
    page_url = "catalog"

    def check_catalog_page(self, text):
        url = self.get_current_url()
        word = re.search(r"\w+$", url)
        assert word.group() == text
