#!/usr/bin/env python3


'''
All countries flags with country name and country code from 
https://www.restcountries.com/ in medium size (512x512) and save them 
in a folder named "flags" in the same directory as this script and set 
the file name as country code.
'''

import os
import sys
import requests
import shutil


def progress_bar(count, total, status=''):
    # Create a progress bar function
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def countries_data():
    # Create a folder named "flags" in the same directory as this script
    if not os.path.exists("flags"):
        os.makedirs("flags")

    # Get all country codes and names
    countries = requests.get("https://restcountries.com/v3.1/all").json()
    count = 0
    total = len(countries)

    # Download all flags
    for country in countries:
        count += 1
        # get country name
        name = country["name"]["common"]
        code = country["cca2"].lower()
        # Download flag
        flag = country['flags']['png']
        # Download flag
        r = requests.get(flag, stream=True)
        # Save flag
        with open("flags/" + code + ".png", "wb") as f:
            shutil.copyfileobj(r.raw, f)
        # Print progress
        progress_bar(count, total, status="Downloading " + name + " flag")


if __name__ == "__main__":
    countries_data()
