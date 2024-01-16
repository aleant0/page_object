from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def should_be_product_page_with_promo(self):
        self.should_be_promo_in_url()
        self.should_bee_add_to_basket_button()

    def should_be_promo_in_url(self):
        assert "?promo=newYear" in self.browser.current_url, "Not promo code in the url"

    def should_bee_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Can't see add_to_basket_button"

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def should_be_correct_book_title_in_alert(self):
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        alert_title = self.browser.find_element(*ProductPageLocators.ALERT_TITLE).text
        assert title == alert_title, "Titles don't match"

    def should_be_right_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        assert price == alert_price, "Prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not dissapeared"
