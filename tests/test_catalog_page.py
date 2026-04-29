def test_url_catalog_page(catalog_page):
    catalog_page.open_page()
    catalog_page.check_catalog_page("catalog")
