import requests

url="https://zipcloud.ibsnet.co.jp/api/search?zipcode=1000001"
response = requests.get(url)
print(response.text)


