import re

a = "I enjoy learning programming languages such as Python 3"

result = re.search(r"\W(\w{2})\W|([A-Z]\w{5})\s\d", a)
result.group(1)

result.group(2) # you get nothing

result = re.search(r"\W(\w{2})\W|([A-Z]\w{5})\s\d", a)
result.group(1)
