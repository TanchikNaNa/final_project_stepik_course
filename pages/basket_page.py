from .base_page import BasePage
from .locators import BasketPageLocators 

class BasketPage(BasePage):

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.product_in_basket), "Product in basket, but shoul not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.message_about_empty_basket), "Message about empty basket is absent"