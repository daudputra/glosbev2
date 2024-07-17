from src.helper.save_json import SaveJson
from src.helper.read_csv import ReadCsv, GetFragment
from src.helper.langcode import LanguageCode

from src.controller.parse import Parse

from http import HTTPStatus

import requests

class ScraperMain:
    
    url = 'https://id.glosbe.com'

    path_csv = './src/csv'
    csv_files = ['list_kata.csv']

    bahasa1 = LanguageCode.codeLang('Indonesia')
    bahasa2 = ['bahasa jawa']


    for bahasa in bahasa2:
        bahasa_code = LanguageCode.codeLang(bahasa)

        if bahasa == 'bahasa jawa':
            provinsi = 'Jawa Barat'
        

        read_csv = ReadCsv(url, path_csv, csv_files, bahasa1, bahasa_code)
        urls_data = read_csv.get_urls()
        links = urls_data['url']
        kata = urls_data['kata']



        for link, kata in zip(links, kata):
            print(link)
            parse_page = Parse.glosbePage(link)
            
            glosbe_translate = Parse.glosbeTranslate(link)
            if glosbe_translate is None:
                continue
            
            if parse_page['deskripsi'] is None:
                continue
            
            if isinstance(glosbe_translate, str):
                glosbe_translate = [glosbe_translate]
            
            terjemahan = parse_page['terjemahan'] + glosbe_translate
            
            fragment_data = []

            fragmets_link = GetFragment.fragmenturl(link)
            for fragmet_link in fragmets_link:
                fragment_page = Parse.glosbeFragment(fragmet_link)
                print(fragmet_link)
                
                fragment_data.extend(fragment_page)
                
            
            json_file = SaveJson(link, provinsi, bahasa, kata, terjemahan, parse_page['deskripsi'], 's3_path', fragment_data)
            json_file.save_json_local(f'{kata}.json', provinsi)