import re
import json
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery


def get_content():
    url = "https://www.mattkaydiary.com/"
    # proxies = {
    #     "http": "http://localhost:1080",
    #     "https": "http://localhost:1080",
    # }
    proxies = {}

    data = requests.get(url, proxies=proxies)
    text = data.text
    soup = BeautifulSoup(text, "lxml")
    div_list = soup.findAll(
        name="a",
        attrs={"href": re.compile(r"https?:\/\/www\.mattkaydiary\.com\S+?\.html")},
    )
    a_list = []
    p = re.compile(r"\d{4}年\d{2}月\d{2}日更新")
    for val in div_list[:10]:
        if p.search(val.text):
            a_list.append(val.get("href"))
    new_v2ray_url = a_list[0]
    new_v2ray_data = requests.get(new_v2ray_url, proxies=proxies)
    new_v2ray_data_html = new_v2ray_data.text
    doc = PyQuery(new_v2ray_data_html)
    urls = re.findall(
        "https?://drive.google.com/uc\Sexport=download&id=\S+", doc.text()
    )
    for url in urls:
        file = requests.get(url, proxies=proxies)
        headers = json.dumps(dict(file.headers))
        if "yaml" in headers:
            with open("pub/mattkaydiary.yaml", "wb") as f:
                f.write(file.content)
