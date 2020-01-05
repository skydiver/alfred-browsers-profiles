const alfy = require('alfy');

const { getProfiles } = require('./lib/chrome-profiles');

(async () => {
  const itemsChrome = getProfiles('CHROME');
  const itemsCanary = getProfiles('CHROME_CANARY');
  alfy.output([...itemsChrome, ...itemsCanary]);
})();
