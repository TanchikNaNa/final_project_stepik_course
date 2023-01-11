from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    register_form = (By.CSS_SELECTOR, '#register_form')
    login_form = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    button_add_into_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    find_product_name = (By.CSS_SELECTOR, ".product_main h1")
    find_product_price = (By.CSS_SELECTOR, ".product_main p")
    basket_find_product_name = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    basket_find_product_price = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")




    

