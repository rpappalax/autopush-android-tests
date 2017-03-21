# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from mobile.basePage import BasePage


class Bookmarks(BasePage):

    _bookmarks_locator = (By.ID, 'bookmarks_list')
    _first_bookmark_locator =(By.XPATH, "//android.widget.TextView[@text='Firefox: About your browser']")

    def __init__(self, selenium):
        BasePage.__init__(self, selenium)

    @property
    def is_bookmark_tab_visible(self):
        return self.is_element_visible(*self._bookmarks_locator)

    @property
    def is_first_bookmark_visible(self):
        return self.is_element_visible(*self._first_bookmark_locator)

    def tap_first_bookmark(self):
        self.selenium.find_element(*self._first_bookmark_locator).click()

    def get_x(self):
        return self.selenium.find_element(*self.body._bookmarks_tab_locator).location['x']

    def get_y(self):
        return self.selenium.find_element(*self.body._bookmarks_tab_locator).location['y']
