import os
import json
from lib.helpers import get_browsers_titles


################################################################################
# Browse trough Chromium based browser profiles
################################################################################
def get_chromium_profiles(browser, path):
    browser_titles = get_browsers_titles('chromium')

    name = browser['name']
    icon = browser['icon']
    title = browser_titles[name]

    profiles = []

    if os.path.isdir(path) == False:
        return profiles

    folders = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

    for folder in folders:
        file = "{}/{}/Preferences".format(path, folder)
        if folder != 'System Profile' and os.path.isfile(file):
            with open(file) as f:
                data = json.load(f)

                browser_profile = get_profile_name(path, folder) if browser['name'] == 'chromium' else data['profile']['name']

                profiles.append({
                    "icon": {
                        "path": "icons/{}".format(icon)
                    },
                    "arg": "{} {}".format(name, folder),
                    "subtitle": "Open {} using {} profile.".format(title, browser_profile),
                    "title": browser_profile,
                })

    return profiles


################################################################################
# Chromium stores the profile name in Local State file
################################################################################
def get_profile_name(path, folder):
    local_state_file = "{}/Local State".format(path)

    with open(local_state_file) as f:
        data = json.load(f)
        if folder in data['profile']['info_cache']:
            return data['profile']['info_cache'][folder]['name']

    return None
