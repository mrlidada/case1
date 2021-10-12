import requests

# 请求对象
rep = requests.request()
# 返回字符串数据
print(rep.text)

# 返回字节格式数据
print(rep.content)

# 返回json格式数据
print(rep.json())

