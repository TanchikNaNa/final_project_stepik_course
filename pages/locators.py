from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    register_form = (By.CSS_SELECTOR, '#register_form')
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form_login = (By.CSS_SELECTOR, "#id_registration-email")
    register_form_password1 = (By.CSS_SELECTOR, "#id_registration-password1")
    register_form_password2 = (By.CSS_SELECTOR, "#id_registration-password2") 
    register_form_button = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    button_add_into_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    find_product_name = (By.CSS_SELECTOR, ".product_main h1")
    find_product_price = (By.CSS_SELECTOR, ".product_main p")
    basket_find_product_name = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    basket_find_product_price = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    go_to_basket = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    product_in_basket = (By.CSS_SELECTOR, ".basket-items")
    message_about_empty_basket = (By.CSS_SELECTOR, "#content_inner>p")



    

