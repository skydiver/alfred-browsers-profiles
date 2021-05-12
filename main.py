#!/usr/bin/env python3

import os
import json
from lib.chromium import get_chromium_profiles
from lib.firefox import get_firefox_profiles


home = os.path.expanduser("~")

chromium = [
  {
    "app" : "/Applications/Google Chrome.app",
    "name": "CHROME",
    "path": "/Library/Application Support/Google/Chrome",
    "icon": "chrome.icns"
  },
  {
    "app" : "/Applications/Google Chrome Canary.app",
    "name": "CHROME_CANARY",
    "path": "/Library/Application Support/Google/Chrome Canary",
    "icon": "canary.icns"
  },
  {
    "app" : "/Applications/Chromium.app",
    "name": "chromium",
    "path": "/Library/Application Support/Chromium",
    "icon": "chromium.icns"
  },
  {
    "app" : "/Applications/Brave Browser.app",
    "name": "BRAVE",
    "path": "/Library/Application Support/BraveSoftware/Brave-Browser",
    "icon": "brave.icns"
  },
]

firefox = [
  {
    "app" : "/Applications/Firefox.app",
    "name": "FIREFOX",
    "path": "/Library/Application Support/Firefox",
    "icon": "firefox.icns"
  },
  {
    "app" : "/Applications/FirefoxDeveloperEdition.app",
    "name": "FIREFOX_DEV",
    "path": "/Library/Application Support/Firefox",
    "icon": "firefox-dev.icns"
  },
]

profiles = []

for browser in chromium:
  if os.path.exists(browser['app']):
    path = "{}/{}".format(home, browser['path'])
    prof = get_chromium_profiles(browser, path)
    profiles += prof

for browser in firefox:
  if os.path.exists(browser['app']):
    path = "{}/{}".format(home, browser['path'])
    prof = get_firefox_profiles(browser, path)
    profiles += prof

result = json.dumps({"items": profiles}, indent=2)
print(result)