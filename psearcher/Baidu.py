from psearcher.BaseEngine import BaseEngine
class Baidu(BaseEngine):
    def __init__(self, keyWord,amount=5,headers=None,timeout=60):
        self.name = 'Baidu'
        self.keyWord = keyWord
        self.amount = amount
        if headers != None:
            self.headers=headers

        self.url = 'http://www.baidu.com/s'
        self.keyTag = 'word'
        self.pageTag = 'pn'
        self.startIndex = 0
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


    def parser(self,soup):
        urls = []
        for div in soup.findAll('div', {'class': 'result'}):
            title = div.h3.a.getText()
            url = div.h3.a['href']
            urls.append({'title': title, 'link': url})
            
        return urls



