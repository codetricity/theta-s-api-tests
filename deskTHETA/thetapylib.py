import requests, json

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
