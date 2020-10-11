import requests
import time
from bs4 import BeautifulSoup
from urllib import request, parse
import urllib
url = "https://jobs.51job.com/shanghai-mhq/122802043.html?s=01&t=0"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363 "
}
html = requests.get(url, headers=headers).content.decode('gbk')
print(html)


