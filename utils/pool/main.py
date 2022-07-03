from crawl import get_file_list, get_proxies
from parse import parse, makeclash
from clash import push
from multiprocessing import Process, Manager
from yaml.loader import SafeLoader
import time
import yaml
import requests

def fetch(proxy_list, filename):
    current_date = time.strftime("%Y_%m_%d", time.localtime())
    baseurl = 'https://raw.githubusercontent.com/changfengoss/pub/main/data/'
    working = yaml.safe_load(requests.get(url=baseurl + current_date + '/' + filename, ).text)
    data_out = []
    for x in working['proxies']:
        data_out.append(x)
    proxy_list.append(data_out)

def url(proxy_list, link):
    try:
        data_out=[]
        working = yaml.safe_load(requests.get(url=link).text)
        for x in working['proxies']:
            data_out.append(x)
        proxy_list.append(data_out)
    except:
        print("Error in fetching "+ link )

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
            tfiles = len(data[current_date]) + len(subscribe_links)
            processes=[]
            filenames = list()
            filenames = data[current_date]
        except KeyError:
            print("Failed: changfengoos/pub库里没有Clash配置文件可以嫖")
        else:
            print("Success: changfengoos/pub库里有" + str(tfiles) + "个Clash配置文件可以嫖")

        processes=[]
        try:
            for i in subscribe_links:
                p = Process(target=url, args=(proxy_list, i))
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            start = time.time()
            for i in filenames:
                p = Process(target=fetch, args=(proxy_list, i))
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            end = time.time()
            print("爬到了节点 in " + "{:.2f}".format(end-start) + " seconds")
        except:
            end = time.time()
            print("没有爬到节点 in " + "{:.2f}".format(end-start) + " seconds")

        proxy_list=list(proxy_list)
        proxies = makeclash(proxy_list)
        push(proxies)
    """
    for i in tqdm(range(int(tfiles)), desc="Download"):
        proxy_list.append(get_proxies(current_date, data[current_date][i]))
    """
