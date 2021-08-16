from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os

# New Visitor Tests
class NewVisisorTest(unittest.TestCase):
    # Runs on setup
    def setUp(self): 
        # Get Current Dir Path
        self.currentDir = os.path.dirname(os.path.abspath(__file__))
        # Create ChromeDriver and Fetch Local Website
        self.browser = webdriver.Chrome(self.currentDir + "/chromedriver")

    # Runs at the end
    def tearDown(self):
        # Quit Driver
        self.browser.quit()

    # Test user can start a list and save it
    def test_user_can_start_new_list(self):
        # Get the Webpage
        self.browser.get('http://localhost:8000')

        # We check the page title that is: Awesome Lists
        assert 'Awesome Lists' in self.browser.title

        # We want to enter a TO-DO Item
        inputBox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputBox.get_attribute('placeholder'),
            'Enter a TO-Do item'
        )
        
        # We enter 'Do Homework' in the textfield
        inputBox.send_keys('Do Homework')

        # We hit enter, the page gets refreshed and we see our To-Do item there
        inputBox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Do Homework' for row in rows)
        )

        # Finish the tests
        self.fail('Finish the Tests.')

        # We add another item, this time 'Study for TDD'

        # The page refreshes again and we see our updated TO-Do list

# Run all the functional tests.
if __name__ == '__main__':
    unittest.main()