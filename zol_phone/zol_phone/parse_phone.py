import json
import pandas as pd


with open("phone_details_indent_new.json", encoding="utf-8") as jf:
    data = json.load(jf)
    print(data[0])
