import time
from utils.find_all_new_brawsers_windows import find_browsers_windows
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.BaseClass import BaseClass
from pages.selectors import main_page_loc as mp


class CustomerMainPage(BaseClass):
    page_url = None

    def wait(self):
        driver_wait = WebDriverWait(self.driver, 10)
        return driver_wait

    def check_main_page(self, text):
        big_title_main_page = self.wait().until(
            EC.visibility_of_element_located(mp.name_main_page)
        )
        assert big_title_main_page.text == text

    def check_link_catalog_page(self, name):
        link_catalog_page = self.wait().until(
            EC.visibility_of_element_located(mp.catalog_loc)
        )
        link_catalog_page.click()
        time.sleep(5)
        name_in_catalog_page = self.wait().until(
            EC.visibility_of_element_located(mp.catalog_page_name_loc)
        )
        assert name_in_catalog_page.text == name

    def check_projects_page(self, name):
        link_projects_page = self.wait().until(
            EC.visibility_of_element_located(mp.projects_loc)
        )
        link_projects_page.click()
        name_in_projects_page = self.wait().until(
            EC.visibility_of_element_located(mp.projects_page_name_loc)
        )
        assert name in name_in_projects_page.text

    def check_blog_page(self, name):
        link_blog_page = self.wait().until(
            EC.visibility_of_element_located(mp.blog_loc)
        )
        link_blog_page.click()
        name_in_blog_page = self.wait().until(
            EC.visibility_of_element_located(mp.blog_name_page_loc)
        )
        assert name in name_in_blog_page.text

    def check_designers(self, name):
        blog = self.wait().until(EC.presence_of_element_located(mp.designers_loc))
        blog.click()
        element = self.wait().until(
            EC.presence_of_element_located(mp.element_designers_loc)
        )
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);", element
        )
        time.sleep(1)
        assert element.text == name

    def check_contacts(self, name):
        link_contacts = self.wait().until(
            EC.presence_of_element_located(mp.contacts_loc)
        )
        link_contacts.click()
        element = self.wait().until(EC.visibility_of_element_located(mp.loc_bel))
        assert element.text == name

    def check_link_whatsapp(self, text):
        link_whatsapp = self.wait().until(
            EC.visibility_of_element_located(mp.loc_whatsapp)
        )
        link_whatsapp.click()
        try:
            find_browsers_windows(self.driver)
            check_tel_whatsapp = self.wait().until(
                EC.visibility_of_element_located(mp.loc_text_whatsapp_2)
            )
        except:
            find_browsers_windows(self.driver)
            check_tel_whatsapp = self.wait().until(
                EC.visibility_of_element_located(mp.loc_text_whatsapp)
            )
        assert check_tel_whatsapp.text == text

    def check_link_telegram(self, url):
        button_telegram = self.wait().until(
            EC.visibility_of_element_located(mp.loc_telegram)
        )
        href = button_telegram.get_attribute("href")
        button_telegram.click()
        find_browsers_windows(self.driver)
        time.sleep(3)
        assert href == url
        assert "t.me" in href, "Ссылка не является Telegram ссылкой"

    def check_link_instagram(self):
        button_instagram = self.wait().until(
            EC.visibility_of_element_located(mp.loc_instagram)
        )
        button_instagram.click()
        link = button_instagram.get_attribute("href")
        assert link == "https://www.instagram.com/artmas.by/"
