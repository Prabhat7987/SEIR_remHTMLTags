# 🌐 Page Info Extractor (Python CLI Web Scraper)

A lightweight **Command Line Web Scraper** built using Python that fetches and extracts useful information from any webpage.

This tool downloads a webpage and displays:

✔ Page Title
✔ Full visible text content
✔ All hyperlinks present on the page

---

##😃 Features
👉Fetch webpage using HTTP requests
👉Parse HTML content efficiently
👉Extract page title
👉Extract clean readable text (without HTML tags)
👉Extract all links (`<a href="">`)
👉Command-line interface support
👉Beginner-friendly and easy to extend

---

## 🛠 Technologies Used
* **Python**
* **Requests** → for HTTP requests
* **BeautifulSoup (bs4)** → for HTML parsing
* **sys module** → for command-line arguments

---

## 📂 Project Structure
```
page_info.py   # Main script
README.md      # Documentation
```

---

## ⚙️ Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/page-info-extractor.git
cd page-info-extractor
```

### 2️⃣ Install dependencies
```bash
pip install requests beautifulsoup4
```

## ▶️ Usage
Run the script from terminal:
```bash
python page_info.py <URL>
```

### ✅ Example
```bash
python page_info.py https://example.com
```

## 🧾 Example Output
```
PAGE TITLE:
Example Domain

PAGE BODY:
Example Domain This domain is for use in illustrative examples...

PAGE LINKS:
https://www.iana.org/domains/example
```

## 🧠 How It Works
### 1️⃣ Command-line Argument
The script reads the URL using:
```python
sys.argv
```

### 2️⃣ Fetch Webpage
The `requests` library sends an HTTP GET request:
```python
requests.get(url)
```

This retrieves the webpage HTML.

### 3️⃣ Parse HTML
BeautifulSoup converts raw HTML into a searchable structure:
```python
BeautifulSoup(html, "html.parser")
```

### 4️⃣ Extract Data
✔ Title → `<title>` tag
✔ Body text → visible page content
✔ Links → `<a href="">` tags

## 📚 Concepts Demonstrated
✔ HTTP Requests & Responses
✔ HTML Parsing
✔ Web Scraping Basics
✔ Command-line Interfaces
✔ Python Standard Library Usage

## ❗ Error Handling
The program checks correct usage:
```bash
Usage: python page_info.py <URL>
```

Prevents crashes when URL is missing.

## 🔮 Future Improvements
* [ ] Extract images from webpage
* [ ] Save output to a file
* [ ] Crawl multiple pages
* [ ] Filter internal vs external links
* [ ] Add user-agent headers
* [ ] Build GUI version

---

## 🤝 Contributing
Contributions are welcome!
Feel free to fork this repo and improve it.

---

## 👨‍💻 Author
**Prabhat Patidar**
Python & Web Development Learner 🚀


