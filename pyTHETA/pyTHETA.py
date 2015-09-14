import requests, json, pprint
import sys
from thetapylib import *

def main():
    if len(sys.argv) < 2:
        print("\nUsage: $ python pyTHETA.py command")
        print("'$ python pyTHETA.py help' for options\n")
    elif len(sys.argv) > 2:
        print("\nUse only one argument.")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "help":
            print("""
Help to be written.
Available commands:
  startSession
  takePicture
  info
  state
""")

        elif sys.argv[1] == "startSession":
            sid = startSession()
            print ("sessionId: {}".format(sid))
        elif sys.argv[1] == "takePicture":
            sid = startSession()
            response = takePicture(sid)
            pprint.pprint(response)
        elif sys.argv[1] == "info":
            response = info()
            pprint.pprint(response)
        elif sys.argv[1] == "state":
            response = state()
            pprint.pprint(response)



if __name__ == '__main__':
    main()
