def parse(data_in):
    dtp = []
    for x in data_in:
        dtp.append(x.replace('data/', ''))
    dtpr1 = [ x for x in dtp if "/" in x]
    dtpr2 = [ x for x in dtpr1 if ".yaml" in x]
    textdict = {}
    for x in dtpr2:
        date, filename = x.split('/')
        if date in textdict:
            textdict[date].append(filename)
        else:
            textdict[date] = []
            textdict[date].append(filename)

    return textdict

def makeclash(dictin):
    badprotocols = ['vless']
    proxies = []
    for x in dictin:
        for y in x:
            try:
                if y in proxies:
                    pass
                else:
                    if y['type'] in badprotocols:
                        pass
                    else:
                        proxies.append(y)
            except:
                continue
    return proxies
