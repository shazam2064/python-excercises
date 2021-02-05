import re

a = "I enjoy learning programming languages such as Python 3"

re.split(r" ", a)
# piece of code of below and from up do same thing
re.split(r"\s", a)

a.split(" ")

re.split(r"\W\w{2}\W", a)

re.subn(r"\s", "_", a)
