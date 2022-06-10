import requests
import json
import yaml
import time
def get_file_list():
    try:
        start = time.time()
        rawdata = json.loads(requests.get('https://api.github.com/repos/changfengoss/pub/git/trees/main?recursive=1').text)
        data = rawdata['tree']
        dirlist = []
        count = 0
        for x in data:
            dirlist.append(data[count]['path'])
            count = count +1
        end = time.time()
        print("Fetch changfengoss/pub succeeded in " + "{:.2f}".format(end-start) + " seconds")
        return dirlist, count
    except:
        print("Failed to fetch proxies from changfengoss/pub")

def get_proxies(date, file):
    baseurl = 'https://raw.githubusercontent.com/changfengoss/pub/main/data/'
    working = yaml.safe_load(requests.get(url=baseurl+date+'/'+file,).text)
    data_out = []
    for x in working['proxies']:
        data_out.append(x)
    return data_out
