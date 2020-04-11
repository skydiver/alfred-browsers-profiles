#!/usr/bin/env python

import os
import json

def get_profiles(browser, path):
  profiles = []
  if os.path.isdir(path) == False:
    return profiles
  folders = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
  for folder in folders:
    file = "{}/{}/Preferences".format(path, folder)
    if folder != 'System Profile' and os.path.isfile(file):
      with open(file) as f:
        data = json.load(f)
        name = data['profile']['name']
        profiles.append({
          "icon": {
            "path": "icons/{}".format(browser['icon'])
          },
          "arg": "{} {}".format(browser['name'], folder),
          "subtitle": "Open Chrome using {} profile.".format(name),
          "title": name,
        })
  return profiles


home = os.path.expanduser("~")

browsers = [
  { 'name': 'CHROME', 'path': '/Library/Application Support/Google/Chrome', 'icon': 'chrome.icns' },
  { 'name': 'CHROME_CANARY', 'path': '/Library/Application Support/Google/Chrome Canary', 'icon': 'canary.icns' },
  # { 'name': 'CHROMIUM', 'path': '/Library/Application Support/Chromium', 'icon': 'chromium.icns' },
]

profiles = []

for browser in browsers:
  path = "{}/{}".format(home, browser['path'])
  prof = get_profiles(browser, path)
  profiles += prof

print json.dumps({"items": profiles}, indent=2)