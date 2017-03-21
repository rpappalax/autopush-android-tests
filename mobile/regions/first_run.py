# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from selenium.webdriver.common.by import By

from mobile.basePage import BasePage


class Firstrun(BasePage):

    _firstrun_view_locator = (By.ID, 'firstrun_pager')
    _welcome_view_1_locator = (By.XPATH, "//android.widget.TextView[@text='Welcome to Nightly']")
    _welcome_view_2_locator = (By.XPATH, "//android.widget.TextView[@text='Your faves, front and center']")
    _welcome_view_3_locator = (By.XPATH, "//android.widget.TextView[@text='Less data, more savings']")
    _welcome_view_4_locator = (By.XPATH, "//android.widget.TextView[@text='Nightly, always by your side']")
    _welcome_view_5_locator = (By.XPATH, "//android.widget.TextView[@text='Get connected, get started']")

    _welcome_next_locator = (By.ID, 'firstrun_link')
    _welcome_browse_locator = (By.ID, 'welcome_browse')

    def __init__(self, selenium):
        BasePage.__init__(self, selenium)

    @property
    def is_firstrun_visible(self):
        return self.is_element_visible(*self._firstrun_view_locator)

    @property
    def is_firstrun_view_1_visible(self):
        return self.is_element_visible(*self._welcome_view_1_locator)

    @property
    def is_firstrun_view_2_visible(self):
        return self.is_element_visible(*self._welcome_view_2_locator)

    @property
    def is_firstrun_view_3_visible(self):
        return self.is_element_visible(*self._welcome_view_3_locator)

    @property
    def is_firstrun_view_4_visible(self):
        return self.is_element_visible(*self._welcome_view_4_locator)

    @property
    def is_firstrun_view_5_visible(self):
        return self.is_element_visible(*self._welcome_view_5_locator)

    def tap_next(self):
        return self.selenium.find_element(*self._welcome_next_locator).click()

    def tap_start_browse(self):
        return self.selenium.find_element(*self._welcome_browse_locator).click()

    # clicking the address bar closes the first run view
    def close_firstrun_view(self):
        self.header.tap_address_bar()

