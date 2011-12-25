#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# using UTF-8 charset

import jaiku
import json
import argparse

file = open('API.keys', 'r+')
data = json.load(file)

API_KEY = data["API_KEY"]


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    parser.add_argument('username', help='Username')
    args = parser.parse_args()
    
    try:

        japi = jaiku.Api(username=args.username, api_key=API_KEY)
        presence = japi.GetUserFeed(args.username)
        print(presence)

    except Exception:
        print("FUUUUU")
 
