import urllib.request
import re

url = 'https://ibex.co.kr/kr/product/mono/ibex-light/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = set(re.findall(r'src=["\'](https?://[^\'"]+\.(?:jpg|png|jpeg|gif))["\']', html))
    for img in images:
        print(img)
except Exception as e:
    print(e)
