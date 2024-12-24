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
