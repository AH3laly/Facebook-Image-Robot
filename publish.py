#!/usr/bin/python2
# Author: Abdelrahman Mohamed
# Contact: < Abdo.Tasks@Gmail.Com , https://Github.com/abd0m0hamed >
# Project: Facebook Image Robot. 
# Description: Automatically Post images from Google to Facebook Page.
# License: Science not for Monopoly.

import framework as f
import time
import requests
import urllib2
import os
import json

def boot():

    try:
        f.db.connect()
        imageInfo = f.db.execute("SELECT id,url,type,categoryId FROM image WHERE isPublished = 0 ORDER BY RAND() LIMIT 1").fetchone()
        if(imageInfo):
            #FYI, (y) is not a tuple - it is an int in parenthesis, adding comma (y,) makes it a tuple with one element inside
            categoryInfo = getImageCategory(imageInfo[3])
            publishReq = publishImage(imageInfo,categoryInfo[1])
            print "Publishing Image: " + str(imageInfo[0]) + " : " + imageInfo[1]
            print "Result: " + str(publishReq)
            print "Published ON: "+ f.getFullDate()

            if(publishReq):
                f.db.execute(" UPDATE image SET isPublished = 1, publishError = 0, facebookId = %s, publishDate = %s WHERE id = %s ",(publishReq,f.getFullDate(),imageInfo[0]))
            else:
                f.db.execute(" UPDATE image SET isPublished = 1, publishError = 1 WHERE id = %s ",(imageInfo[0],))

            f.db.commit()

        f.db.disconnect()
	return publishReq

    except Exception as e:
        print e.message
	return False


def getImageCategory(imageId):
    return f.db.execute("SELECT id,description FROM category WHERE id = %s ",(imageId,)).fetchone()

def publishImage(imageInfo,message):
    try:
        facebookConfig = f.config.get('facebook')

        url = 'https://graph.facebook.com/' + facebookConfig['pageId'] + '/photos'
        imgReq = urllib2.Request(imageInfo[1])
        imgData = urllib2.urlopen(imgReq).read()
        tmpFile = '/tmp/'+str(time.time())
        tf = open(tmpFile,'w')
        tf.write(imgData)
        tf.close()

        files = {'file': open(tmpFile)}
        data = {
            'access_token':facebookConfig['accessToken'],
            'message':message,
            #'link':'https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg',
            #'picture': '/store/testupload.jpeg'
            #'picture': 'http://i65.tinypic.com/2hmegkk.jpg'
            #'attachment': '/store/testupload.jpeg'
        }
        response = requests.post(url, params=data, files=files)
        os.remove(tmpFile)
        callResponse = json.loads(response.content)
        return callResponse['id']

    except Exception as e:
        print e.message
        return 0


while not boot():
      time.sleep(60)
      boot()

