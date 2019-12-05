# psearcher

pseacher 是一个为python3打造的网页搜索借口。
psearcher is a web search interface for python3.
目前支持 Baidu Bing
now support Baidu Bing 

```
from psearcher import Baidu
from psearcher import Bing

engine = Baidu(keyWord='蝙蝠侠', amount=20)
engine = Bing(keyWord='蝙蝠侠 黑暗骑士',amount=20)
result = engine.Search()
print(result)
```

19.12.25 使用loger控制输出 
19.12.25 use loger control output