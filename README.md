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

### How to Use

**Clone the repository**:
   If you haven’t already, clone the repository to your local machine:


   git clone https://github.com/akintolt/reddit-scraper.git
   cd reddit-scraper
   python reddit_scraper.py
   collate_links(link)


## Example of `links.json` Output

[
    "https://www.reddit.com/r/unitedkingdom/comments/abc123/some_post_title/",
    "https://www.reddit.com/r/unitedkingdom/comments/def456/another_post_title/",
    
]


## Notes

- Make sure you have Chrome installed on your system and the corresponding version of ChromeDriver.
- By default, the Chrome WebDriver runs in headless mode, meaning it won't show a UI. You can uncomment the `chrome_options.add_argument("--headless")` line in the script if you prefer running it in a non-headless mode.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
