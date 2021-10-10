#!/usr/bin/env python3

import os
import json
from lib.chromium import get_chromium_profiles
from lib.firefox import get_firefox_profiles
from lib.helpers import get_browsers

home = os.path.expanduser("~")

supported_browsers = get_browsers()

profiles = []

for browser in supported_browsers['chromium']:
    if os.path.exists(browser['app']):
        path = "{}/{}".format(home, browser['path'])
        prof = get_chromium_profiles(browser, path)
        profiles += prof

for browser in supported_browsers['firefox']:
    if os.path.exists(browser['app']):
        path = "{}/{}".format(home, browser['path'])
        prof = get_firefox_profiles(browser, path)
        profiles += prof

result = json.dumps({"items": profiles}, indent=2)
print(result)
