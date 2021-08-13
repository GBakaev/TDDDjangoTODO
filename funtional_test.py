from selenium import webdriver
import os

# Get Current Dir Path
currentDir = os.path.dirname(os.path.abspath(__file__))

# Create ChromeDriver and Fetch Local Website
browser = webdriver.Chrome(currentDir + "/chromedriver")
browser.get('http://localhost:8000')

# We check the page title that is: Awesome Lists
assert 'Awesome Lists' in browser.title

# We want to enter a TO-DO Item

# We enter 'Do Homework' in the textfield

# We hit enter, the page gets refreshed and we see our To-Do item there

# We add another item, this time 'Study for TDD'

# The page refreshes again and we see our updated TO-Do list

# Quit Driver
browser.quit()