# NOTE: This scraper works only for websites that serve content in static HTML and does not support JavaScript-rendered pages.
# I am not able to do the Simhash Assignment yet sir I am still learning Simhash
# Credit goes to google for learning this below libraries again from google

import sys
import re
import requests
from bs4 import BeautifulSoup  # for parsing credit goes to google first i learn from google then execute


# Browser header it will avoid blocking => Credit goes to google will help from google for this
HEADERS= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) " "AppleWebKit/537.36 (KHTML, like Gecko) " "Chrome/120.0 Safari/537.36"}
# fuction for extracting titles, body text and links on the page
def dataOf_page(url):
    try:
        response= requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        html_content = response.text
    except Exception as e:
        print("ohh we access this error 😮", e)
        return "title not exist", "", []
    SOP= BeautifulSoup(html_content, "html.parser")
    # title of the page
    if SOP.title and SOP.title.string:
        page_title= SOP.title.string.strip()
    else:
        page_title= "No title"
    # removing styles and scripts inside our html page
    for tag in SOP(["script", "style", "noscript"]):
        tag.decompose()
    # extracting visible text from page
    visible_text = SOP.get_text(separator=" ", strip=True)
    # Main links (outlinks)
    link_set= set()
    for tag in SOP.find_all("a"):
        href= tag.get("href")
        if href and href.startswith("http"):
            link_set.add(href)
    return page_title, visible_text, link_set
# Merging Assignment-2
# This is case sensitive basically we count the frequency of each word
# I know this method is not used here but added for assignment requirement
def count_words(text):
    tokens= re.findall(r'\b[a-zA-Z0-9]+\b', text)
    frequency= {}
    for word in tokens:
        frequency[word]= frequency.get(word,0)+ 1
    return frequency


# Entry point of program
def main():
    if len(sys.argv)!= 2:
        return
    url= sys.argv[1]
    title,body,links= dataOf_page(url)
    # Output as required by sir
    # Title (1 line)
    print(title)
    # Body Text
    print(body)
    # Outlinks (1 per line)
    for link in links:
        print(link)
if __name__ == "__main__":
    main()
