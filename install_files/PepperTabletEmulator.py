#!/usr/bin/python

""" 
Pepper PapperTabletService emulator

2015/4/26 tkawata
"""

import sys
import time
import os

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

import webbrowser

NAO_IP = "localhost"


# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None


class ALTabletServiceModule(ALModule):
    """ ALTabletServiceModule

    """
    def __init__(self, name):
        ALModule.__init__(self, name)

    def cleanWebview(self):
        """ 
        """
        print "cleanWebview called"

    def hideWebview(self):
        """
        """
        print "hideWebview called"
        return True

    def loadApplication(self, *_args):
        """
        """
        appName = _args[0]
        i = appName.find("/")
        print i
        if i>1:
            appName = appName[0:i]
        url = "http://localhost/apps/%s" % appName
        print "loadApplication called %s" % url
        webbrowser.open(url)

        return True

    def loadUrl(self, *_args):
        """
        """
        print "loadUrl called open URL: %s" % _args[0]
        webbrowser.open(_args[0])
        return True

    def showWebview(self):
        """
        """
        print "showWebview called.."
        return True

    def getVideoLength(self):
        """
        """
        print "getVideoLength called.. Not implemented yet.."
        return -1


    def getVideoPosition(self):
        """
        """
        print "getVideoPosition called.. Not implemented yet.."
        return -1

    def pauseVideo(self):
        """
        """
        print "pauseVideo called.. Not implemented yet.."
        return False

    def playVideo(self, *_args):
        """
        """
        print "playVideo called.. Not implemented yet.."
        return False

    def resumeVideo(self):
        """
        """
        print "resumeVideo called.. Not implemented yet.."
        return False

    def stopVideo(self):
        """
        """
        print "stopVideo called.. Not implemented yet.."
        return False

    def hideImage(self):
        """
        """
        print "hideImage called.. Not implemented yet.."

    def pauseGif(self):
        """
        """
        print "pauseGif called.. Not implemented yet.."

    def preLoadImage(self, *_args):
        """
        """
        print "preLoadImage called.. Not implemented yet.."
        return True

    def resumeGif(self):
        """
        """
        print "resumeGif called.. Not implemented yet.."
        return True

    def setBackgroundColor(self, *_args):
        """
        """
        print "setBackgroundColor called.. Not implemented yet.."

    def showImage(self, *_args):
        """
        """
        print "showImage called open URL: %s" % _args[0]
        webbrowser.open(_args[0])
        return True


    def showAlertView(self, *_args):
        """
        """
        print "showAlertView called.. Not implemented yet.."

    def showInputDialog(self):
        """
        """
        print "showInputDialog called.. Not implemented yet.."

    def showInputTextDialog(self):
        """
        """
        print "showInputTextDialog called.. Not implemented yet.."

    def configureWifi(self, *_args):
        """
        """
        print "configureWifi called.. Not implemented yet.."
        return True

    def disableWifi(self):
        """
        """
        print "disableWifi called.. Not implemented yet.."

    def enableWifi(self):
        """
        """
        print "enableWifi called.. Not implemented yet.."

    def forgetWifi(self, *_args):
        """
        """
        print "forgetWifi called.. Not implemented yet.."
        return True

    def getWifiStatus(self):
        """
        """
        print "getWifiStatus called.. Not implemented yet.."
        return "CONNECTED"

    def getBrightness(self):
        """
        """
        print "getBrightness called.. Not implemented yet.."
        return 1

    def getCurrentLifeActivity(self):
        """
        """
        print "getCurrentLifeActivity called.. Not implemented yet.."
        return ""

    def hide(self):
        """
        """
        print "hide called.. Not implemented yet.."

    def resetToDefaultValue(self):
        """
        """
        print "resetToDefaultValue called.. Not implemented yet.."

    def robotIp(self):
        """
        """
        print "robotIp called"
        return "127.0.0.1"

    def setBrightness(self, *_args):
        """
        """
        print "setBrightness called.. Not implemented yet.."
        return True

    def setTabletLanguage(self, *_args):
        """
        """
        print "setTabletLanguage called.. Not implemented yet.."
        return True

    def setVolume(self, *_args):
        """
        """
        print "setVolume called.. Not implemented yet.."
        return True

    def version(self):
        """
        """
        print "version called.. Not implemented yet.."
        return ""

    def getLastVideoErrorLog(self):
        """
        """
        print "getLastVideoErrorLog called.. Not implemented yet.."
        return ""

    def postEventToApplication(self, *_args):
        """
        """
        print "postEventToApplication called.. Not implemented yet.."



def main():
    """ Main entry point

    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port


    global ALTabletService
    ALTabletService = ALTabletServiceModule("ALTabletService")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)



if __name__ == "__main__":
    main()