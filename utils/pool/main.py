import time
import yaml
import requests
from crawl import get_file_list, get_proxies
from parse import parse, makeclash
from clash import push
from multiprocessing import Process, Manager
from yaml.loader import SafeLoader

headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive', 'User-Agent': 'Clash'}

def local(proxy_list, file):
    try:
        with open(file, 'r') as reader:
            working = yaml.safe_load(reader)
        data_out = []
        for x in working['proxies']:
            data_out.append(x)
        proxy_list.append(data_out)
    except:
        print(file + ": No such file")

def url(proxy_list, link):
    try:
        working = yaml.safe_load(requests.get(url=link, timeout=240, headers=headers).text)
        data_out = []
        for x in working['proxies']:
            data_out.append(x)
        proxy_list.append(data_out)
    except:
        print("Error in Collecting " + link )
        #pass

def fetch(proxy_list, filename):
    current_date = time.strftime("%Y_%m_%d", time.localtime())
    baseurl = 'https://raw.githubusercontent.com/changfengoss/pub/main/data/'
    working = yaml.safe_load(requests.get(url=baseurl + current_date + '/' + filename, timeout=240).text)
    data_out = []
    for x in working['proxies']:
        data_out.append(x)
    proxy_list.append(data_out)

proxy_list=[]
if __name__ == '__main__':
    with Manager() as manager:
        proxy_list = manager.list()
        current_date = time.strftime("%Y_%m_%d", time.localtime())
        #print("Today is: " + current_date)
        start = time.time() #time start
        config = 'config.yaml'
        with open(config, 'r') as reader:
            config = yaml.load(reader, Loader=SafeLoader)
            subscribe_links = config['sub']
            subscribe_files = config['local']
        directories, total = get_file_list()
        data = parse(directories)
        try:
            sfiles = len(subscribe_links)
            tfiles = len(subscribe_links) + len(data[current_date])
            processes=[]
            filenames = list()
            filenames = data[current_date]
        except KeyError:
            print("Success: " + "find " + str(sfiles) + " Clash link")
        else:
            print("Success: " + "find " + str(tfiles) + " Clash link")

        processes=[]

        try: #Process开启多线程
            for i in subscribe_files:
                p = Process(target=local, args=(proxy_list, i))
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            for i in subscribe_links:
                p = Process(target=url, args=(proxy_list, i))
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            for i in filenames:
                p = Process(target=fetch, args=(proxy_list, i))
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            end = time.time() #time end
            print("Collecting in " + "{:.2f}".format(end-start) + " seconds")
        except:
            end = time.time() #time end
            print("Collecting in " + "{:.2f}".format(end-start) + " seconds")

        proxy_list=list(proxy_list)
        proxies = makeclash(proxy_list)
        push(proxies)
    """
    for i in tqdm(range(int(tfiles)), desc="Download"):
        proxy_list.append(get_proxies(current_date, data[current_date][i]))
    """
