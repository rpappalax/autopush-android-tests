# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from selenium.webdriver.common.by import By

from mobile.basePage import BasePage


class Topsites(BasePage):

    _facebook_icon_locator = (By.XPATH, "//android.widget.TextView[@text='Facebook']")
    _youtube_icon_locator = (By.XPATH, "//android.widget.TextView[@text='YouTube']")
    _addsite_icon_locator = (By.XPATH, "//android.widget.TextView[@text='Add a site']")
    _home_banner_locator = (By.ID, "home_banner")

    _search_text_field_locator = (By.ID, 'search')
    _bookmark_list_locator = (By.ID,'list')

    def __init__(self, selenium):
        BasePage.__init__(self, selenium)

    @property
    def is_fb_icon_visible(self):
        return self.is_element_visible(*self._facebook_icon_locator)

    @property
    def is_youtube_icon_visible(self):
        return self.is_element_visible(*self._youtube_icon_locator)

    @property
    def is_addsite_icon_visible(self):
        return self.is_element_visible(*self._addsite_icon_locator)

    @property
    def is_search_field_visible(self):
        return self.is_element_visible(*self._search_text_field_locator)

    @property
    def is_bookmark_list_visible(self):
        return self.is_element_visible(*self._bookmark_list_locator)

    @property
    def is_home_banner_visible(self):
        return self.is_element_visible(*self._home_banner_locator)

    def tap_addsite_icon(self):
        self.selenium.find_element(*self._addsite_icon_locator).click()

    def tap_home_banner(self):
        self.selenium.find_element(*self._home_banner_locator).click()

    def get_x(self):
        return self.selenium.find_element(*self.body._topsites_tab_locator).location['x']

    def get_y(self):
        return self.selenium.find_element(*self.body._topsites_tab_locator).location['y']
