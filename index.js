const alfy = require('alfy');
const chromeProfileList = require('chrome-profile-list');

(async () => {
  const profilesChrome = chromeProfileList(chromeProfileList.variations.CHROME);
  const profilesCanary = chromeProfileList(
    chromeProfileList.variations.CHROME_CANARY
  );

  const itemsChrome = alfy
    .inputMatches(profilesChrome, 'displayName')
    .map(element => ({
      title: element.displayName,
      subtitle: `Open Chrome using ${element.displayName} profile.`,
      arg: element.displayName,
      icon: {
        path: 'icons/chrome.icns',
      },
    }));

  const itemsCanary = alfy
    .inputMatches(profilesCanary, 'displayName')
    .map(element => ({
      title: element.displayName,
      subtitle: `Open Chrome using ${element.displayName} profile.`,
      arg: element.displayName,
      icon: {
        path: 'icons/canary.icns',
      },
    }));

  alfy.output([...itemsChrome, ...itemsCanary]);
})();
