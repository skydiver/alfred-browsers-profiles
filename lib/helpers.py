import json


def get_browsers():
    f = open('browsers.json')
    supported_browsers = json.load(f)
    return supported_browsers


def get_browsers_titles(browser):
    supported_browsers = get_browsers()
    titles = {}
    for browser in supported_browsers[browser]:
        titles[browser['name']] = browser['title']
    return titles
