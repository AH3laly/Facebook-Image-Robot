#!/usr/bin/python2
# Author: Abdelrahman Mohamed
# Contact: < Abdo.Tasks@Gmail.Com , https://Github.com/abd0m0hamed >
# Project: Facebook Image Robot. 
# Description: Automatically Post images from Google to Facebook Page.
# License: Science not for Monopoly.


import database
import datetime
from framework import config

db = database.database()

def getFullDate():
    dateNow = datetime.date.today().isoformat()
    timeNow = datetime.datetime.now().time().isoformat()
    return dateNow+' '+timeNow
