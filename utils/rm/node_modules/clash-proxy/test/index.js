const test = require('./test');
const assert = require('assert');
const clash = require('..')({
  secret: 'song940@163.com',
  api: 'http://lsong.me:9090'
});


test('clash#proxies', async () => {
  const proxies = await clash.proxies();
  assert.ok(proxies);
  assert.ok(proxies.GLOBAL);
  assert.ok(proxies.DIRECT);
  assert.ok(proxies.REJECT);
});

test('clash#proxy', async () => {
  const proxy = await clash.proxy('vmess-01');
  assert.ok(proxy);
  assert.equal(proxy.type, 'Vmess');
});

test('clash#delay', async () => {
  const delay = await clash.delay('v2net-auto');
  assert.ok(delay);
  assert.ok(delay.delay, delay.message);
});

test('clash#rules', async () => {
  const rules = await clash.rules();
  assert.ok(Array.isArray(rules));
  
  const [ rule ] = rules;
  assert.ok(rule);
  assert.ok(rule.type);
  assert.ok(rule.payload);
  assert.ok(rule.proxy);
});

test('clash#config', async () => {
  const config = await clash.config();
  assert.ok(config);
  assert.ok(config.port);
  assert.ok(config.mode);
});

test('clash#switch', async () => {
  const result = await clash.switch('Proxy', 'v2net-auto');
  assert.ok(result);
});