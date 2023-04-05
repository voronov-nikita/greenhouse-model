from requests import get

res = get("http://192.168.0.19")
print(res.text)