from tokenize import String

from fastapi import FastAPI
from datetime import datetime
from sqlalchemy.ext.asyncio import  create_async_engine
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from sqlalchemy import func, DateTime,Float
app = FastAPI()

# 1.创建异步引擎
ASYNC_DATABASE_URL = "mysql+aiomysql://root:@zyt0ZHC@localhost:3306/FastApiTest?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo = True,#可选，输出sql的日志
    pool_size = 10,#设置活跃的连接池的连接数量
    max_overflow = 20#允许额外的连接数
)

# 2.定义模型类：基类+ 模型类
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now(), comment="创建时间")#可选，设置默认值为当前时间
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now(),onupdate=func.now)#可选，设置更新时的默认值为当前时间

# 定义模型类
class Book(Base):
    __tablename__ = "book"

    id:Mapped[int] = mapped_column(primary_key=True, comment="书籍id")
    book_name: Mapped[str] = mapped_column(String(255), comment="书籍名称")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")#可选，设置价格为浮点型
    publisher: Mapped[str] = mapped_column(String(255), comment="出版社")


# 创建用户表
class User(DeclarativeBase):
    __tablename__ = "user"

    id:Mapped[int] = mapped_column(primary_key=True, comment="用户id")
    username: Mapped[str] = mapped_column(String(255), comment="用户名")
    password: Mapped[str] = mapped_column(String(255), comment="密码")

    # 3.创建表
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def startup_event():
    await create_tables()


@app.get("/")
async def root():
    return {"message":"hello"}

