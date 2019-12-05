import requests, time
import random
from retry import retry
from bs4 import BeautifulSoup
from loger import setting, makelog

class BaseEngine(object):
    name = 'BaseEngine'
    timeout=60
    session=requests.session()
    keyWord = ''
    amount = 5
    searchType = 'base'
    results = []
    nextPage = 0
    typeKit = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",   
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }

    def parser(self, soup):
        makelog('You must rewrite your parser!',1)
        return None

    def getUrlParmas(self):
        makelog('You must rewrite your getUrlParmas!',1)
        return None
  

    def AddResult(self, url, params):
        @retry(tries=3, delay=random.random()*2)
        def getPageResults():
            def net():
                r = self.session.get(url, params=params, headers=self.headers)
                r.raise_for_status
                return r
        
            try:
                r = net()
            except:
                makelog('Connection error!',2)

            soup = BeautifulSoup(r.text, 'html.parser')
            pageResults = self.parser(soup)
            if len(pageResults) == 0:
                makelog('PageResult count is 0!',2)
                makelog(r.url)
                with open('error.html', 'w') as f:
                    f.write(r.text)
                raise
            else:
                return pageResults

        makelog('{} {} {} {}'.format(
                                self.name,
                                self.keyWord,
                                self.nextPage,
                                len(self.results),
                                ))
        try:
            pageResults = getPageResults()
            self.results.extend(pageResults)
            makelog('Got page results!',4)
        except:
            makelog("Can't get page !",1)


    def Search(self):
        startTime=time.time()
        while len(self.results) < self.amount:
            url, params = self.getUrlParmas()
            self.AddResult(url, params)
            
            # Timeout  
            if time.time() - startTime > self.timeout:
                makelog('Search Timeout!',1)
                break
                

        return self.results
