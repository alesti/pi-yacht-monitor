#!/bin/bash

# this script opens a ssh-connection to a server running at home
# and creates 2 tunnels:
# ssh tunnel can be used to login from home
# http tunnel to access the webserver running on remote pi
# - ssh-server must be running running at home (for example by using dyndns and port-forwarding in the router)
# - create a ssh-key on the remote pi
# - put public-key of remote pi in authorized keys in local pi
# - run this script on remote-pi
#
# on the local pi it's possible to login to the remote pi:
# - ssh -p 2222 pi@127.0.0.1
#
# webserver can be found at
# - http://127.0.0.1:8888
# 
# to enable the access to remote webserver in the whole local lan:
# on the local ssh-server put the following line in
# /etc/ssh/sshd_config
# GatewayPorts yes
# now website is available at http://ip.of.local.pi:8888


LOG=/home/pi/callhome.log
HOME_IP=xxx.xxx.xxx.xxx
HOME_PORT=xxxx
LOCAL_SSH_PORT=2222
LOCAL_WEB_PORT=8888

while true
do
        echo "calling home at `date`" >> $LOG
        ssh -N -l pi -p $HOME_PORT -R $LOCAL_SSH_PORT:127.0.0.1:22 -R $LOCAL_WEB_PORT:127.0.0.1:80 $HOME_IP >> $LOG 2>&1
        echo "calling-home died, trying again in 30 seconds" >> $LOG
        sleep 30
done
