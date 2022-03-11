import requests


def get_content():
    # proxies = {
    #     "http": "http://localhost:1080",
    #     "https": "http://localhost:1080",
    # }
    proxies = {}

    url = "https://api.dler.io/sub?target=clash&new_name=true&url=https://jiang.netlify.app&insert=false&config=https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online.ini"
    file = requests.get(url, proxies=proxies)
    with open("pub/jiang.yaml", "wb") as f:
        f.write(file.content)
