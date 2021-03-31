from pytest import mark


@mark.body
class BodyTests:
    @mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('https://www.sydsvenskan.se')
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
