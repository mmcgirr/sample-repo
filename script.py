import math
import os
import sys

import requests

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    return f"Hello, {who_to_greet}"


print(greet("World"))
print(greet("Mike"))
r = requests.get("https://www.google.com")
print(r.status_code)
name = input("Your name? ")
print(f"Hello {name}")
