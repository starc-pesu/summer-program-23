import csv
import json

class MyPipeline:
    def __init__(self):
        self.file = open('output.csv', 'w', newline='', encoding='utf-8')
        self.exporter = csv.DictWriter(self.file, fieldnames=['url'])
        self.exporter.writeheader()

    def process_item(self, item, spider):
        self.exporter.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()
