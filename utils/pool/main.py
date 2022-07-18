from crawl import get_file_list, get_proxies
from parse import parse, makeclash
from clash import push
from multiprocessing import Process, Manager
from yaml.loader import SafeLoader
import time
import yaml
import requests

headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive'}

def fetch(proxy_list, filename):
    current_date = time.strftime("%Y_%m_%d", time.localtime())
    baseurl = 'https://raw.githubusercontent.com/changfengoss/pub/main/data/'
    working = yaml.safe_load(requests.get(url=baseurl + current_date + '/' + filename, timeout=30).text)
    data_out = []
    for x in working['proxies']:
        data_out.append(x)
    proxy_list.append(data_out)

def url(proxy_list, link):
    try:
        data_out=[]
        working = yaml.safe_load(requests.get(url=link,timeout=30, headers=headers).text)
        for x in working['proxies']:
            data_out.append(x)
        proxy_list.append(data_out)
    except:
        print("Error in Collecting "+ link )

proxy_list=[]
if __name__ == '__main__':
    with Manager() as manager:
        proxy_list = manager.list()
        current_date = time.strftime("%Y_%m_%d", time.localtime())
        print("Today is: " + current_date)
        with open('config.yaml', 'r') as reader:
            config = yaml.load(reader,Loader=SafeLoader)
        subscribe_links = config['sub']
        directories, total = get_file_list()
        data = parse(directories)
        try:
            sfiles = len(subscribe_links)
            tfiles = len(data[current_date]) + len(subscribe_links)
            processes=[]
            filenames = list()
            filenames = data[current_date]
        except KeyError:
            print("Success: " + str(sfiles) + " Clash files")
        else:
            print("Success: " + str(tfiles) + " Clash files")

        processes=[]
        try:
            start = time.time()
            for i in subscribe_links:
                p = Process(target=url, args=(proxy_list, i))
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            # for i in filenames:
            #     p = Process(target=fetch, args=(proxy_list, i))
            #     p.start()
            #     processes.append(p)
            # for p in processes:
            #     p.join()
            end = time.time()
            print("Collecting in " + "{:.2f}".format(end-start) + " seconds")
        except:
            end = time.time()
            print("Collecting in " + "{:.2f}".format(end-start) + " seconds")

        proxy_list=list(proxy_list)
        proxies = makeclash(proxy_list)
        push(proxies)
    """
    for i in tqdm(range(int(tfiles)), desc="Download"):
        proxy_list.append(get_proxies(current_date, data[current_date][i]))
    """
