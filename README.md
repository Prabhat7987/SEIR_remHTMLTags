# I am currently working on understanding SimHash and its implementation. As I am still learning the concept, I have not yet completed the SimHash assignment. I will finish the coding part once I gain a clearer understanding of the topic.

# Simple Web Page Info Extractor
This Python script takes a website URL from the command line and extracts:
* Page title
* Visible body text
* All links present on the page
It uses **Requests** to download the webpage and **BeautifulSoup** to parse the HTML.

## Requirements
Install required libraries:
```
pip install requests beautifulsoup4
```
## Usage
Run from command line:
```
python Assignment.py url1 and url 2
```
Example:
```
python Assignment.py https// google.com
```

## Output
The program prints:
* title of the page
* body text
* links found on the page

## Note
Some websites use JavaScript to load content.
In such cases, the scraper may not show full content.
