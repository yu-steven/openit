const Clash = require('..');

const clash = Clash({
  secret: 'song940@163.com',
  api: 'http://lsong.me:9090'
});

clash.traffic(({ up, down }) => {
  console.log('traffic: up: %i; down: %i', up, down);
});

clash.logs('debug', ({ type, payload }) => {
  console.log('log', type, payload);
});