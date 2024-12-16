import csv
import random

# Define the possible values for each column based on your example
pno_prefixes = ["A4701", "A4702", "A4703", "A4704", "A4705"]
pno_suffixes = ["-000-1234", "-A01-1234", "-B02-1234", "-C03-1234", "-D04-1234"]
pno_cn_values = ["不織布", "不銹鋼", "高斯玩具", "塑料", "陶瓷"]
pno_desc_values = ["不織布TN001", "鋼鐵TC222", "Plastic 765", "Ceramic 876", "Fabric 123"]
labels = ["布類", "鐵類", "玩具類", "塑料類", "陶瓷類"]

# Create a list to hold the rows of data
data = []

# Generate 1000 rows of data
for _ in range(20):
    index = random.randint(0, 4)
    pno = random.choice(pno_prefixes) + random.choice(pno_suffixes)
    pno_cn = pno_cn_values[index]
    pno_desc = pno_desc_values[index]
    label = labels[index]
    data.append([pno, pno_cn, pno_desc, label])

# Write the data to a CSV file
with open('sample_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["pno", "pno_cn", "pno_desc", "label"])  # Write header
    writer.writerows(data)  # Write data

print("CSV file 'sample_data.csv' generated successfully.")