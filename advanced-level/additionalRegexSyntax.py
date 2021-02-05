import re

a = "I enjoy learning programming languages such as Python 3"

re.search(r"ˆ[A-Z]\d\w{5}", a)

re.search(r"ˆ[A-Z]\w{5}\s\d$", a)

x = "He is ... z . . . sleeeeeeping"

re.search(r"z{10}", x)

