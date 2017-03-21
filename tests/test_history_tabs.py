# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mobile.regions.history import History


def test_history_tabs(appium):
    driver = appium

    ## Tap history tab, verify Recently closed/ Synced devices list are showing
    history_tab = History(driver)
    assert history_tab.body.is_history_tab_clickable
    history_tab.body.click_history_tab()
    assert history_tab.is_empty_recent_website_area_visible

    ## Tap synced devices, check for welcome to sync message
    history_tab.tap_synced_devices()
    assert history_tab.is_empty_sync_field_visible

    ## Tap back to full history, verify that it went back to the history page
    history_tab.tap_back_to_history()
    assert history_tab.is_empty_recent_website_area_visible
