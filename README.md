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


# 06_FastAPI x Vue js前後端分離設計

前後端分離 ?


![](https://i.imgur.com/BwP0lzR.png)


![](https://i.imgur.com/bVVKFxT.png)


![](https://i.imgur.com/UaYsawX.png)

下載nodejs
https://nodejs.org/zh-tw

- 查看`node`是否安裝
```cmd
node -v 
```

```cmd
npm install -g @vue/cli
```

- 查看`vue`是否安裝
	顯示`@vue/cli 5.0.8`
	代表安裝5.0.8版本
	
```cmd
vue -version
```

- cd `C:\Users\tn006\Desktop\fastAPI`(替換成你的專案路徑)
- 開始創建vue的專案在fastAPI的資料夾下

```cmd
vue create fastapi-frontend
```

![](https://i.imgur.com/sSprRpg.png)

選項分為 :
- [1] Vue3 (這邊選擇 Vue 3 版本作為專案使用)
- [ ] Vue2 
- [ ] 提供更細緻的自定義能力

[Vue2與Vue3差異](https://hackmd.io/@grayshine/BJ6gbNV8F/%2FQvsOBO9QQPGTqaYO0Cj4TQ)

專案啟動中...

![](https://i.imgur.com/7TLRSqw.png)


```cmd
npm run serve
```

打開瀏覽器

```
http://localhost:8080/
```

預設vue專案的啟動畫面

![](https://i.imgur.com/6NsigoZ.png)

---
接著新建在 `/src/components/Home.vue` 

![](https://i.imgur.com/PQJCOtj.png)

- Home.vue 程式碼
```vue
<template>
  <div>
    <h1>{{ message }}</h1>
    <button @click="getData">Get Data</button>
    <button @click="posthData">Post Data</button>
  </div>
</template>

<script>
export default {
  name: "DataComponent",
  data() {
    return {
      message: "This is some default message.",
    };
  },

  methods: {
    async getData() {
      try {
        const response = await fetch("http://127.0.0.1:8000/");
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },

    async posthData() {
      try {
        const item = {
          name: "Test",
          price: 100.0,
          description: "This is an example item.",
        };
        const response = await fetch("http://127.0.0.1:8000/items", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(item),
        });
        const data = await response.json();
        this.message = `name: "${data.item_name}", price: ${data.item_price}`;
        // this.message = data.item_name;
      } catch (error) {
        console.error("Error posting data:", error);
      }
    },
  },
};
</script>
```

 首先先建立兩個button去對應 `getData` 跟`posthData`funtion
```vue
    <button @click="getData">Get Data</button>
    <button @click="posthData">Post Data</button>
```

```vue
<script>
export default {
  name: "DataComponent",
  data() {
    return {
      message: "This is some default message.",
    };
  },

  methods: {
    async getData() {
      try {
        const response = await fetch("http://127.0.0.1:8000/");
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },

    async posthData() {
      try {
        const item = {
          name: "Test",
          price: 100.0,
          description: "This is an example item.",
        };
        const response = await fetch("http://127.0.0.1:8000/items", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(item),
        });
        const data = await response.json();
        this.message = `name: "${data.item_name}", price: ${data.item_price}`;
        // this.message = data.item_name;
      } catch (error) {
        console.error("Error posting data:", error);
      }
    },
  },
};
</script>
```


接著修改啟動檔`App.vue`
	修改成 `import Home from "./components/Home";`
	修改成 `export default {`
	`name: "App",`
	  `components: {`
	 ``   Home,`
	``  },`
	`};`
```vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <Home />
  </div>
</template>

<script>
import Home from "./components/Home";

export default {
  name: "App",
  components: {
    Home,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

![](https://i.imgur.com/pAY73wS.png)

### 設置了跨域資源共享(CORS)


讓vue 與 fastAPI的 8000端口進行fetch `127.0.0.1:8000`
```python
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允許跨域請求(這裡定義了來源、憑證和方法)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 或改成你需要的外部 或 內部 IP
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    data = {"title": "網站", "user": "Ulysses"}
    message = f"{data['user']} 的{data['title']}"
    return {"message": message}
```


這段程式碼使用 FastAPI 框架創建了一個 web 應用程序,並設置了跨域資源共享(CORS)中間件。

主要設置包括:

1. 允許來自 `http://localhost:8080` 的跨域請求。
2. 允許使用憑證進行跨域請求。
3. 允許使用所有 HTTP 方法進行跨域請求。
4. 允許使用所有 HTTP 標頭進行跨域請求。


![](https://i.imgur.com/STAZA71.png)


![](https://i.imgur.com/w23Gh4b.png)


# 07_FastAPI連結資料庫教學


![](https://i.imgur.com/Z5Awpq2.png)



![](https://i.imgur.com/mnup62c.png)


![](https://i.imgur.com/ZNLDUvf.png)

### 使用 UV 虛擬環境 

**uv 初始化+專案名稱**
```cmd
uv init fastapi_database
cd .\fastapi_database\
```

**uv安裝依賴套件** 
```
uv add fastapi uvicorn sqlalchemy pydantic
```

**若要移除相關依賴你也可以使用 `remove`
```
uv remove uvicorn
```

- **uv 啟動 uvicorn**
```cmd
uv run uvicorn hello:app --reload
```

```cmd
uv run python --verison
```

**uv更改python版本的方式**

打開 `.python-version`
將`3.12` 修改成 `3.9`
再執行以下指令
```
uv sync
```

![](https://i.imgur.com/Ev39jF0.png)

![](https://i.imgur.com/aG3u9d6.png)





