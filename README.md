
# 介紹甚麼是 FastAPI ?

https://medium.com/seaniap/%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B-%E7%B0%A1%E5%96%AE%E6%98%93%E6%87%82-python%E6%96%B0%E6%89%8B%E7%9A%84fastapi%E4%B9%8B%E6%97%85-ebd09dc0167b


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



![](https://i.imgur.com/Vbl00ZD.png)


`main.py`

```python
from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
)  # Depends 用於依賴注入 HTTPException 用於拋出異常
from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, Product as ProductSchema
from database import engine, Base, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)  # 創建資料庫表


# 創建
@app.post("/products/", response_model=ProductCreate)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    # 創建產品時需要指定 id,因為資料庫會自動生成
    db_product = Product(
        name=product.name, description=product.description, price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # 刷新以確保獲取自動生成的 id
    return db_product


# 查詢所有商品 前10筆
@app.get("/products/", response_model=list[ProductSchema])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


# 查詢1筆商品
@app.get("/produts/{product_id}", response_model=ProductSchema)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# 更新
@app.put("/products/{product_id}", response_model=ProductSchema)
def update_product(
    product_id: int, product: ProductCreate, db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db.commit()
    db.refresh(db_product)
    return db_product


# 刪除
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": f"刪除{db_product.name}"}


# 刪除所有商品
@app.delete("/products/")
def delete_products(db: Session = Depends(get_db)):
    db.query(Product).delete()
    db.commit()
    return {"message": "已刪除所有商品"}


# 啟動服務 (省略uvicorn main:app --reload)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

```

`database.py`用於建立資料庫連結 與 繪畫
```python
from sqlalchemy import create_engine  # 匯入 create_engine 函數，用於建立資料庫引擎
from sqlalchemy.ext.declarative import (
    declarative_base,
)  # 匯入 declarative_base 函數，用於建立基礎類
from sqlalchemy.orm import sessionmaker  # 匯入 sessionmaker 函數，用於建立資料庫會話

# 設定資料庫的 URL，這裡使用的是 SQLite 資料庫
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 建立資料庫引擎，並設定 check_same_thread 參數為 False，允許多線程訪問
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 建立資料庫會話（Session）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 建立基礎類，所有的 ORM 模型都將繼承自這個基礎類
Base = declarative_base()


# 定義一個生成資料庫會話的函數 get_db，這個函數會在請求期間打開一個資料庫會話，並在請求結束後關閉
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```


- `autocommit=False`：這個參數設定會話不會自動提交變更。這意味著你需要手動提交變更，這樣可以更好地控制事務。
- `autoflush=False`：這個參數設定會話不會自動刷新。這意味著在查詢之前不會自動將所有掛起的變更發送到資料庫，這樣可以避免一些不必要的資料庫操作。


`models.py`用於建立資料欄位`products`

四個欄位分別是`id , name , description , price `
```python
from sqlalchemy import (
    Column,
    Integer,
    String,
)  # 匯入 Column, Integer, String 類，用於定義資料庫欄位
from database import Base  # 匯入 Base 類，用於繼承建立 ORM 模型


# 定義 Product 類，繼承自 Base 類，作為 ORM 模型
class Product(Base):
    __tablename__ = "products"  # 指定資料表名稱為 "products"

    id = Column(
        Integer, primary_key=True, index=True
    )  # 定義 id 欄位，整數型，主鍵，並建立索引
    name = Column(String, index=True)  # 定義 name 欄位，字串型，並建立索引
    description = Column(String)  # 定義 description 欄位，字串型
    price = Column(Integer)  # 定義 price 欄位，整數型

```


- `sessionmaker` 用來創建 `SessionLocal` 工廠，這個工廠可以生成 `Session` 物件。
- `SessionLocal()` 用來創建 `Session` 物件 `db`，這個物件可以用來與資料庫進行操作。



`schemas.py` 用於
```python
from pydantic import BaseModel


# 定義 ProductBase 類，作為 Product 的基礎類
class ProductBase(BaseModel):
    name: str
    description: str
    price: int


# 定義 ProductCreate 類，繼承自 ProductBase，用於創建 Product
class ProductCreate(ProductBase):
    pass


# 定義 Product 類，繼承自 ProductBase，並添加 id 欄位
class Product(ProductBase):
    id: int

    class Config:
		# orm_mode = True  # 設定 orm_mode 為 True，允許 Pydantic 模型與 ORM 模型互動
        from_attributes = True  # Updated from orm_mode to from_attributes for Pydantic V2 compatibility

```


##### 遇到Error
* 'orm_mode' has been renamed to 'from_attributes'
  warnings.warn(message, UserWarning)

解決方案 : 
```python
class Product(ProductBase):
    id: int

    class Config:
        # orm_mode = True  # Pydantic v1 版本 : 設定 orm_mode 為 True，允許 Pydantic 模型與 ORM 模型互動
        from_attributes = True  # Pydantic v2 版本 : 設定 from_attributes 為 True，允許 Pydantic 模型與 ORM 模型互動
```
	使用`from_attributes = True  # Updated from orm_mode to from_attributes for Pydantic V2 compatibility `





```python
Base.metadata.create_all(bind=engine)  # 創建資料庫表
```
- 自動生成`sqllist` 檔案，在路徑 SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

![](https://i.imgur.com/t1Goym2.png)

### 加入自動測試 pytest 

```cmd 
uv pip install pytest httpx
```

`test_main.py`用來測試及發送資料
```python
import pytest
from fastapi.testclient import TestClient
from main import app
from database import init_db, clear_db

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # 初始化資料庫
    init_db()
    yield
    # 清理資料庫（如果需要）
    # clear_db()


def test_create_product():
    response = client.post(
        "/products/",
        json={"name": "Test Product", "description": "Test Description", "price": 100},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
    assert response.json()["description"] == "Test Description"
    assert response.json()["price"] == 100


def test_read_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_product():
    # 先創建一個產品
    response = client.post(
        "/products/",
        json={
            "name": "Another Product",
            "description": "Another Description",
            "price": 200,
        },
    )
    assert response.status_code == 200
    product_id = response.json()["id"]

    # 查詢該產品
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Another Product"
    assert response.json()["description"] == "Another Description"
    assert response.json()["price"] == 200


def test_update_product():
    # 先創建一個產品
    response = client.post(
        "/products/",
        json={
            "name": "Update Product",
            "description": "Update Description",
            "price": 300,
        },
    )
    assert response.status_code == 200
    product_id = response.json()["id"]

    # 更新該產品
    response = client.put(
        f"/products/{product_id}",
        json={
            "name": "Updated Product",
            "description": "Updated Description",
            "price": 400,
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"
    assert response.json()["description"] == "Updated Description"
    assert response.json()["price"] == 400


def test_delete_product():
    # 先創建一個產品
    response = client.post(
        "/products/",
        json={
            "name": "Delete Product",
            "description": "Delete Description",
            "price": 500,
        },
    )
    assert response.status_code == 200
    product_id = response.json()["id"]

    # 刪除該產品
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["message"] == f"刪除Delete Product"

```


# 08_FastAPI_JWT用戶認證與授權機制實作


# ![](https://i.imgur.com/CLPsQyY.png)


![](https://i.imgur.com/ruXmbBl.png)


![](https://i.imgur.com/whcHdyC.png)


![](https://i.imgur.com/rpBcyaH.png)



![](https://i.imgur.com/rtgjNfW.png)


![](https://i.imgur.com/212IQJv.png)


![](https://i.imgur.com/bS3vYqG.png)


![](https://i.imgur.com/etjkdIt.png)

```cmd
uv run pip install pyjwt passlib
```

### **PyJWT** 
是一個專門用來處理 **JSON Web Token (JWT)** 的 Python 套件，功能包括生成、解析、驗證 JWT。

#### **用途**：

- **生成 JWT**：用於身份驗證和信息安全傳遞，常用於 Web API 的 Token-based 認證。
- **驗證 JWT**：解析並驗證 Token 的有效性（簽名是否正確，是否過期）。
- **支持演算法**：支援多種演算法（如 `HS256`, `RS256`）進行簽名和驗證。


### **passlib**  
是一個靈活且強大的密碼雜湊處理庫，支援多種密碼雜湊演算法，適合用於密碼存儲和驗證。

#### **用途**：

- **安全存儲密碼**：通過加鹽和強加密算法（如 bcrypt）保護密碼。
- **驗證密碼**：驗證使用者輸入的密碼是否匹配存儲的雜湊值。
- **演算法支持**：支援多種雜湊演算法（如 `bcrypt`, `argon2`, `sha256_crypt`）。


`models.py`新增**class User(Base):**

```python
from sqlalchemy import (
    Column,
    Integer,
    String,
)  # 匯入 Column, Integer, String 類，用於定義資料庫欄位
from database import Base  # 匯入 Base 類，用於繼承建立 ORM 模型


# 定義 Product 類，繼承自 Base 類，作為 ORM 模型
class Product(Base):
    __tablename__ = "products"  # 指定資料表名稱為 "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # 定義 name 欄位，字串型，並建立索引
    description = Column(String)  # 定義 description 欄位，字串型
    price = Column(Integer)  # 定義 price 欄位，整數型


# 定義 User 類，繼承自 Base 類，作為 ORM 模型
class User(Base):
    __tablename__ = "users"  # 指定資料表名稱為 "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # 用於角色管理，默認為普通用戶
```

`schemas.py` 新增**User 類型**

```python
from pydantic import BaseModel


# 定義 ProductBase 類，作為 Product 的基礎類
class ProductBase(BaseModel):
    name: str
    description: str
    price: int


# 定義 ProductCreate 類，繼承自 ProductBase，用於創建 Product
class ProductCreate(ProductBase):
    pass


# 定義 Product 類，繼承自 ProductBase，並添加 id 欄位
class Product(ProductBase):
    id: int

    class Config:
        # orm_mode = True  # Pydantic v1 版本 : 設定 orm_mode 為 True，允許 Pydantic 模型與 ORM 模型互動
        from_attributes = True  # Pydantic v2 版本 : 設定 from_attributes 為 True，允許 Pydantic 模型與 ORM 模型互動


# 定義 User 類型
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str  # 用於測試時提供密碼


class User(UserBase):
    id: int
    role: str  # 返回用戶包含的角色資訊

    class Config:
        from_attributes = True

```

`main.py` 
@app.post("/register/", response_model=UserSchema)
def create_access_token(data: dict, expires_delta: timedelta):
@app.post("/login")
```python
from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
)  # Depends 用於依賴注入 HTTPException 用於拋出異常
from sqlalchemy.orm import Session
from models import Product, User
from schemas import ProductCreate, Product as ProductSchema
from schemas import UserCreate, User as UserSchema

from database import engine, Base, get_db, init_db
import jwt
from passlib.context import CryptContext  # 處理密碼的庫
from datetime import datetime, timedelta, timezone

app = FastAPI()

pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto"
)  # 設置加密方式 , bcrypt 是一種加密方式 , deprecated="auto" 表示自動選擇加密方式

# Base.metadata.create_all(bind=engine)  # 創建資料庫表
init_db()  # 初始化資料庫

"""
以下為 User 的 操作
1.創建用戶
2.

"""


def hash_password(password: str):
    return pwd_context.hash(password)


# 創建用戶
@app.post("/register/", response_model=UserSchema)
def create_product(user: UserCreate, db: Session = Depends(get_db)):
    # 創建產品時需要指定 id,因為資料庫會自動生成
    hash_password = hash_password(user.password)
    db_user = User(
        username=user.name, hashed_password=hash_password
    )  # hashed_password 儲存加密的密碼

    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # 刷新以確保獲取自動生成的 id
    return db_user


SECRET_KEY = "8fIxtm15HwDDpJc4Zvz01iorhOHNS2hIgK--lsrdJo4"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = (
        datetime.now(timezone.utc) + expires_delta
        if expires_delta
        else datetime.now(timezone.utc) + timedelta(minutes=15)
    )  # 代表15分鐘後過期
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == username.name).first()  # 查詢用戶
    if not db_user or not pwd_context.verify(password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(
        data={"sub": username.name, "role": db_user.role},
        expires_delta=timedelta(minutes=15),
    )
    return {"access_token": access_token, "token_type": "bearer"}


"""
以下為 products 的 CRUD 操作
1.創建商品
2.查詢所有商品
3.查詢1筆商品
4.更新商品
5.刪除商品
6.刪除所有商品
"""


# 創建
@app.post("/products/", response_model=ProductSchema)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    # 創建產品時需要指定 id,因為資料庫會自動生成
    db_product = Product(
        name=product.name, description=product.description, price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  # 刷新以確保獲取自動生成的 id
    return db_product


# 查詢所有商品 前10筆
@app.get("/products/", response_model=list[ProductSchema])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


# 查詢1筆商品
@app.get("/products/{product_id}", response_model=ProductSchema)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# 更新
@app.put("/products/{product_id}", response_model=ProductSchema)
def update_product(
    product_id: int, product: ProductCreate, db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db.commit()
    db.refresh(db_product)
    return db_product


# 刪除
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": f"刪除{db_product.name}"}


# 刪除所有商品
@app.delete("/products/")
def delete_products(db: Session = Depends(get_db)):
    db.query(Product).delete()
    db.commit()
    return {"message": "已刪除所有商品"}


# 啟動服務 (省略uvicorn main:app --reload)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

```



```python
datetime.utcnow() # 已棄用 
datetime.now(timezone.utc) # 修正
```
