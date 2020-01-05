const alfy = require('alfy');
const chromeProfileList = require('chrome-profile-list');

const getBrowserParameters = browser => {
  if (browser === 'CHROME_CANARY') {
    return {
      app: 'Chrome Canary',
      icon: 'canary',
    };
  }
  return {
    app: 'Chrome',
    icon: 'chrome',
  };
};

const getProfiles = browser => {
  const params = getBrowserParameters(browser);
  const profiles = chromeProfileList(chromeProfileList.variations[browser]);

  const items = alfy.inputMatches(profiles, 'displayName').map(element => ({
    title: element.displayName,
    subtitle: `Open ${params.app} using ${element.displayName} profile.`,
    arg: `${browser} ${element.profileDirName}`,
    icon: {
      path: `icons/${params.icon}.icns`,
    },
  }));

  return items;
};

module.exports = { getProfiles };
