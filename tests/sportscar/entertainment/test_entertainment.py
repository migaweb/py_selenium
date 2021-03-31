from pytest import mark


@mark.ui
def test_can_navigate_to_entertainment(chrome_browser):
    chrome_browser.get('https://www.google.com')
    assert True
