#!/usr/bin/env python3

import requests
import sys



def ping(addr):
    try:
        r = requests.get(addr, timeout=1)
        return r.ok

    except requests.exceptions.ConnectionError:
        return False


if __name__ == '__main__':
    rs = ping('https://www.baidu.com')
    if rs:
        print('OK')

    else:
        print('False')
