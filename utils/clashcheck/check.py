import requests
import json



def check(alive, proxy, apiurl,sema,timeout, testurl):
    try:
        r = requests.get(url=apiurl + '/proxies/' + str(proxy['name']) + '/delay?url='+testurl+'&timeout=' + str(timeout), timeout=10)
        response = json.loads(r.text)
        try:
            if response['delay'] > 0:
                r = requests.get(url=apiurl + '/proxies/' + str(proxy['name']) + '/delay?url=https://www.youtube.com/s/player/23010b46/player_ias.vflset/en_US/remote.js&timeout=' + str(timeout), timeout=10)
                response = json.loads(r.text)
                try:
                    if response['delay'] > 0:
                        r = requests.get(url=apiurl + '/proxies/' + str(proxy['name']) + '/delay?url=https://cachefly.cachefly.net/1mb.test&timeout=' + str(timeout), timeout=15)
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
