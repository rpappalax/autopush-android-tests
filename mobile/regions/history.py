# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from mobile.basePage import BasePage


class History(BasePage):

    _recent_closed_locator = (By.XPATH, "//android.widget.TextView[@text='Recently closed']")
    _synced_devices_locator = (By.XPATH, "//android.widget.TextView[@text='Synced devices']")
    _recent_website_empty_area_locator = (By.ID, "home_history_empty_view")
    _back_locator = (By.XPATH, "//android.widget.TextView[@text='Back to full History']")
    _empty_recent_tab_area_locator = (By.ID, 'home_recent_tabs_empty_view')
    _empty_sync_field_locator = (By.ID, 'home_clients_empty_view')

    def __init__(self, selenium):
        BasePage.__init__(self, selenium)

    @property
    def is_empty_recent_website_area_visible(self):
        return self.is_element_visible(*self._recent_website_empty_area_locator)

    @property
    def is_empty_recent_tab_field_visible(self):
        return self.is_element_visible(*self._empty_recent_tab_area_locator)

    @property
    def is_empty_sync_field_visible(self):
        return self.is_element_visible(*self._empty_sync_field_locator)

    def tap_recently_closed(self):
        self.selenium.find_element(*self._recent_closed_locator).click()

    def tap_synced_devices(self):
        self.selenium.find_element(*self._synced_devices_locator).click()

    def tap_back_to_history(self):
        assert self.is_element_visible(*self._back_locator)
        self.selenium.find_element(*self._back_locator).click()
