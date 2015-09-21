"""
Example library for RICOH THETA S hacking with Python.  The new
API is compliant with the Open Spherical Camera specification.
This is intended to show how the THETA S API works.  It is
not intended for use in your program.  There is no error
checking and this example library only handles a handful
of commands.


There are three example programs that use this library.
At the top of your Python script, use

  from thetapylib import *

After you import the library, you can use the commands like this:

  state()

That will return the state of the camera, which is great to
get the sessionId.

You can also get the sessionId when you start a new session:

  startSession()

In fact, the startSession() function will return the
sessionId.

Example use of the library with Pygame to detect the
button press.

          if event.type == pygame.MOUSEBUTTONDOWN:
              mouse_pos = pygame.mouse.get_pos()
              if pictureButton.collidepoint(mouse_pos):
                  sid = startSession()
                  takePicture(sid)
              if captureStartButton.collidepoint(mouse_pos):
                  sid = startSession()
                  startCapture(sid)
              if captureStopButton.collidepoint(mouse_pos):
                  stopCapture(sid)

Example use of library from the command line:

        if sys.argv[1] == "startCapture":
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

"""
import requests, json
# import pprint # for printing out test data
# from PIL import Image
# from StringIO import StringIO

def request(url_request):
    """
    Generate the URI to send to the THETA S.  The THETA IP address is
    192.168.1.1
    All calls start with /osc/
    """
    url_base = "http://192.168.1.1/osc/"
    url = url_base + url_request
    return url

def startSession():
    """
    Start a new session.  Grab the sessionId number and
    return it.
    You'll need the sessionId to take a video or image.
    """
    url = request("commands/execute")
    body = json.dumps({"name": "camera.startSession",
         "parameters": {}
         })
    req = requests.post(url, data=body)
    response = req.json()
    sid = (response["results"]["sessionId"])
    return sid

def takePicture(sid):
    """
    Take a still image.  The sessionId is either taken from
    startSession or from state.  You can change the mode
    from video to image with captureMode in the options.
    """
    url = request("commands/execute")
    body = json.dumps({"name": "camera.takePicture",
         "parameters": {
            "sessionId": sid
         }
         })
    req = requests.post(url, data=body)
    response = req.json()
    return response

def info():
    """
    Get basic information ont he camera.  Note that this is a GET call
    and not a POST.  Most of the calls are POST.
    """
    url = request("info")
    req = requests.get(url)
    response = req.json()
    return response

def state():
    """
    Get the state of the camera, which will include the sessionsId and also the
    latestFileUri if you've just taken a picture.
    """
    url = request("state")
    req = requests.post(url)
    response = req.json()
    return response

def startCapture(sid):
    """
    Begin video capture if the captureMode is _video.  If the
    captureMode is set to image, the camera will take multiple
    still images.  The captureMode can be set in the options.
    Note that this will not work with streaming video using the
    HDMI or USB cable.
    """
    url = request("commands/execute")
    body = json.dumps({"name": "camera._startCapture",
         "parameters": {
            "sessionId": sid
         }
         })
    req = requests.post(url, data=body)
    response = req.json()
    return response


def stopCapture(sid):
    """
    Stop video capture.  If in image mode, will stop
    automatic image taking.
    """
    url = request("commands/execute")
    body = json.dumps({"name": "camera._stopCapture",
         "parameters": {
            "sessionId": sid
         }
         })
    req = requests.post(url, data=body)
    response = req.json()
    return response

def latestFileUri():
    """
    This will only work if you've just taken a picture.  The state
    will include the attribute latestFileUri.  You need this to
    transfer the file from the camera to your computer or phone.
    """
    state_data = state()["state"]
    latestFileUri = state_data["_latestFileUri"]
    return latestFileUri

def getImage(fileUri, imageType="image"):
    """
    Transfer the file from the camera to computer and save the
    binary data to local storage.  This works, but is clunky.
    There are easier ways to do this. The __type parameter
    can be set to "thumb" for a thumbnail or "image" for the
    full-size image.  The default is "image".
    """
    url = request("commands/execute")
    body = json.dumps({"name": "camera.getImage",
         "parameters": {
            "fileUri": fileUri,
            "_type": imageType
         }
         })
    fileName = fileUri.split("/")[1]
    print(fileName)
    with open(fileName, 'wb') as handle:
        response = requests.post(url, data=body, stream=True)
        for block in response.iter_content(1024):
            handle.write(block)

def listAll(entryCount = 3, detail = False, sortType = "newest", ):
    """
    entryCount:
            Integer	No. of still images and video files to be acquired
    detail:
            Boolean	(Optional)  Whether or not file details are acquired
            true is acquired by default. Only values that can be acquired
            when false is specified are "name", "uri", "size" and "dateTime"
    sort:
            String	(Optional) Specify the sort order
            newest (dateTime descending order)/ oldest (dateTime ascending order)
            Default is newest
    """
    url = request("commands/execute")
    body = json.dumps({"name": "camera._listAll",
         "parameters": {
            "entryCount": entryCount,
            "detail": detail,
            "sort": sortType
         }
         })
    req = requests.post(url, data=body)
    response = req.json()
    return response
