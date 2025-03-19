# Reddit Scraper

A simple Python-based scraper that collects all post links from a subreddit using Selenium and BeautifulSoup. The scraper scrolls through the subreddit, extracts all post URLs, and saves them into a JSON file.

## Features

- **Automated Scrolling**: The scraper automatically scrolls through the subreddit page to load all posts.
- **Link Extraction**: Extracts all post URLs containing the word "comments".
- **JSON Output**: Saves the URLs to a `links.json` file.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- Chrome WebDriver

