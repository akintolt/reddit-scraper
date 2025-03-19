
import json
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time



def collate_links(url):
    print("INITIALISITNG CHROMEDRIVER")
    # Set up Chrome options in headless mode
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration in headless mode
    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    print("FINISHED INITIALISITNG CHROMEDRIVER")

    print("NAVIGATING TO THE SUBREDDIT")
    # Navigate to the page
    
    driver.get(url)

    print("Rejecting cookies.")
    time.sleep(10)


    print("SCROLLING THE LENGTH OF THE PAGE\n")
    # Scroll down the page
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:


        SCROLL_PAUSE_TIME =  random.randint(4, 9) # Time in seconds between scrolls
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the updated page source after scrolling
    page_source = driver.page_source
    # Close the browser
    driver.quit()
    # Parse the updated page source using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    print("PULLING ALL OF THE LINKS\n")
    # Now you can work with the soup object to extract the data you need
    # For example, find all <a> tags with href containing "https://"
    https_links = soup.find_all('a', href=lambda href: href and "comments" in href)

    all_urls = []
    # Make a list for all of the unique lists.
    # Using a list comprehension to filter and modify links
    links = [link['href'] if 'https://www.reddit.com' in link['href'] else 'https://www.reddit.com' + link['href'] for link in https_links]

    # Converting the list to a set to remove duplicates, and then back to a list
    unique_links = list(set(links))
    # Dump into a JSON file
    with open("links.json", "w") as file:
        json.dump(unique_links, file, indent=4) 
    print("a link to each post in the subreddit has been saved to links.json")




collate_links("https://www.reddit.com/r/unitedkingdom/")