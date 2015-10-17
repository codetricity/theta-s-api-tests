#! /usr/bin/env python

import requests, json, pprint
import sys, io
from thetapylib import *
from PIL import Image
import binascii
from StringIO import StringIO
import urllib

def main():
    if len(sys.argv) < 2:
        print("\nUsage: $ python pyTHETA.py command")
        print("'$ python pyTHETA.py help' for options\n")
    # elif len(sys.argv) > 2:
    #     print("\nUse only one argument.")
    else:
        help = ["help", "--help", "-h", "-help", "h"]
        if sys.argv[1] in help:
            print("""
Usage: $ python pyTHETA.py COMMAND
Available commands:
  startSession
  takePicture SID
  info
  state
  startCapture SID
  stopCapture SID
  latestFileUri
  getLatestImage
  listAll NUMBER
  getMode SID
  getSid
""")

        elif sys.argv[1] == "startSession":
            sid = startSession()
            print ("sessionId: {}".format(sid))
        elif sys.argv[1] == "takePicture":
            if len(sys.argv) < 3:
                print("Usage: pyTHETA.py takePicture SID_000X")
                print("Use 'state' to get sessionId")
            else:
                sid = startSession()
                response = takePicture(sid)
                pprint.pprint(response)
        elif sys.argv[1] == "getMode":
            sid = sys.argv[2]
            response = getMode(sid)
            pprint.pprint(response)
        elif sys.argv[1] == "getSid":
            response = getSid()
            pprint.pprint(response)

        elif sys.argv[1] == "info":
            response = info()
            pprint.pprint(response)
        elif sys.argv[1] == "state":
            response = state()
            pprint.pprint(response)
        elif sys.argv[1] == "startCapture":
            if len(sys.argv) < 3:
                print("Usage: pyTHETA.py startCapture SID_000X")
                print("Use 'state' to get sessionId")

            else:
                sid = sys.argv[2]
                response = startCapture(sid)
                pprint.pprint(response)
        elif sys.argv[1] == "stopCapture":
            if len(sys.argv) < 3:
                print("Usage: pyTHETA.py stopCapture SID_000X")
                print("Use 'state' to get sessionId")
            else:
                sid = sys.argv[2]
                response = stopCapture(sid)
                pprint.pprint(response)
        elif sys.argv[1] == "latestFileUri":
            data = latestFileUri()
            print(data)
        elif sys.argv[1] == "getLatestImage":
            fileUri = latestFileUri()
            getImage(fileUri)
        elif sys.argv[1] == "listAll":
            if len(sys.argv) > 2:
                listing_all = listAll(int(sys.argv[2]))
                pprint.pprint(listing_all)
            else:
                listing_all = listAll()
                pprint.pprint(listing_all)


if __name__ == '__main__':
    main()
