import sys
import re
import requests
from bs4 import BeautifulSoup # for parsing credit goes to google first i learn from google then execute

# Browser header it will avoid blocking => Credit goes to goole will help from google for this
HEADERS={
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36"
}

# fuction for extracting titiles, body text and links on the page
def dataOf_page(url):
    try:
        response=requests.get(url, headers=HEADERS,timeout=10)
        html_content = response.text
    except Exception as e:
        print(f"ohh we access this error😮", e)
        return "title not exist🙂‍↔️", "", []
    soup=BeautifulSoup(html_content, "html.parser")

    # title of the page
    page_title=soup.title.string.strip() if soup.title else "No🙂‍↔️ title"

    #removing styles and scripts inside our html page
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    visible_text= soup.get_text(separator=" ",strip=True).lower()

    # Main links
    link_set=set()
    for tag in soup.find_all(["a","link"]):
        href=tag.get("href")
        if href and href.startswith("http"):
            link_set.add(href)
    return page_title, visible_text, link_set

# Merging Assingnment- 2
# This is case sensitive basically we count the frequesncy of each word
def count_words(text):
    tokens=re.findall(r'\b[a-z0-9]+\b', text)
    frequency={}
    for word in tokens:
        frequency[word]= frequency.get(word,0)+1
    return frequency

# Entry point of program
def main():
    if len(sys.argv)!=3:
        print("Usage: python Assignment.py <URL1> <URL2>")
        return
    url1=sys.argv[1]
    url2=sys.argv[2]
    title1,body1,links1= dataOf_page(url1)
    print("Pg-1 title")
    print(title1)
    print("pg-1 body")
    print(body1)
    print("All-links page1")
    for link in links1:
        print(link)

if __name__ == "__main__":
    main()
