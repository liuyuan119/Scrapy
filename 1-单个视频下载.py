import requests

url = "http://v11-tt.ixigua.com/3eeda4ff03851e6182b3174471c8e466/5b4c1f11/video/m/220f6ab8f1574504b929e8e6c6b76e03ed31158ff600000df2cb81b33c7/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36'
}

res = requests.get(url=url, headers=headers)

# print(res.text)


with open("jinri.mp4", 'wb') as fw:
    fw.write(res.content)