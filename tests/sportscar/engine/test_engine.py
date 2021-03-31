from pytest import mark


@mark.ui
def test_can_navigate_to_engine(chrome_browser):
    chrome_browser.get('https://www.artofmanliness.com')
    assert True
