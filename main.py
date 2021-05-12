#!/usr/bin/env python3

import os
import json
from lib.chromium import get_chromium_profiles
from lib.firefox import get_firefox_profiles


home = os.path.expanduser("~")

chromium = [
  {
    'name': 'CHROME',
    'path': '/Library/Application Support/Google/Chrome',
    'icon': 'chrome.icns'
  },
  {
    'name': 'CHROME_CANARY',
    'path': '/Library/Application Support/Google/Chrome Canary',
    'icon': 'canary.icns'
  },
  # {
  #   'name': 'chromium',
  #   'path': '/library/application support/chromium',
  #   'icon': 'chromium.icns'
  # },
  {
    'name': 'BRAVE',
    'path': '/Library/Application Support/BraveSoftware/Brave-Browser',
    'icon': 'brave.icns'
  },
]

firefox = [
  {
    'name': 'FIREFOX',
    'path': '/Library/Application Support/Firefox',
    'icon': 'firefox.icns'
  },
  {
    'name': 'FIREFOX_DEV',
    'path': '/Library/Application Support/Firefox',
    'icon': 'firefox-dev.icns'
  },
]

profiles = []

for browser in chromium:
  path = "{}/{}".format(home, browser['path'])
  prof = get_chromium_profiles(browser, path)
  profiles += prof

for browser in firefox:
  path = "{}/{}".format(home, browser['path'])
  prof = get_firefox_profiles(browser, path)
  profiles += prof

result = json.dumps({"items": profiles}, indent=2)
print(result)