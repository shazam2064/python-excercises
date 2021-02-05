import re

a = "I enjoy learning programming languages such as Python 3"

result = re.findall(r"[a-z]", a)
result

result = re.findall(r"[A-Z]", a)
result

result = re.findall(r"[a-d]", a)
result

result = re.findall(r"[abn]", a)
result

result = re.findall(r"[ˆa]", a)
result

result = re.findall(r"[1-5]", a)
result

result = re.findall(r"[135]", a)
result

result = re.findall(r"[ˆ7]", a)
result