from fastapi import FastAPI,Depends,Query
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse

app = FastAPI()

#定义实体类
class User(BaseModel):
    username: str = Field(default = "测试默认", min_length=2,max_length=10,description="用户名")
    password: str = Field(default="123456", min_length=6,max_length=10,description="密码")

# 定义图书实体
class Book(BaseModel):
    # 在 Pydantic 中，判断字段不能为空（即必填）：不设置 default，且类型非 Optional。
    # 使用 ... 可以显式标记该字段为必填项。
    book_name: str = Field(..., min_length=2, max_length=20, description="书名，不能为空")
    book_author: str = Field(..., min_length=2, max_length=10, description="作者，不能为空")
    book_community: str = Field(default="黑马社区", description="社区")
    book_price: float = Field(..., gt=0, description="价格，不能为空且必须大于0")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/register")
async def register(user:User):
    return user

@app.post("/book/add")
async def addBook(book:Book):
    return book

# 直接在装饰器中定义响应类型
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>一级标题</h1>"


from fastapi.responses import FileResponse
# 返回一张图片的内容
@app.get("/file", response_class=FileResponse)
async def get_file():
    path ="./file/1.jpg"
    return path

# 用到httpException
from fastapi import  HTTPException
@app.get("/new/{id}")
async def get_news (id:int):
    id_list = [1,3,4,5,6]
    if id not in id_list:
        raise HTTPException(status_code=404,detail="您查找的新闻不存在")
    return {"id":id}
#
# # 采用中间件的使用
# @app.middleware("http")
# async def middleware1(request,call_next):
#     print("中间件1 start")
#     response = await call_next(request)
#     print("中间件1 end")
#     return response
#
#
# @app.middleware("http")
# async def middleware2(request,call_next):
#     print("中间件2 start")
#     response = await call_next(request)
#     print("中间件2 end")
#     return response


# 依赖注入
async def common_parameters(
    skip: int = Query(default=0,ge=0),
    limit: int = Query(default=10, le=100)
):
    return {"skip": skip, "limit": limit}

@app.get("/news/list")
async def get_news_list(
    commons = Depends(common_parameters)
):
    return commons