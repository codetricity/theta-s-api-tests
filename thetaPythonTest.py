import requests, json, pprint



def request(url_request):
    url_base = "http://192.168.1.1/osc/"
    url = url_base + url_request
    return url

def basic_info():
    protocols = [
        "state",
        "info"
    ]
    for protocol in protocols:
        print(60 * "=")
        print(protocol + " - Testing RICOH THETA API v2\n")
        url = request(protocol)
        if protocol == "info":
            req = requests.get(url)
        else:
            req = requests.post(url)
        pprint.pprint(req.json())

def startSession():
    url = request("commands/execute")
    body = json.dumps({"name": "camera.startSession",
         "parameters": {}
         })
    req = requests.post(url, data=body)
    response = req.json()
    print(60 * "=")
    print("startSession - Testing RICOH THETA API v2\n")
    pprint.pprint(response)
    sid = (response["results"]["sessionId"])
    print sid
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
    print(60 * "=")
    print("takePicture - Testing RICOH THETA API v2\n")
    pprint.pprint(response)

def main():
    basic_info()
    sid = startSession() #grab session ID
    takePicture(sid) #still image

if __name__ == '__main__':
    main()

# url =  base_url + "commands/execute"

#req = requests.post(url, data=body)
