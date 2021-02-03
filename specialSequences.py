import re

a = "I enjoy learning programming languages such as Python 3"
# \d digits, \s whitespace, \w word, \D, \s #can't use this letters because will get error in path

result = re.search(r"\D+", a)
result.group()

result = re.search(r"\S+", a)
result.group()

result = re.search(r"\W+", a)
result.group()

a.index(result.group())

result = re.search(r"\AI", a)
result.group()

result = re.search(r"3\z", a)
result.group()
