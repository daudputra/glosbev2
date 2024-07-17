class LanguageCode:
    def __init__(self, lang):
        self.lang : str = lang


    @staticmethod
    def codeLang(lang):
        codelang = {
            'batak toba' : 'bbc',
            'jepang' : 'ja',
            'indonesia' : 'id',
            'madura' : 'mad',
            'bali' : 'ban',
            'banjar' : 'bjn',
            'bugis' : 'bug',
            'toraja' : 'sda',
            'tidore' : 'tvo',
            'biak' : 'bhw',
            'tolaki' : 'lbw',
            'komering' : 'kge',
            'batak simalungun' : 'bts',
            'jawa' : 'jv',
            'sunda' : 'su',
            'indonesia' : 'id'
        }

        lang_lower = lang.lower()
        if 'bahasa' in lang_lower:
            lang_lower = lang_lower.replace('bahasa','').strip()
        
        if lang_lower in codelang:
            return codelang[lang_lower]
        else:
            print('unknown langcode')
            return 'unknown'