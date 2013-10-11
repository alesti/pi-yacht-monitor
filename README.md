pi-yacht-monitor
================

The idea of this project is to develop a framework to use the raspberry-pi as a yacht-monitoring and alerting system. Let's see what happens...

Dependencies / installation
---------------------------

Install dependencies
```
# install redis as main database
sudo apt-get install redis-server

# install python-setuptools
sudo apt-get install python-setuptools

# install python-bindings for redis
sudo easy_install redis

# install web-framework for python
sudo easy_install web.py

# fswebcam is used for capturing webcam images
sudo apt-get install fswebcam

#install git for easily download pi-yacht-monitor
sudo apt-get install git-core
```

Run
```
#install via git:
#for contributers:
git clone git@github.com:lnitram/pi-yacht-monitor.git

#for all users (no write access to repository)
git clone https://github.com/lnitram/pi-yacht-monitor.git

cd pi-yacht-monitor


#fill database with some dummy-values
cd collector
python dummycollector.py
cd ..

#run server
cd server
python server.py
```
Now the server will listen on port 8080. 
Now just open a browser: http://xxx.xxx.xxx.xxx:8080
You should see something like this:

|Sensor|Wert|Zeit der Erfassung|
|---|---|---|
|voltage|12.5|2013-10-11 21:59:29|
|temperature|14.5|2013-10-11 21:59:29|
|bilge|dry|2013-10-11 21:59:29|

Folder-structure
-----------------
- actor: Scripts for performing actions (sending mail, upload to webserver,...)
- captain: Daemon-scripts putting all together
- collector: Scripts for collecting data from different sources
- server: Webserver running local for showing data

