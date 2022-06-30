## clash-proxy

> simple javascript api for [clash](https://github.com/Dreamacro/clash)

[![clash-proxy](https://img.shields.io/npm/v/clash-proxy.svg)](https://npmjs.org/clash-proxy)
[![Build Status](https://travis-ci.org/song940/clash-proxy.svg?branch=master)](https://travis-ci.org/song940/clash-proxy)

### Installation

```bash
$ npm install clash-proxy
```

### Example

```js
const Clash = require('clash-proxy');

const clash = Clash({
  secret: '-- YOUR CLASH TOKEN HERE --',
  api: 'http://127.0.0.1:9090'
});

clash.traffic(({ up, down }) => {
  console.log('traffic: up:%i; down:%i', up, down);
});

clash.logs('debug', log => {
  console.log('log', log);
});

(async () => {

  const proxies = await clash.proxies();
  console.log(proxies);

  const name = 'ss-ru1';

  const proxy = await clash.proxy(name);
  console.log(proxy);

  const delay = await clash.delay(name);
  console.log('delay', delay);

  const rules = await clash.rules();
  console.log(rules);

  const config = await clash.config();
  console.log(config);

  const result = await clash.switch('auto');
  console.log(result);

})();

```

### Contributing
- Fork this Repo first
- Clone your Repo
- Install dependencies by `$ npm install`
- Checkout a feature branch
- Feel free to add your features
- Make sure your features are fully tested
- Publish your local branch, Open a pull request
- Enjoy hacking <3

### MIT

This work is licensed under the [MIT license](./LICENSE).

---