import urllib.request
import urllib.parse

# 获取get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# 获取post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# url = "http://httpbin.org/post"
#
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
# }
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
url = "http://www.douban.com"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
