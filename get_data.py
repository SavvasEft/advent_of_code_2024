# get data

import requests
import sys
import os

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from page_session import session



def get_data_from_url(url):
    # i.e. url = 'https://adventofcode.com/2024/day/1/input'
    cookies = {'session': session}
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        input_data = response.text
        #print(input_data)
        return input_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    