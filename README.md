pi-yacht-monitor
================

The idea of this project is to develop a framework to use the raspberry-pi as a yacht-monitoring and alerting system. Let's see what happens...

Dependencies / installation
---------------------------

Install dependencies
```
# install redis as main database
sudo apt-get install redis-server

# install python-bindings for redis
sudo easy_install redis

# install web-framework for python
sudo easy_install web.py
```

Run
```
#fill database with some dummy-values
python collector/dummycollector.py

#run server
python server/server.py
```
Now the server will listen on port 8080. 
Now just open a browser: http://<ip-of-raspberry>:8080
You should see something like this:

|||
|---|---|
|Voltage|12.5|
|Temperature|14.5|
|Bilge|dry|

Folder-structure
-----------------
- actor: Scripts for performing actions (sending mail, upload to webserver,...)
- captain: Daemon-scripts putting all together
- collector: Scripts for collecting data from different sources
- server: Webserver running local for showing data

