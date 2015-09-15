"""
Example library for RICOH THETA S hacking with Python.  The new
API is compliant with the Open Spherical Camera specification.
There are three example programs that use this library.
At the top of your Python script, use
  from thetalib import *

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
"""
import requests, json
import pprint # for printing out of test data
from PIL import Image
from StringIO import StringIO

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
    startSession or from state.
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
    Stop video capture
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

def getImage(fileUri):
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
#            "_type": "thumb"
            "_type": "image"
         }
         })
    with open('output.jpg', 'wb') as handle:
        response = requests.post(url, data=body, stream=True)
        for block in response.iter_content(1024):
            handle.write(block)
