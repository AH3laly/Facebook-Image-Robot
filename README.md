
## Description

<p>Python software to publish photos to Facebook page, You can modify it to publish anything.</p>

<p><b>spider.py</b> Parses Google images to get images and save it into <b>image</b> table.</p>

<p><b>publish.py</b> Gets single image from the <b>image</b> table and publish it to the Facebook page.</p>

## Requirements
- <b>Python2</b> at least.
- Python library<b>mechanize</b>

## Installation
- Import db/database.sql
- Configure framework/config.py
- run spider.py once.
- Configure the Cron to run <b>publish.py</b> every one hour.
- You can set images categories for <b>spider.py</b> from <b>category</b> table.

## Live Examble
See [fb.com/WonderfulPhotoStore Facebook Page](https://www.facebook.com/WonderfulPhotoStore)

