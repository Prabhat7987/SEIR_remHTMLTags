# NOTE: This scraper works only for websites that serve content in static HTML and does not support JavaScript-rendered pages.
# I am not able to do the Simhash Assignment yet sir I am still learning Simhash
# Credit goes to google for learning this below libraries again from google
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
def normalize_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url
def dataOf_page(url):
    # Headless Chrome setup
    chrOps= Options()
    chrOps.add_argument("--headless")
    chrOps.add_argument("--disable-gpu")
    chrOps.add_argument("--no-sandbox")
    chrOps.add_argument("--window-size=1920,1080")
    drver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrOps)
    try:
        drver.get(url)
        time.sleep(3)  # allow JS to load
        html = drver.page_source
    finally:
        drver.quit()
    SOP= BeautifulSoup(html, "html.parser")
    # title
    title= SOP.title.string.strip() if SOP.title and SOP.title.string else "No title"
    # remove scripts and styles
    for tag in SOP(["script", "style", "noscript"]):
        tag.decompose()
    #body text
    body_text= SOP.get_text(separator=" ", strip=True)
    # outgoing links
    lnks= set()
    for a in SOP.find_all("a", href=True):
        href= a["href"]
        if href.startswith("http"):
            lnks.add(href)
    return title,body_text, lnks
def main():
    if len(sys.argv)!= 2:
        print("Usage: python scraper.py <URL>")
        return
    rwURLs= sys.argv[1]
    url= normalize_url(rwURLs)
    title, body, lnks= dataOf_page(url)
    # rquired output by sir
    print(title)
    print(body)
    for link in lnks:
        print(link)
if __name__ == "__main__":
    main()
    
