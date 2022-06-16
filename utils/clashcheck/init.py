import os
import yaml
import requests
import shutil
from clash import filter

from yaml import SafeLoader
def init():
    if not os.path.exists('./temp'):
        os.mkdir('temp')

    # read from config file
    with open('config.yaml', 'r') as reader:
        config = yaml.load(reader, Loader=SafeLoader)
        http_port = config['http-port']
        api_port = config['api-port']
        threads = config['threads']
        source = str(config['source'])
        timeout = config['timeout']
        testurl = config['test-url']
        outfile = config['outfile']
    # get clash config file
    if source.startswith('https://'):
        proxyconfig = yaml.load(requests.get(source).text, Loader=SafeLoader)
    else:
        with open(source, 'r') as reader:
            proxyconfig = yaml.load(reader, Loader=SafeLoader)

    # set clash api url
    baseurl = '127.0.0.1:' + str(api_port)
    apiurl = 'http://'+baseurl

    # filter config files
    proxyconfig = filter(proxyconfig)

    config = {'port': http_port, 'external-controller': baseurl, 'mode': 'global',
              'log-level': 'silent', 'proxies': proxyconfig['proxies']}

    with open('./temp/working.yaml', 'w') as file:
        file = yaml.dump(config, file)

    # return all variables
    return http_port, api_port, threads, source, timeout, outfile, proxyconfig, apiurl, testurl, config

def cleanup(clash):
    shutil.rmtree('./temp')
    clash.terminate()
    exit(0)
