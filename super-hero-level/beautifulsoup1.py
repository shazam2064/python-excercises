# Run in iDLE
import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/static")

type(webpage)

text = webpage.text
type(text)

type(webpage)

text = webpage.text
type(text)
content = webpage.content
type(content)

result = BeautifulSoup(text)
# or:
result = BeautifulSoup(content)
# or, also specifying the parser to use:
result = BeautifulSoup(content, "html.parser")

# The result is the BeautifulSoup object
type(result)
content = webpage.content
type(content)

result = BeautifulSoup(text)
# or:
result = BeautifulSoup(content)
# or, also specifying the parser to use:
result = BeautifulSoup(content, "html.parser")
