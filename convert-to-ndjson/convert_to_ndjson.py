import pandas as pd
import openpyxl # dependency installed
import io
import json

# convert xls/xlsx binary into ndjson format 

with open("Untitled spreadsheet.xlsx", "rb") as binary_file:
    # read the whole file at once
    data = binary_file.read()
    print(data)
    print(type(data))

vBytes = io.BytesIO()
vBytes.write(data)
vBytes.seek(0)

df = pd.read_excel(vBytes)

with io.open("myndjsondata-excel.ndjson", "w", encoding="utf-8") as f:
    f.write(df.to_json(orient="records", lines=True, force_ascii=False))

# print(df)
# print(type(df))

# convert csv binary into ndjson format 

with open("Untitled spreadsheet.csv", "rb") as binary_file:
    # read the whole file at once
    data = binary_file.read()
    print(data)
    print(type(data))

vBytes = io.BytesIO()
vBytes.write(data)
vBytes.seek(0)

df = pd.read_csv(vBytes)

with io.open("myndjsondata-csv.ndjson", "w", encoding="utf-8") as f:
    f.write(df.to_json(orient="records", lines=True, force_ascii=False))

# print(df)
# print(type(df))