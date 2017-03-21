# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage(object):

    def __init__(self, selenium, **kwargs):
        """
        Constructor
        """
        self.selenium = selenium
        self.timeout = 30
        self.wait = WebDriverWait(self.selenium, self.timeout)
        self.kwargs = kwargs

    def is_element_present(self, *locator):
        try:
            self.wait.until(lambda s: self.selenium.find_element(*locator))
            return True
        except TimeoutException:
            print "Present Timed Out"
            return False

    def is_element_visible(self, *locator):
        try:
            self.wait.until(lambda s: self.selenium.find_element(*locator).is_displayed())
            return True
        except TimeoutException:
            print "Visible Timed Out"
            return False

    def is_element_clickable(self, *locator):
        try:
            self.wait.until(lambda s: self.selenium.find_element(*locator).get_attribute('clickable') == 'true')
            return True
        except TimeoutException:
            print "Clickable Timed Out"
            return False

    def scroll_to_element(self, *locator):
        """Scroll to element"""
        el = self.selenium.find_element(*locator)
        self.selenium.execute_script("window.scrollTo(0, %s)" % (el.location['y'] - el.size['height']))

    @property
    def body(self):
        return Body(self.selenium)

    @property
    def header(self):
        return HeaderRegion(self.selenium)


class Body(BasePage):

    _body_locator = (By.ID,'home_pager')
    _topsites_tab_locator = (By.XPATH, "//android.widget.TextView[@index='0']")
    _bookmarks_tab_locator = (By.XPATH, "//android.widget.TextView[@index='1']")
    _history_tab_locator = (By.XPATH, "//android.widget.TextView[@index='2']")
    _gecko_view_locator = (By.XPATH, "//org.mozilla.gecko.GeckoView")

    @property
    def is_topsites_tab_clickable(self):
        return self.is_element_clickable(*self._topsites_tab_locator)

    @property
    def is_bookmarks_tab_clickable(self):
        return self.is_element_clickable(*self._bookmarks_tab_locator)

    @property
    def is_history_tab_clickable(self):
        return self.is_element_clickable(*self._history_tab_locator)

    @property
    def is_gecko_view_visible(self):
        return self.is_element_visible(*self._gecko_view_locator)

    def click_topsites_tab(self):
        self.selenium.find_element(*self._topsites_tab_locator).click()

    def click_bookmarks_tab(self):
        self.selenium.find_element(*self._bookmarks_tab_locator).click()

    def click_history_tab(self):
        self.selenium.find_element(*self._history_tab_locator).click()


class HeaderRegion(BasePage):

    _address_bar_locator = (By.ID, 'url_bar_entry')
    _address_textfield_locator = (By.ID, 'url_bar_title')
    _tab_button_locator = (By.ID, 'tabs')
    _menu_button_locator = (By.ID, 'menu')
    ##_dropdown_menu_locator = TBD

    def click_header_menu(self):
        self.selenium.find_element(*self._menu_button_locator).click()

    def tap_address_bar(self):
        self.selenium.find_element(*self._address_bar_locator).click()

    @property
    def is_menu_button_present(self):
        return self.is_element_present(*self._menu_button_locator)

    @property
    def is_address_bar_present(self):
        return self.is_element_present(*self._address_bar_locator)

    @property
    def get_address_bar_value(self):
        return self.selenium.find_element(*self._address_textfield_locator).text

    ##@property
    ##def is_dropdown_menu_visible(self):
    ##    return self.is_element_visible(*self._dropdown_menu_locator)

    ##@property
    ##def dropdown_menu_items(self):
    ##    # returns a list containing all the menu items
    ##    return [self.MenuItem(self.base_url, self.selenium, web_element) for web_element in self.selenium.find_elements(*self._menu_items_locator)]
