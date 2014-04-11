from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_conversion_table(self, row_text):
        table = self.browser.find_element_by_id('id_conversion_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def check_for_correct_number_of_results(self, expected_count):
        expected_count = str(expected_count)
        count = self.browser.find_element_by_id('id_match_count').text
        self.assertIn(expected_count, count)

    def test_can_convert_a_munsell_color(self):
        # Nina has heard about a cool new online tool that converts Munsell
        # colors to RGB and HEX values.  She goes to the homepage:
        self.browser.get(self.live_server_url)

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

        # When she hits enter, the page updates, and now a single munsell color,
        #  name, and RGB values are listed for her color
        inputbox.send_keys(Keys.ENTER)

        self.check_for_correct_number_of_results(1)
        self.check_for_row_in_conversion_table('2.5Y 8/6 Yellow 229, 196, 123')

        # Excited, she tries a different munsell value: N 2.5
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N 2.5\n')

        self.check_for_row_in_conversion_table('N 2.5 Black 60, 60, 60')

        # Now, she wants to see a listing of ALL the N values
        ##  There are currently 10 N records in the database
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N\n')

        self.check_for_correct_number_of_results(10)

        # Now, she gets lazy and types the entire munsell value as a single string
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('N2.5\n')

        self.check_for_correct_number_of_results(1)

        # Next, she tries to enter a lower case letter to see how it likes that
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('n\n')

        self.check_for_correct_number_of_results(10)

        # She notices there are two different buttons beside the input box
        # One button says Fuzzy Match and the other says Exact Match
        fuzzy_button = self.browser.find_element_by_id('id_fuzzy_btn')
        self.assertIn('Fuzzy Match', fuzzy_button.text)
        exact_button = self.browser.find_element_by_id('id_exact_btn')
        self.assertIn('Exact Match', exact_button.text)

        # Curious, she enters a munsell name she knows and loves
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('5YR 4/6')
        
        # She decides to try the fuzzy match first, she guesses that any munsell
        # color with a matching set of characters will appear in her results
        fuzzy_button.send_keys(Keys.ENTER)

        ## there are currently 3 matching munell colors in the database
        self.check_for_correct_number_of_results(3)
        
        # Next she decides to try the exact match, this time she expects a single result
        exact_button = self.browser.find_element_by_id('id_exact_btn')
        inputbox = self.browser.find_element_by_id('id_munsell_entry')
        inputbox.send_keys('5YR 4/6')

        exact_button.send_keys(Keys.ENTER)

        self.check_for_correct_number_of_results(1)

        # Satisfied, she goes back to sleep

    def test_layout_and_styling(self):

        # Nina goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the header is nicely centered
        header_title = self.browser.find_element_by_tag_name('h1')
        self.assertAlmostEqual(header_title.location['x'] + header_title.size['width'] / 2, 512, delta=3)
