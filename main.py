from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder  # 关键转换工具
import json2xmind8
app = FastAPI()


# 定义请求体模型
class MindMapRequest(BaseModel):
    mindMap: dict  # 直接声明为字典类型


@app.post("/json2xmind8")
async def convert_mindmap(request: MindMapRequest):
    # 直接访问模型属性
    mindmap_dict = request.mindMap
    json2xmind = json2xmind8.json2xmind(mindmap_dict)
    return {"status": "success", "mindmap_path": json2xmind}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=18080)