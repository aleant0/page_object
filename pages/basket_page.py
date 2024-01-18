from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Basket is not empty. Checkout button is visible"

    def should_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Can't see empty basket message"
