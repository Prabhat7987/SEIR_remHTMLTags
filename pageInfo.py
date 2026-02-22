import sys
import requests
from bs4 import BeautifulSoup

def main():
    # 1. Take URL from command line
    if len(sys.argv) != 2:
        print("Usage: python page_info.py <URL>")
        return

    url = sys.argv[1]

    # 2. Fetch the webpage
    response = requests.get(url)
    html = response.text
    
    # 3. Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # -------- PAGE TITLE --------
    title = soup.title.string if soup.title else "No Title"
    print("PAGE TITLE:")
    print(title.strip())
    print()

    # -------- PAGE BODY (NO HTML TAGS) --------
    body = soup.get_text(separator=" ", strip=True)
    print("PAGE BODY:")
    print(body)
    print()

    # -------- ALL LINKS --------
    print("PAGE LINKS:")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)
            
if __name__ == "__main__":
    main()


# import sys #sys is a built-in module inside this module we have functions and methods that provides access to the Python interpreter and system-level operations.
# 👉 It helps you interact with:
# the runtime environment
# command line arguments
# memory & performance
# program execution control
# ✔ Why used here?
# To read input given in terminal.
# 🔹 Key Concept to Remember ⭐

# ✔ sys = built-in module
# ✔ contains variables + functions + system objects
# ✔ not a package
# ✔ mostly written in C

# 🔹 Key Concept to Remember ⭐
# ✔ sys = built-in module
# ✔ contains variables + functions + system objects
# ✔ not a package
# ✔ mostly written in C

# import requests
# 🔹 2️⃣ import requests
# ✔ What is requests?
# requests is a Python HTTP library used to:
# ✅ download webpages
# ✅ send GET & POST requests
# ✅ interact with APIs
# ✅ fetch data from internet
# 👉 Think of it as a browser inside Python.


# #👉sys.argv
# 🔹 How it works
# Run program from terminal:
# python test.py hello 123
# Output:
# ['test.py', 'hello', '123']
# Meaning:
# argv[0] → script name
# argv[1] → first argument
# argv[2] → second argument

 # 2. Fetch the webpage
# response = requests.get(url)
# 👉 It asks the server:
# “Send me the data from this URL.”
# 🔹 Quick Example
# import requests
# r = requests.get("https://httpbin.org/get")
# print(r.status_code)
# print(r.json())
# ✔ status → success
# ✔ json → server data
# 🔹 What is GET request?
# Web browsers use HTTP requests to fetch webpages.
# GET request = ask server:
# 👉 “Send me this webpage”
# 🔹 What does requests.get() do?
# ✔ Input:
# URL string
# ✔ Output:
# Response object containing:
# HTML content
# status code
# headers
# cookies

# response.status_code → 200 (success)
# response.text → HTML content
# response.headers → server info

