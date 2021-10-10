import configparser
from lib.helpers import get_browsers_titles


def get_firefox_profiles(browser, path):
    browser_titles = get_browsers_titles('firefox')

    name = browser['name']
    icon = browser['icon']
    title = browser_titles[name]

    profiles = []

    config_file = "{}/profiles.ini".format(path)
    config = configparser.ConfigParser()
    config.read(config_file)

    for profile in config.sections():

        try:
            browser_profile = config.get(profile, "Name")

            profiles.append({
                "icon": {
                    "path": "icons/{}".format(icon)
                },
                "arg": "{} {}".format(name, browser_profile),
                "subtitle": "Open {} using {} profile.".format(title, browser_profile),
                "title": browser_profile,
            })

        except configparser.NoOptionError:
            pass

    return profiles
