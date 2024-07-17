from parsel import Selector
import requests
from http import HTTPStatus
class Parse:

    @staticmethod
    def glosbeTranslate(url):

        url_split = url.split('/')
        bahasa1 = url_split[3]
        bahasa2 = url_split[4]
        kata = url_split[5]

        url = f'https://translate.glosbe.com/{bahasa1}-{bahasa2}/{kata}'

        response = requests.get(url)
        if response.status_code == HTTPStatus.OK:
            selector = Selector(text=response.text)
            translate = selector.xpath('/html/body/app-root/app-logo-navbar-content-footer-layout/div[2]/app-page-translator/div[1]/div[2]/div[2]/app-page-translator-translation-output/div/text()').get()

            if translate:
                return translate
            else:
                return None
        else:
            print(f'{HTTPStatus(response.status_code).description}')
            return None

    @staticmethod
    def glosbePage(url):
        try:
            response =  requests.get(url)
            print(url + ' ' + str(response.status_code))
            if response.status_code == HTTPStatus.OK:
                selector = Selector(text=response.text)

                deskripsi_raw = selector.xpath('/html/body/div[1]/div/div[2]/main/article/div/div[1]/div[1]/p[@id="content-summary"]/span//text()').getall()
                deskripsi = ' '.join(deskripsi_raw).strip()
                
                terjemahan = [text.strip() for text in selector.xpath('/html/body/div[1]/div/div[2]/main/article/div/div[1]/section[1]/div[2]/div/ul/li/div[2]/div[1]/div/h3/text()').getall()]

                return {
                    'deskripsi' : deskripsi,
                    'terjemahan' : terjemahan
                }
            else:
                print(f'{HTTPStatus(response.status_code).description}')
                return None
        except Exception as e:
            print(e)

    @staticmethod
    def glosbeFragment(url):
        try:
            example_data = []

            response =  requests.get(url)
            if response.status_code == HTTPStatus.OK:
                print(url + ' ' + str(response.status_code))
                selector = Selector(text=response.text)

                rows = selector.xpath('/html/body/div[2]/div/div[1]')
                for row in rows:
                    kata_text1_raw = row.xpath('.//div[1]//text()').getall()
                    kata_text2_raw = row.xpath('.//div[2]//text()').getall()
                    
                    kata_text1 = ' '.join(kata_text1_raw).strip()
                    kata_text2 = ' '.join(kata_text2_raw).strip()

                    data = {
                        'kalimat' : kata_text1,
                        'terjemahan' : kata_text2
                    }
                    
                    example_data.append(data)

                return example_data
            else:
                print(f'{HTTPStatus(response.status_code).description}')
                return None
        except Exception as e:
            print(e)