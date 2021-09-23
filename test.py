from psearcher import Baidu
from psearcher import Bing
import requests

session = requests.session()
engine = Baidu(keyWord='哔哩哔哩', amount=10, timeout=60, session=session)
# engine = Bing(keyWord='蝙蝠侠 黑暗骑士', amount=20, timeout=20)
result = engine.search()
print(result)
