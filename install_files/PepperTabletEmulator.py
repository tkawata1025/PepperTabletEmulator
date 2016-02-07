#!/usr/bin/python

""" 
Pepper PapperTabletService emulator

2015/4/26 tkawata
"""

import sys
import time
import os

import qi

import webbrowser

robotIp = "localhost"


memory = None


class ALTabletServiceModule:
    """ ALTabletServiceModule

    """
    def __init__(self):
        pass

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
        url = "http://%s/apps/%s" % (robotIp, appName)
        print "loadApplication called %s" % url
        webbrowser.open(url, new=0)

        return True

    def loadUrl(self, *_args):
        """
        """
        print "loadUrl called open URL: %s" % _args[0]
        webbrowser.open(_args[0],new=0)
        return True

    def showWebview(self, *_args):
        """
        """
        print "showWebview called.."

        if len(_args) > 0:
            self.loadUrl(_args[0])
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
        webbrowser.open(_args[0], new=0)
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
        return robotIp

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

    def reloadPage(self, *_args):
        """
        """
        print "reloadPage called.. Not implemented yet.."
        


def main():
    app = qi.Application()
    app.start()
    session = app.session
    myService = ALTabletServiceModule()
    session.registerService("ALTabletService", myService)
    app.run()


if __name__ == "__main__":
    main()
