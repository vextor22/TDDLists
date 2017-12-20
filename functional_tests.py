from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        #invited to enter a to-do item

        #type in a text box

        #hit enter, page updates, now the page shows:
        #"1: The ting we type" in the list

        #text box still present for next item

        #page updates showing new item added

        #unique url for the list

        #visit unique url, list is there

if __name__ == '__main__':
    unittest.main(warnings='ignore')
