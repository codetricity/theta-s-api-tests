import requests, json, pprint
import sys, io
from thetapylib import *
from PIL import Image
import binascii
from StringIO import StringIO

def main():
    if len(sys.argv) < 2:
        print("\nUsage: $ python pyTHETA.py command")
        print("'$ python pyTHETA.py help' for options\n")
    # elif len(sys.argv) > 2:
    #     print("\nUse only one argument.")
    else:
        if sys.argv[1] == "help":
            print("""
Help to be written.
Available commands:
  startSession
  takePicture
  info
  state
  startCapture
  stopCapture
  latestFileUri
  getLatestImage
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

        #    target = open("test_file.jpg", 'wb')


if __name__ == '__main__':
    main()
