from selenium.webdriver.common.by import By


class Locators:
    #login page
    USER_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.TAG_NAME, "h3")

    OPEN_TOP_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    #product page
    FIRST_CART_PRODUCT_IMAGE_LINK = (By.ID, "item_4_img_link")
    FIRST_CART_PRODUCT_HEADER_LINK = (By.LINK_TEXT, "Sauce Labs Backpack")
    # TODO: Написать нормальные locator для добавления товара
    ADD_FIRST_PRODUCT_TO_SHOPPINGCART = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_PRODUCT_TO_SHOPPINGCART = (By.LINK_TEXT, "Add to cart")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    COUNT_SHOPPING_CART =(By.CLASS_NAME, "shopping_cart_badge")

    OPEN_SWITCH_FILTER_MENU = (By.CLASS_NAME, "product_sort_container")
    FILTER_A_to_Z = (By.XPATH, "//*[@id=\"header_container\"]/div[2]/div[2]/span/select/option[1]")
    FILTER_Z_to_A = (By.XPATH, "//*[@id=\"header_container\"]/div[2]/div[2]/span/select/option[2]")
    FILTER_PRICE_LOW_to_HIGH = (By.XPATH,
                                "//*[@id=\"header_container\"]/div[2]/div[2]/span/select/option[3]")
    FILTER_PRICE_HIGH_to_LOW = (By.XPATH,
                                "//*[@id=\"header_container\"]/div[2]/div[2]/span/select/option[4]")
    FIRST_NAME_PRODUCT = (By.CLASS_NAME, "inventory_item_name")

