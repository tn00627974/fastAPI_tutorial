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
        # orm_mode = True  # 設定 orm_mode 為 True，允許 Pydantic 模型與 ORM 模型互動
        from_attributes = True  # Updated from orm_mode to from_attributes for Pydantic V2 compatibility
