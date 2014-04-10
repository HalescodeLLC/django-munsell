
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_conversion_table(self, row_text):
        table = self.browser.find_element_by_id('id_conversion_table').text
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def check_for_correct_number_of_results(self, expected_count):
        expected_count = str(expected_count)
        count = self.browser.find_element_by_id('id_match_count').text
        self.assertIn(expected_count, count)

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

        self.check_for_row_in_conversion_table('229 196 123')

        # Excited, she tries a different munsell value: N 2.5
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N 2.5\n')

        # inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_conversion_table('60 60 60')

        # Now, she wants to see a listing of ALL the N values
        ##  There are currently 10 N records in the database
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N\n')

        self.check_for_correct_number_of_results(10)

        # Now, she gets lazy and types the entire munsell value as a single string
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N2.5\n')

        self.check_for_correct_number_of_results(1)

        # Next, she tries to enter a lower case letter to see how it likes it
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('n\n')

        self.check_for_correct_number_of_results(10)

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
