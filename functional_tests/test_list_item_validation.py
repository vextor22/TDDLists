from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #user goes to homepage and accidentally tries to add empty list item
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        #the homepage refreshes and there is a message stating list items can't be 
        #empty
        self.wait_for(lambda: self.assertEqual(
                self.browser.find_element_by_css_selector('.has-error').text,
                "You can't have an empty list item"
        ))
        #tries again with a list item, it works, use then tries again to add an
        #empty item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)


        #similar warning message
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))


        #corrects error by entering text
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
