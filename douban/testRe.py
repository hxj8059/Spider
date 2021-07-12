import re

pat = re.compile("AA")
m = pat.findall("CBAAGFFAA")
# m = re.search("asd", "Aasd")
print(m)
