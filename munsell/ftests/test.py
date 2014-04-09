
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Munsell', header_text)

        # She is invited to enter a munsell color straight away
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a Munsell color'
                         )

        # She types '2.5Y 8/6'
        inputbox.send_keys('2.5Y 8/6')

        # When she hits enter, the page updates, and now the RGB values are
        # listed for her color
        inputbox.send_keys(Keys.ENTER)

        value01 = self.browser.find_element_by_class_name('rgb_value').text
        self.assertIn('229 196 123', value01)

        # Excited, she tries a different munsell value: N 2.5
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N 2.5')

        inputbox.send_keys(Keys.ENTER)

        value02 = self.browser.find_element_by_class_name('rgb_value').text
        self.assertIn('60 60 60', value02)

        # Now, she wants to see a listing of ALL the N values
        ##  There are currently 10 N records in the database
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N')

        inputbox.send_keys(Keys.ENTER)

        count = self.browser.find_element_by_id('id_match_count').text
        self.assertIn('10', count)

        # Satisfied, she goes back to sleep
        self.fail("Finish the ftests.")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
