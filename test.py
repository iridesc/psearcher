from psearcher import Baidu
from psearcher import Bing

# engine = Baidu(keyWord='蝙蝠侠', amount=20)
engine = Bing(keyWord='蝙蝠侠 黑暗骑士',amount=20)
result = engine.Search()
print(result)
