# Run in iDLE
from unittest import result

# Finds all div
result.find("div")

# Finds all div and returns them pretty
print(result.find("div").prettify())

# Finds all h1
result.find_all("h1")

# Finds all h1 and returns the number of h1 which is 6
len(result.find_all("h1"))

# Creates variable that finds the products
products = result.find_all("div", {"class": "col-sm-4 col-lg-4 cold-md-4"})
# Finds out what type the variable product is
type(products)
# Returns the number of products which should be 3
len(products)


