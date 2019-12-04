import requests, time
import random
from retry import retry
from bs4 import BeautifulSoup

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
        print('You must rewrite your parser!')
        return None

    def getUrlParmas(self):
        print('You must rewrite your getUrlParmas!')
        return None
  

    def AddResult(self, url, params):
        print(random.random()*2)
        @retry(tries=3, delay=random.random()*2)
        def getPageResults():
            def net():
                r = self.session.get(url, params=params, headers=self.headers)
                r.raise_for_status
                return r
        
            try:
                r = net()
            except:
                print('Error！Connection error!')

            soup = BeautifulSoup(r.text, 'html.parser')
            pageResults = self.parser(soup)
            if len(pageResults) == 0:
                print('Error！ When parser PageResult count is 0!')
                print(r.url)
                with open('error.html', 'w') as f:
                    f.write(r.text)
                raise
            else:
                return pageResults

        print('{} {} {} {}'.format(
                                self.name,
                                self.keyWord,
                                self.nextPage,
                                len(self.results),
                                ))
        try:
            pageResults = getPageResults()
            self.results.extend(pageResults)
            print('Scuess! When get page results!')
        except:
            print('Error! When get page results!')


    def Search(self):
        startTime=time.time()
        while len(self.results) < self.amount:
            url, params = self.getUrlParmas()
            self.AddResult(url, params)
            
            # Timeout  
            if time.time() - startTime > self.timeout:
                print('Error! Timeout!')
                break
                

        return self.results
