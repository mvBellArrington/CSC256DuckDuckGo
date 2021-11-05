import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def start_chrome():
    driver = webdriver.Chrome()
    website = "https://www.wikipedia.org/"
    driver.get(website)

def test_is_chrome_webdriver():
    driver = webdriver.Chrome()
    assert driver.name == "chrome"


def test_opens_wikipedia():
    driver = webdriver.Chrome()
    website = "https://www.wikipedia.org/"
    driver.get(website)

    assert driver.title == "Wikipedia"

def test_search_wake_tech():
    driver = webdriver.Chrome()
    website = "https://www.wikipedia.org/"
    driver.get(website)
    item_to_search = "wake tech"
    searchField = driver.find_element(By.ID, "searchInput") # driver.find_element_by_name("search") <-- this method is deprecated
    searchField.clear()
    searchField.send_keys(item_to_search)

    current_search_field = searchField.get_attribute("value")
    assert current_search_field == "wake tech"


def test_content_page_title_WTCC():
    driver = webdriver.Chrome()
    website = "https://www.wikipedia.org/"
    driver.get(website)
    item_to_search = "wake tech"
    searchField = driver.find_element(By.ID, "searchInput") # driver.find_element_by_name("search") <-- this method is deprecated
    searchField.clear()
    searchField.send_keys(item_to_search)
    searchField.send_keys(Keys.ENTER)
    sleep(8)
    site_title = driver.find_element(By.ID, "firstHeading").text # driver.find_element_by_id("firstHeading").text <-- this method is deprecated

    assert site_title == "Wake Technical Community College"

#def main():
#    test_is_chrome_webdriver()
#    test_opens_wikipedia()
#    test_search_wake_tech()
#    test_content_page_title_WTCC()




#main()




