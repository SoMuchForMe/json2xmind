import requests

url = "http://localhost:18080/json2xmind"
payload = {
    "mindMap": {
        "title": "林默个人档案",
        "children": [
            {
                "title": "基本信息",
                "children": [
                    "出生日期：1992年8月15日凌晨3点22分",
                    "出生地点：杭州市第一妇幼保健院"
                ]
            },
            {
                "title": "教育背景",
                "children": [
                    "小学：杭州市文一街小学",
                    "初中：杭州第十三中学"
                ]
            }
        ]
    }
}

response = requests.post(url, json=payload)
print(response.json())