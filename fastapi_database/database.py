from sqlalchemy import create_engine  #
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 資料庫 URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 初始化資料庫引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 建立會話工廠
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 宣告基類
Base = declarative_base()


# 自動創建資料表
def init_db():
    import models  # 確保模型被載入

    Base.metadata.create_all(bind=engine)


# 清理資料表
def clear_db():
    Base.metadata.drop_all(bind=engine)


# 資料庫連接的依賴
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
