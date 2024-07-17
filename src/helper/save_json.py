import json
import os
from datetime import datetime

class SaveJson:

    def __init__(self, response, prov, bahasa, kata, tl_list, desc, s3_path, data):
        self.response = response
        self.prov = prov
        self.bahasa = bahasa
        self.kata = kata
        self.tl_list = tl_list
        self.desc = desc
        self.s3_path = s3_path
        self.data:dict = data


    def save_json_local(self, filename, provinsi):
        directory = os.path.join('data', provinsi.replace(' ', '_').lower())
        os.makedirs(directory, exist_ok=True)
        filename_json = filename.replace(' ', '_').lower()
        file_path = os.path.join(directory, filename_json)

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.mapping(), json_file, ensure_ascii=False)


    def mapping(self):
        full_data = {
            'link': self.response,
            'domain': self.response.split('/')[2],
            'tag': [
                self.response.split('/')[2],
                self.prov,
                self.bahasa
            ],
            'crawling_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'crawling_time_epoch': int(datetime.now().timestamp()),
            'path_data_raw': self.s3_path,
            'path_data_clean': None,
            'provinsi': self.prov,
            'nama_bahasa': self.bahasa,
            'kata': self.kata,
            'data': {
                'kata': self.kata,
                'terjemahan': self.tl_list,
                'deskripsi': self.desc,
                'contoh_teks_terjemahan': self.data
            },
        }
        return full_data