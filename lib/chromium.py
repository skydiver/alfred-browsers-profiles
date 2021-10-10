import os
import json

def get_chromium_profiles(browser, path):
  browser_titles = {
    "CHROME": "Chrome",
    "CHROME_CANARY": "Chrome Canary",
    "BRAVE": "Brave",
  }

  name = browser['name']
  icon = browser['icon']
  title = browser_titles[name]

  profiles = []

  if os.path.isdir(path) == False:
    return profiles

  folders = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]

  for folder in folders:
    file = "{}/{}/Preferences".format(path, folder)
    if folder != 'System Profile' and os.path.isfile(file):
      with open(file) as f:

        data = json.load(f)
        browser_profile = data['profile']['name']

        profiles.append({
          "icon": {
            "path": "icons/{}".format(icon)
          },
          "arg": "{} {}".format(name, folder),
          "subtitle": "Open {} using {} profile.".format(title, browser_profile),
          "title": browser_profile,
        })

  return profiles