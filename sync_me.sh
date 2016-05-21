#!/bin/sh
echo starting
while true; do
  echo rsyncing
  rsync -avzP web_i2c.py pi@192.168.1.16:~/FireBender/WebIOPi-0.7.1/frbndr/python/
  #inotifywait -r -e modify web_i2c.py
  
  rsync -avzP config pi@192.168.1.16:/etc/webiopi/
  #inotifywait -r -e modify config
  
  rsync -avzP index.html pi@192.168.1.16:~/FireBender/WebIOPi-0.7.1/frbndr/html/
  inotifywait -r -e modify index.html -e modify config -e modify web_i2c.py

done
