import os, configparser

def get_firefox_profiles(browser, path):
  profiles = []

  config_file = "{}/profiles.ini".format(path)
  config = configparser.ConfigParser()
  config.read(config_file)

  for name in config.sections():

    try:
      profile = config.get(name, "Name")
      profiles.append({
        "icon": {
          "path": "icons/{}".format(browser['icon'])
        },
        "arg": "{} {}".format(browser['name'], profile),
        "subtitle": "Open Firefox using {} profile.".format(profile),
        "title": profile,
      })

    except configparser.NoOptionError:
        pass

  return profiles