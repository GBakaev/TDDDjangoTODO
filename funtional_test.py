from selenium import webdriver
import os

# Get Current Dir Path
currentDir = os.path.dirname(os.path.abspath(__file__))

# Create ChromeDriver and Fetch Local Website
browser = webdriver.Chrome(currentDir + "/chromedriver")
browser.get('http://localhost:8000')

# Brand New Django installation; 
# Title: The install worked successfully! Congratulations!
assert 'successfully' in browser.title