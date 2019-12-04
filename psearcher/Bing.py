from psearcher.BaseEngine import BaseEngine
class Bing(BaseEngine):
    def __init__(self, keyWord, amount=5, headers=None,timeout=60):
        self.name = 'Bing'
        self.keyWord = keyWord
        self.amount = amount
        if headers != None:
            self.headers = headers

        self.url = 'http://www.bing.com/search'
        self.keyTag = 'q'
        self.pageTag = 'first'
        self.startIndex = 1
        self.indexGap = 10
        self.timeout=timeout



    def getUrlParmas(self):
        url = self.url
        params = {
            self.keyTag: self.keyWord,
            self.pageTag: self.startIndex + self.indexGap*self.nextPage,
        }
        self.nextPage += 1
        return url, params

    def parser(self, soup):
        urls = []
        for li in soup.findAll('li', {'class': 'b_algo'}):
            title = li.h2.text.replace('\n', '').replace('  ', '')
            url = li.h2.a['href']
            desc = li.find('p').text
            result = {'title': title,
                            'link': url,
                            'desc': desc}
            urls.append(result)
        return urls
