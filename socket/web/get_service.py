#! /usr/bin/env python3
# coding=utf-8

''''
python搭建http接口get
测试get接口
curl localhost:8080/test/a=1/b=2
'''

from fastapi import FastAPI
 
app = FastAPI()
 
@app.get('/test/a={a}/b={b}')
def calculate(a: int=None, b: int=None):
    c = a + b
    res = {"res":c}
    return res
 
 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)
