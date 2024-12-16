https://medium.com/seaniap/%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B-%E7%B0%A1%E5%96%AE%E6%98%93%E6%87%82-python%E6%96%B0%E6%89%8B%E7%9A%84fastapi%E4%B9%8B%E6%97%85-ebd09dc0167b

# 介紹甚麼是 FastAPI ?



特點 : 
1.速度
2.易用性
3.自動化文件
4.簡潔易懂

![](https://i.imgur.com/ohoZiyo.png)



![](https://i.imgur.com/aPK5lnM.png)


前端開發者 : 呼叫API傳入參數USER ID

![](https://i.imgur.com/QZZdFEb.png)


- 後端開發者 : 

![](https://i.imgur.com/rL21Ba8.png)



![](https://i.imgur.com/qurgtRH.png)

安裝 fastapi uvicorn
接著我們還需要一個ASGI伺服器，這裡我們使用`uvicorn`。您可以用透過下面的指令來安裝：
```cmd
pip install fastapi uvicorn
```

啟動應用程式
```cmd
uvicorn main:app --reload
```

註：以上的安裝，強烈建議在安裝前先建立一個虛擬環境。並在虛擬環境下安裝各個套件。

![](https://i.imgur.com/xTWlzyF.png)



# 02_FastAPI_自動生成API文件與單元測試 [#python](https://www.youtube.com/hashtag/python) [#fastapi](https://www.youtube.com/hashtag/fastapi)

[](https://www.youtube.com/@changlunglung)

![](https://i.imgur.com/wHP3wAQ.png)



網頁輸入 http://127.0.0.1:8000/docs 產成文件

點擊 Try it out 
![](https://i.imgur.com/wxg70XE.png)


Execute
![](https://i.imgur.com/Gd0psBw.png)

會得到回傳內容 Responses

![](https://i.imgur.com/SMf34Wp.png)


創建另一個呼叫函數

```python
@app.get("/items/{item_id}")
async def read_item(item_id : int , query : str = None ):
    return {"message":"Hello, FastAPI!"} 
```

更新瀏覽器，可以看到GET方法多了一個

![](https://i.imgur.com/01T7rWl.png)


進行驗證 

item_id 輸入 1
query 輸入 test

![](https://i.imgur.com/38cRyON.png)

![](https://i.imgur.com/hXf3x4e.png)



接著使用 pytest 來單元測試

```cmd
pip install pytest
```

```cmd
pip install httpx
```

- 創建一個`test_api.py`程式碼

```python
from fastapi.testclient import TestClient
from main import app # main的app

client = TestClient(app) 

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200 
    assert response.json() == {"message":"Hello, FastAPI!"}
```

接著來單元測試
-v : 可以看到更多內容
```cmd
pytest .\test_api.py -v
```


![](https://i.imgur.com/NYG9kk0.png)
結果 PASSED 為正確

![](https://i.imgur.com/UHvFwS2.png)
假如測試結果不符合
這邊可以看到 
正確為{"message":"Hello, FastAPI!"}  
跟
{"message":"999hello, FastAPI!"}   

---

來打印出json格式
-s 為`print()` 函數的輸出選項

```cmd
pytest .\test_api.py -s
```

```python
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200 
    print("測試json",response.json())
```


可以看到json輸出了

![](https://i.imgur.com/iNIBL8p.png)


# 03_FastAPI_詳解路徑參數與查詢參數

- 路徑參數 ?
- 查詢參數 ?

![](https://i.imgur.com/yfgjVtg.png)


![](https://i.imgur.com/vjMDmhs.png)




![](https://i.imgur.com/7wsj1Ol.png)


 main.py 加上 products 的查詢參數
```python
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id, "details": "這是產品的明細"}

# Query(0,ge=0) 不得小於0
# Query(10000,le=10000) 最多是10000 ,le為 超出10000會有警示
@app.get("/products/")
async def search_products(
    category: str,
    price_min: int = Query(0, ge=0),
    price_max: int = Query(10000, le=10000),
    sort_by: str = "price",
):
    return {
        "category": category,
        "price_min": price_min,
        "price_max": price_max,
        "sort_by": sort_by,
        "results": "Here are the filtered products",
    }
```

# 04_FastAPI 資料驗證與模式設計


![](https://i.imgur.com/AuJgsoF.png)


## 資料驗證

- 保證資料完整性與一致性
- 預防安全漏洞
- 減少錯誤與系統崩潰
- 確保商業規則的遵守
- 減少後端負擔


![](https://i.imgur.com/SfdTAJU.png)


![](https://i.imgur.com/I9GaRl0.png)


![](https://i.imgur.com/sCDP2La.png)


![](https://i.imgur.com/0POG950.png)



![](https://i.imgur.com/KwvBVF0.png)



![](https://i.imgur.com/W7pUNKJ.png)


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	name : str 
	price : float
	description : str = None 

@app.post("/item/")
async def create_item(item:Item):
	return item
```

```cmd
uvicorn main:app --reload
```


使用 POST進行Item的資料驗證

![](https://i.imgur.com/rMV6w4Y.png)


![](https://i.imgur.com/kCwTo19.png)




![](https://i.imgur.com/qQpKcpx.png)

若是資料錯誤會出現422
代表資料不符合格式進行報錯


![](https://i.imgur.com/ArAbU9h.png)




# 05_FastAPI靜態檔案處理與模板結合實作

![](https://i.imgur.com/m4DJZPo.png)



![](https://i.imgur.com/AXtOZHK.png)

創建 static/images/yourpicture

- main_py
```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# 掛載 static 資料夾處理靜態檔案
app.mount("/static", StaticFiles(directory="static"), name="static")

# 建立 Jinja2 模板引擎的實例,指定模板所在目錄
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_index(request: Request):
    data = {"title": "使用者", "user": "張成龍"} # 對應02_index.html的 {{ data.user }} 的 {{ data.title }}
    # 使用 Jinja2 渲染模板
    return templates.TemplateResponse("01_index.html", {"request": request, "data": data})

```


![](https://i.imgur.com/GnxXB3b.png)

創建 templates 放入以下兩個html
- 01_index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatibl e" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FastAPI 靜態檔案與模板範例</title>
  <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
  <h1>歡迎來到 FastAPI 範例頁面</h1>
  <img src="/static/images/01.png" alt="Logo"> <!--01.png請替換成你的image name -->
</body>
</html>
```
- 02_index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatibl e" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FastAPI 靜態檔案與模板範例</title>
  <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
  <!-- <h1>歡迎來到 FastAPI 範例頁面</h1> -->
  <h1>歡迎來到 {{ data.user }} 的 {{ data.title }}</h1>
  <img src="/static/images/Jackie.png" alt="Logo">
</body>
</html>
```

啟動應用程式
```cmd
uvicorn main:app --reload
```

![](https://i.imgur.com/tp4cpfS.png)


