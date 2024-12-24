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
