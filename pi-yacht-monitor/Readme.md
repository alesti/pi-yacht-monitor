The idea of this project is to develop a framework to use the raspberry-pi as a yacht-monitoring and alerting system. Let's see what happens...

Dependencies / installation
---------------------------

Install dependencies
```
#system update
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade

#install git
sudo apt-get install git-core

# install redis-database
sudo apt-get install redis-server

# install python-setuptools
sudo apt-get install python-setuptools

# install python-bindings for redis
sudo easy_install redis

#install i2c - support
sudo apt-get install i2c-tools

#remove i2c from blacklist:
sudo nano /etc/modprobe.d/raspi-blacklist.conf
#add "#" before blacklist spi-bcm2708
#add "#" before blacklist i2c-bcm2708
#save and exit

#add i2c-dev to modules
sudo nano /etc/modules
# add "i2c-dev"
# save and exit

#put pi-user in i2c-group
sudo adduser pi i2c

#install python i2c support
sudo apt-get install python-smbus

#reboot
sudo reboot

#install apache
sudo apt-get install apache2 apache2-doc apache2-utils

#install php5
sudo apt-get install libapache2-mod-php5 php5 php-pear php5-xcache

#install redis-support for php
sudo pear channel-discover pear.nrk.io
sudo pear install nrk/Predis 

# for contributors only
# set up git user and email
git config --global user.name "yourname"
git config --global user.email "youremail"

#install yacht-monitor

cd /home/pi

#for contributers:
git clone git@github.com:lnitram/pi-yacht-monitor.git

#install for all users (no write access to repository)
git clone https://github.com/lnitram/pi-yacht-monitor.git

#create symlink in /var/www
sudo ln -s /home/pi/pi-yacht-monitor/pi-yacht-monitor/server/httpdocs /var/www/yacht-monitor

#open your browser and visit:
#http://ip.of.your.raspberry/yacht-monitor
#username: yacht-monitor
#password: yacht-monitor
#please change this first using "Configuration"

#install i2c-daemon
sudo cp /home/pi/pi-yacht-monitor/pi-yacht-monitor/collector/i2ccollect /etc/init.d/
sudo chmod +x /etc/init.d/i2ccollect
chmod +x /home/pi/pi-yacht-monitor/pi-yacht-monitor/collector/i2ccollect
sudo /etc/init.d/i2ccollect start
```
