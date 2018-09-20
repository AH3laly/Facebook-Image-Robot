#!/usr/bin/python2
# Author: Abdelrahman Mohamed
# Contact: < Abdo.Tasks@Gmail.Com , https://Github.com/abd0m0hamed >
# Project: Facebook Image Robot. 
# Description: Automatically Post images from Google to Facebook Page.
# License: Science not for Monopoly.

import mechanize
import time
import urllib2
import re
from mimetypes import MimeTypes
import framework as f
import framework.logger as logger
import hashlib


class imageRobot:
    br = ""
    baseUrl = "https://images.google.com"
    foundImages = []
    foundLinks = []
    currentCategoryId = 0
    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br.set_header('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')

    def boot(self):

        try:
            f.db.connect()
            lastCategory = f.db.execute("SELECT optionValue FROM setting WHERE optionName = 'lastParsedCategory' ").fetchone()[0]
            nextCategoryInfo = f.db.execute("SELECT id,searchString FROM category WHERE id > %s ",(lastCategory,)).fetchone()
            f.db.disconnect()

            f.db.connect()
            if(nextCategoryInfo):
                self.currentCategoryId = nextCategoryInfo[0]
                f.db.execute("UPDATE setting SET optionValue = %s WHERE optionName='lastParsedCategory' ",(nextCategoryInfo[0],))
                self.start(nextCategoryInfo[1])
            else:
                f.db.execute("UPDATE setting SET optionValue = 0 WHERE optionName='lastParsedCategory' ")
            f.db.commit()
            f.db.disconnect()

        except Exception as e:
            logger.log(e.message,'Error',False)


    def start(self,qString):
        try:
            print "Initiating First Search"
            self.firstSearch(qString)
            response = self.br.response().read()
            print "Saving First Search Images"
            self.saveImages(response)
            print "Parsing Links found in First Search Page"
            self.parseLinks()
        except Exception as e:
            logger.log(e.message)

        #self.loadImages(response)

        #print response
        #imagesArray = re.finditer('base64(.*)\"\]',response)
        #imagesArray = re.finditer('base64,[a-zA-Z0-9/+\\\\]+',response)
        #imagesArray = re.finditer('data:image/jpeg;base64,[a-zA-Z0-9\/+]+',response)
        #for image in imagesArray:
        #    print '<img src="'+image.group(0)+'"><br>';



    def firstSearch(self,qString):
        try:
            self.br.open(self.baseUrl)
            self.br.select_form(nr=0)
            self.br.form['q'] = qString
            self.br.submit()

            #response = br.response()
            #print response.info()
            #print response.read()
            #print response.read()
        except Exception as e:
            logger.log(e.message)


    def parseLinks(self):
        try:
            pageLinks = self.br.links()
            for link in pageLinks:
                lnk = str(link.url)
                if(lnk.find('/search?') == 0):
                    print "Parsing Link https://www.google.com" + lnk+ " To Get Images"
                    self.getLinkImages(link.url)
            time.sleep(10)
        except Exception as e:
            logger.log(e.message)


    def getLinkImages(self,url):
        fullUrl = "https://www.google.com" + url
        try :
            req = urllib2.Request(fullUrl)
            req.add_header('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
            response = urllib2.urlopen(req)
            self.saveImages(response.read())

        except Exception as err:
            print err.message


    def saveImages(self,content):
        try:
            f.db.connect()
            #imagesArray = re.finditer('data:image/jpeg;base64,[a-zA-Z0-9\/+]+',content)
            imagesArray = re.finditer('"ou":"http(.+?)"',content)
            for image in imagesArray:
                #print '<img src="'+image.group(0)+'"><br>';
                imageUrl = image.group();
                imageUrl = imageUrl.replace('"ou":"','').replace('"','')
                imageType = self.getImageType(imageUrl)
                if imageType != 0:
                    f.db.execute(""" INSERT INTO image (url,catchDate,categoryId,urlId,type) VALUES (%s,now(),%s,%s,%s)""",(imageUrl,self.currentCategoryId,hashlib.md5(imageUrl).hexdigest(),imageType))
                    f.db.commit()
                #self.downloadImage(imageUrl)
                time.sleep(2)
        except Exception as e:
            logger.log(e.message)

    def getImageType(self,imageUrl):
        try:
            #Get image Type
            mime = MimeTypes()
            mime_type = mime.guess_type(imageUrl)[0]
            allowedTypes = ['image/jpeg','image/png','image/gif']
            if mime_type in allowedTypes:
                return mime_type
            else:
                return 0
        except Exception as e:
            print e.message

        #urllib2.urlretrieve(imageUrl, newImageName+".jpg")

"""
    def loadImages(self,content):
        #imagesArray = re.finditer('data:image/jpeg;base64,[a-zA-Z0-9\/+]+',content)
        imagesArray = re.finditer('"ou":"http(.+?)"',content)
        for image in imagesArray:
            #print '<img src="'+image.group(0)+'"><br>';
            imageUrl = image.group();
            imageUrl = imageUrl.replace('"ou":"','').replace('"','')
            print '<img src="'+imageUrl+'"><br>';
            self.downloadImage(imageUrl)
            time.sleep(3)


    def downloadImage(self,imageUrl):
        try:
            #Get image Type
            mime = MimeTypes()
            mime_type = mime.guess_type(imageUrl)[0]

            if mime_type.lower() == 'image/jpeg':
                fileExtension = 'jpg'
            elif mime_type.lower() == 'image/png':
                fileExtension = 'png'
            elif mime_type.lower() == 'image/gif':
                fileExtension = 'gif'
            else:
                return 0

            #Generate random file name
            newImageName = str(time.time())
            imgReq = urllib2.Request(imageUrl)
            imgData = urllib2.urlopen(imgReq).read()
            #Save downloaded image to local path
            localFile = open('/home/store/Work/pythonProjects/downloadedImages/'+newImageName+'.'+fileExtension,'w')
            localFile.write(imgData)
            localFile.close()

        except Exception as e:
            print e.message

        #urllib2.urlretrieve(imageUrl, newImageName+".jpg")

"""


ir = imageRobot()
while True:
    ir.boot()
    time.sleep(30)

