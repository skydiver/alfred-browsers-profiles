#!/usr/bin/env python3

import os
import json
from lib.chromium import get_chromium_profiles


home = os.path.expanduser("~")

browsers = [
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

profiles = []

for browser in browsers:
  path = "{}/{}".format(home, browser['path'])
  prof = get_chromium_profiles(browser, path)
  profiles += prof

result = json.dumps({"items": profiles}, indent=2)
print(result)