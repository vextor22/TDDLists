from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                'Enter a to-do item')

        #type in a text boxa
        inputbox.send_keys('Buy peacock feathers')

        #hit enter, page updates, now the page shows:
        #"1: The ting we type" in the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)        
        )

        #text box still present for next item
        self.fail('Finish the test!')
        #page updates showing new item added

        #unique url for the list

        #visit unique url, list is there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
