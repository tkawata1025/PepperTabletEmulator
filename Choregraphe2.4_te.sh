#!/bin/bash

cd "/Applications/Aldebaran/Choregraphe Suite 2.4/Choregraphe.app/Contents/Resources"

DYLD_FRAMEWORK_PATH=. DYLD_LIBRARY_PATH=lib bin/naoqi-bin &

sleep 5

export DYLD_LIBRARY_PATH=<NAOqi python SDK をコピーした場所>:$DYLD_LIBRARY_PATH
export PYTHONPATH=<NAOqi python SDK をコピーした場所>:$PYTHONPATH 

/usr/bin/python /usr/local/bin/qimessaging-json &
/usr/bin/python /usr/local/bin/PepperTabletEmulator.py & 

/Applications/Aldebaran/Choregraphe\ Suite\ 2.4/Choregraphe.app/Contents/Resources/choregraphe -p 9559 

kill %1
kill %2
kill %3







