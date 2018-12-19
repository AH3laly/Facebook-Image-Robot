#!/usr/bin/python2
# Author: Abdelrahman Helaly
# Contact: < AH3laly@gmail.com , https://Github.com/AH3laly >
# Project: Facebook Image Robot. 
# Description: Automatically Post images from Google to Facebook Page.
# License: Science not for Monopoly.


def get(key = 'all'):

    conf = {
        'db':{
            'user':'root',
            'password':'',
            'host':'localhost',
            'database':'imagerobot',
            'raise_on_warnings': True
        },
        'facebook':{
            'pageId':'',
            'accessToken':''
        }
    }

    if key == 'all':
        return conf
    else:
        return conf[key]
