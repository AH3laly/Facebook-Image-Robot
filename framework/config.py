#!/usr/bin/python2
# Author: Abdelrahman Mohamed
# Contact: < Abdo.Tasks@Gmail.Com , https://Github.com/abd0m0hamed >
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
