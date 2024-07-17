import csv
import os
from parsel import Selector
import requests

class ReadCsv:

    def __init__(self, base_url, csv_folder, csv_files, bahasa1, bahasa2):
        self.base_url = base_url
        self.csv_folder = csv_folder
        self.csv_files: list = csv_files
        self.bahasa1 = bahasa1
        self.bahasa2 = bahasa2

    def get_urls(self):
        urls = []
        kata_list = []

        for csv_file in self.csv_files:
            csv_path = os.path.join(self.csv_folder, csv_file)
            with open(csv_path, newline='') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for row in csvreader:
                    kata = row[0]
                    url = f'{self.base_url}/{self.bahasa1}/{self.bahasa2}/{kata}'
                    urls.append(url)
                    kata_list.append(kata)

        return {'url': urls, 'kata': kata_list}


class GetFragment:

    @staticmethod
    def fragmenturl(url):
        index = 1

        urls = []

        while True:
            url_fragment = f'{url}/fragment/tmem?page={index}&mode=MUST&stem=false'

            response = requests.get(url_fragment)
            sel = Selector(text=response.text)
            text = sel.xpath('/html/body/p[1]/text()').get()

            if text:
                break
            else:
                urls.append(url_fragment)

                index += 1
        return urls