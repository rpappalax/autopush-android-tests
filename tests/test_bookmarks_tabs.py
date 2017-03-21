# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mobile.regions.bookmarks import Bookmarks

def test_bookmarks_tabs(appium):
    driver = appium

    bookmarks_tab = Bookmarks(driver)
    assert bookmarks_tab.body.is_bookmarks_tab_clickable
    bookmarks_tab.body.click_bookmarks_tab()
    assert bookmarks_tab.is_bookmark_tab_visible
    assert bookmarks_tab.is_first_bookmark_visible

    # click first bookmark, check it's about:firefox page
    bookmarks_tab.tap_first_bookmark()
    assert bookmarks_tab.body.is_gecko_view_visible
    assert bookmarks_tab.header.get_address_bar_value == "about:firefox"

