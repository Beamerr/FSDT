from selenium import webdriver
import unittest

class AccessTableTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_load_table(self):

    # open homepage to access table
    self.browser.get('http://localhost:8000')

    # table header exists
    self.assertIn('Phone-Mast-Table', self.browser.title)
    self.fail('finish test')
  
if __name__ == '__main__':
  unittest.main()

assert 'Phone Mast Table' in browser.title

self.browser.quit