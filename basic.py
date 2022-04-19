from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from control_functions import slow_typing

# For headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")

# Open the browser
chrome_path = which("chromedriver")
driver = webdriver.Chrome(executable_path=chrome_path)
#driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options) # for headless
driver.get("https://duckduckgo.com")

# Search as per slow typing with different element
# search_input = driver.find_element_by_id("search_form_input_homepage")
# search_input = driver.find_element_by_xpath('//input[@class="js-search-input search__input--adv"]')
search_input = driver.find_element_by_xpath("//input[contains(@class,'js-search-input')]")
search_text = slow_typing(search_input, 'My User Agent')
search_input.send_keys(Keys.ENTER)

# Click on search button
"""search_btn = driver.find_element_by_id("search_button_homepage")
search_btn.click()"""

print(driver.page_source)
driver.close()




