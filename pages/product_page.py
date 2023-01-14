from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_into_basket(self):
        assert self.is_element_present(*ProductPageLocators.button_add_into_basket), "button_add_into_basket is absent"
        product_name = self.browser.find_element(*ProductPageLocators.find_product_name).text 
        product_price = self.browser.find_element(*ProductPageLocators.find_product_price).text
        button = self.browser.find_element(*ProductPageLocators.button_add_into_basket)
        button.click()
        self.solve_quiz_and_get_code()
        basket_product_name = self.browser.find_element(*ProductPageLocators.basket_find_product_name).text 
        basket_product_price = self.browser.find_element(*ProductPageLocators.basket_find_product_price).text
        product_price = product_price.replace (",", ".")
        product_price = filter(lambda x: x in "0123456789.", product_price)
        product_price = str.join("", product_price) 
        basket_product_price = filter(lambda x: x in "0123456789.", basket_product_price)
        basket_product_price = str.join("", basket_product_price)
        assert basket_product_name==product_name, "Uncorrect product's name in basket"
        assert basket_product_price==product_price, "Uncorrect product's price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.basket_find_product_name), \
        "Success message is presented, but should not be"

    def should_went_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.basket_find_product_name), \
        "Success message is presented, but should not be"




