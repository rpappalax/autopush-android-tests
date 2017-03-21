# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mobile.regions.topsites import Topsites


def test_topsites_tabs(appium):
    driver = appium

    ## Tap topsites tab, verify Facebook/Twitter icon is showing,
    topsites_tab = Topsites(driver)
    assert topsites_tab.is_fb_icon_visible
    assert topsites_tab.is_youtube_icon_visible

    ## Verify Add a site icon is showing
    assert topsites_tab.is_addsite_icon_visible
    assert topsites_tab.is_home_banner_visible

    ## Tap add a site icon, verify the text field is showing
    topsites_tab.tap_home_banner()
    topsites_tab.tap_addsite_icon()
    assert topsites_tab.is_search_field_visible
    assert topsites_tab.is_bookmark_list_visible

    ## Tap back button, verify the text field is now gone
    driver.back() ## To hide keyboard
    driver.back() ## To close window

    assert topsites_tab.is_fb_icon_visible
