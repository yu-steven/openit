require('isomorphic-fetch');

/**
 * Clash API
 * @docs https://clash.gitbook.io/doc/
 * @param {*} param0 
 */
const Clash = ({ api, secret }) => {
  const request = (method, path, body) => {
    const headers = {
      'Content-Type': 'application/json'
    };
    if (secret) {
      headers['Authorization'] = `Bearer ${secret}`;
    }
    return Promise
      .resolve()
      .then(() => fetch(api + path, {
        method,
        headers,
        body: body && JSON.stringify(body),
      }));
  };
  return {
    /**
     * @docs https://clash.gitbook.io/doc/restful-api/common#获得当前的流量
     * @param {*} cb 
     */
    traffic() {
      return request('get', '/traffic');
    },
    /**
     * @docs https://clash.gitbook.io/doc/restful-api/common#获得实时日志
     * @param {*} level 
     * @param {*} cb 
     */
    logs(level) {
      return request('get', `/logs?level=${level}`);
    },
    /**
     * @docs https://clash.gitbook.io/doc/restful-api/proxies#获取所有代理
     */
    proxies() {
      return Promise
        .resolve()
        .then(() => request('get', `/proxies`))
        .then(res => res.json())
        .then(data => data.proxies)
    },
    /**
     * @docs https://clash.gitbook.io/doc/restful-api/proxies#获取单个代理信息
     * @param {*} name 
     */
    proxy(name) {
      return Promise
        .resolve()
        .then(() => request('get', `/proxies/${name}`))
        .then(res => res.json())

    },
    /**
     * @docs https://clash.gitbook.io/doc/restful-api/proxies#获取单个代理的延迟
     * @param {*} name 
     * @param {*} url 
     * @param {*} timeout 
     */
    delay(name, url = 'http://www.gstatic.com/generate_204', timeout = 2000) {
      return Promise
        .resolve()
        .then(() => request('get', `/proxies/${name}/delay?url=${url}&timeout=${timeout}`))
        .then(res => res.json())
    },
    /**
     * @docs https://clash.gitbook.io/doc/restful-api/proxies#切换Selector中选中的代理
     * @param {*} selector 
     * @param {*} name 
     */
    switch(selector, name) {
      return Promise
        .resolve()
        .then(() => request('put', `/proxies/${selector}`, { name }))
        .then(res => res.status === 204)
    },
    /**
     * rules
     * @docs https://clash.gitbook.io/doc/restful-api/config#获取所有已经解析的规则
     */
    rules() {
      return Promise
        .resolve()
        .then(() => request('get', '/rules'))
        .then(res => res.json())
        .then(data => data.rules)
    },
    /**
     * https://clash.gitbook.io/doc/restful-api/config#获得当前的基础设置
     */
    config(conf) {
      if(conf) {
        return Promise
        .resolve()
        .then(() => request('PATCH', '/configs', conf))
        .then(res => res.status == 204)
      }
      return Promise
        .resolve()
        .then(() => request('get', '/configs'))
        .then(res => res.json())
    }
  };
};

module.exports = Clash;