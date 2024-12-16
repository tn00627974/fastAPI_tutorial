from fastapi import FastAPI
from fastapi import Query  # 用來設定查詢參數
from pydantic import BaseModel  #
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# 掛載 static 資料夾處理靜態檔案
app.mount("/static", StaticFiles(directory="static"), name="static")

# 建立 Jinja2 模板引擎的實例,指定模板所在目錄
templates = Jinja2Templates(directory="templates")


# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}
@app.get("/")
def read_index(request: Request):
    data = {"title": "網站", "user": "Ulysses"}
    # 使用 Jinja2 渲染模板
    return templates.TemplateResponse(
        # "01_index.html", {"request": request, "data": data}
        "02_index.html",
        {"request": request, "data": data},
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: str = None):
    return {"item_id": item_id, "query": query}


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


class Item(BaseModel):
    name: str
    price: float
    description: str = None


@app.post("/item/")
async def create_item(item: Item):
    return item
