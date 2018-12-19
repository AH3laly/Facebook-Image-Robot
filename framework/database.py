#!/usr/bin/python2
# Author: Abdelrahman Helaly
# Contact: < AH3laly@gmail.com , https://Github.com/AH3laly >
# Project: Facebook Image Robot. 
# Description: Automatically Post images from Google to Facebook Page.
# License: Science not for Monopoly.


import mysql.connector
import logger
import config
class database:
    conn = False
    cur = False

    def __init__(self):
        self.conn = False
        self.cur = False

    def connect(self):
        try:

            self.conn = mysql.connector.connect(**config.get('db'))
            self.cur = self.conn.cursor()
        except Exception, err:
            logger.log('Database Connect Error: '+err.message,'Error',True)
            return False

    def execute(self,query,params = ()):
        try:
            self.cur.execute(query,params)
            return self.cur
        except mysql.connector.Error as err:
            logger.log('Executing Query Error: '+err.msg,'Error',True)
            return False

    def commit(self):
        try:
            self.conn.commit()
            return True
        except Exception, err:
            logger.log('Database Commit Error: '+err.msg,'Error',True)
            return False

    def disconnect(self):
        try:
            self.conn.close()
        except Exception, err:
            logger.log('Database Close Error: '+err.message,'Error',True)
            return False

