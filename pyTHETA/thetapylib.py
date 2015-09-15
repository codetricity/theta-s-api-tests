import requests, json
import pprint # for printing out of test data
from PIL import Image
from StringIO import StringIO

def request(url_request):
    url_base = "http://192.168.1.1/osc/"
    url = url_base + url_request
    return url

def startSession():
    url = request("commands/execute")
    body = json.dumps({"name": "camera.startSession",
         "parameters": {}
         })
    req = requests.post(url, data=body)
    response = req.json()
    sid = (response["results"]["sessionId"])
    return sid

def takePicture(sid):
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
    url = request("info")
    req = requests.get(url)
    response = req.json()
    return response

def state():
    url = request("state")
    req = requests.post(url)
    response = req.json()
    return response

def startCapture(sid):
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
    state_data = state()["state"]
    latestFileUri = state_data["_latestFileUri"]
    return latestFileUri

def getImage(fileUri):
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
    # i = Image.open(StringIO(req.content))
    # with open("test_file.bin", 'wb') as f:
    #     f.write(req.content)
