# Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Django Live Tests
from django.test import LiveServerTestCase
import os

# New Visitor Tests
class NewVisisorTest(LiveServerTestCase):
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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    # Test user can start a list and save it
    def test_user_can_start_new_list(self):
        # Get the Webpage
        self.browser.get(self.live_server_url)

        # We check the page title that is: Awesome Lists
        assert 'Awesome Lists' in self.browser.title

        # We want to enter a TO-DO Item
        inputBox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputBox.get_attribute('placeholder'),
            'Enter a To-Do item'
        )

        # We enter 'Do Homework' in the textfield
        inputBox.send_keys('Do Homework')
        # We hit enter, the page gets refreshed and we see our To-Do item there
        inputBox.send_keys(Keys.ENTER)
        list_url = self.browser.current_url
        self.assertRegex(list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Do Homework')

        # We add another item to the list
        # We add another item, this time 'Study for TDD'
        inputbox = self.browser.find_element_by_id('id_new_item') 
        inputbox.send_keys('Study for TDD') 
        inputbox.send_keys(Keys.ENTER)

        # The page refreshes again and we see our updated TO-Do list
        self.check_for_row_in_list_table('1: Do Homework')
        self.check_for_row_in_list_table('2: Study for TDD')

        # New Session
        self.browser.quit()
        self.browser = webdriver.Chrome(self.currentDir + "/chromedriver")

        # New User visits the home page. 
        # There is no sign of the last user's # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text 
        self.assertNotIn('Do Homework', page_text) 
        self.assertNotIn('Study for TDD', page_text)

        # We start by entering a new item.
        inputbox = self.browser.find_element_by_id('id_new_item') 
        inputbox.send_keys('Buy milk') 
        inputbox.send_keys(Keys.ENTER)

        # We get our own unique URL
        second_list_url = self.browser.current_url
        self.assertRegex(second_list_url, '/lists/.+')
        self.assertNotEqual(second_list_url, list_url)

        # Again, there is no trace of the first user's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)