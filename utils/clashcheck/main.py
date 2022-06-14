import os.path
import sys
import time
from multiprocessing import Process, Manager, Semaphore
from yaml.loader import SafeLoader
from clash import push
from tqdm import tqdm
import platform
import json
import yaml
import requests
import shutil
import subprocess
import geoip2.database

def geoip_update(url):
        print('Downloading Country.mmdb...')
        try:
            request.urlretrieve(url, './utils/clashcheck/Country.mmdb')
            print('Success!\n')
        except Exception:
            print('Failed!\n')
            pass

def check(alive, proxy, apiurl,sema,timeout):
    try:
        r = requests.get(url=apiurl + '/proxies/'+str(proxy['name'])+'/delay?url=https://gstatic.com/generate_204&timeout='+str(timeout),timeout=10)
        response = json.loads(r.text)
        try:
            if response['delay'] > 0:
                r = requests.get(url=apiurl + '/proxies/' + str(proxy['name']) + '/delay?url=https://www.youtube.com/s/player/23010b46/player_ias.vflset/en_US/remote.js&timeout=' + str(timeout), timeout=10)
                response = json.loads(r.text)
                try:
                    if response['delay'] > 0:
                        r = requests.get(url=apiurl + '/proxies/' + str(proxy['name']) + '/delay?url=https://cachefly.cachefly.net/1mb.test&timeout=' + str(timeout), timeout=10)
                        response = json.loads(r.text)
                        try:
                            if response['delay'] > 0:
                                alive.append(proxy)
                        except:
                            pass
                except:
                    pass
        except:
            pass
    except:
        pass

    sema.release()



if __name__ == '__main__':
    geoip_update('https://ghproxy.com/https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country.mmdb')
    with Manager() as manager:
        if not os.path.exists('./temp'):
            os.mkdir('temp')
        with open ('config.yaml','r') as reader:
            config = yaml.load(reader,Loader=SafeLoader)
            http_port = config['http-port']
            api_port = config['api-port']
            threads = config['threads']
            source = str(config['source'])
            timeout = config['timeout']
            outfile = config['outfile']
        alive = manager.list()
        if source.startswith('https://'):
            proxyconfig = yaml.load(requests.get(source).text,Loader=SafeLoader)
        else:
            with open (source,'r') as reader:
                proxyconfig = yaml.load(reader,Loader=SafeLoader)
        baseurl = '127.0.0.1:' + str(api_port)
        config = {'port': http_port, 'external-controller': baseurl, 'mode': 'global',
                      'log-level': 'silent', 'proxies': proxyconfig['proxies']}
        with open('./temp/working.yaml', 'w') as file:
            file = yaml.dump(config, file)
        operating_system=str(platform.platform())
        if operating_system.startswith('macOS'):
            if 'arm64' in operating_system:
                clashname='./clash-darwinarm64'
            else:
                clashname='./clash-darwinamd64'
        elif operating_system.startswith('Linux'):
            clashname='./clash-linuxamd64'
        elif operating_system.startswith('Windows'):
            clashname='clash-windowsamd64.exe'
        else:
            print('Unsupported Platform')
            exit(1)
        print('Running on '+ operating_system)
        clash = subprocess.Popen([clashname, '-f', './temp/working.yaml'])
        processes =[]
        apiurl='http://'+baseurl
        sema = Semaphore(threads)
        time.sleep(5)
        for i in tqdm(range(int(len(config['proxies']))), desc="Testing"):
            sema.acquire()
            p = Process(target=check, args=(alive,config['proxies'][i],apiurl,sema,timeout))
            p.start()
            processes.append(p)
        for p in processes:
            p.join
        time.sleep(5)
        alive=list(alive)
        push(alive,outfile)
        shutil.rmtree('./temp')
        clash.terminate()
