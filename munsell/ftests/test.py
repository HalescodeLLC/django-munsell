from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_convert_a_munsell_color(self):
        # Nina has heard about a cool new online tool that converts Munsell
        # colors to RGB and HEX values.  She goes to the homepage:
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Munsell colors
        assert 'Munsell' in self.browser.title

        # Satisfied, she goes back to sleep
        self.fail("Finish the ftests.")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
