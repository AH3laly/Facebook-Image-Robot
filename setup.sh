#!/usr/bin/bash
# Author: Abdelrahman Helaly
# Contact: < AH3laly@gmail.com , https://Github.com/AH3laly >
# Project: Facebook Image Robot. 
# Description: Automatically Post images from Google to Facebook Page.
# License: Science not for Monopoly.

echo "Please type Mysql Password."
mysql -u root -p < ./ < $PWD/db/database.sql
sed -s 's|__path_to_install__|'"${PWD}"'|g' ./systemd/serviceTemplate > ./systemd/imageRobotSpider.service
mv -f $PWD/systemd/imageRobotSpider.service /usr/lib/systemd/system/
systemctl daemon-reload
systemctl enable imageRobotSpider
systemctl start imageRobotSpider
systemctl status imageRobotSpider
