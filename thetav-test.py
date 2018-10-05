import requests
import pprint


url = "http://192.168.1.1/osc/"
header = {'Content-Type': 'application/json'}


def state(url, header):
    url = url + "state"
    req = requests.post(url, headers=header)
    response = req.json()
    return response


def info(url):
    url = url + "info"
    req = requests.get(url)
    response = req.json()
    return response


def takePicture(url, header):
    url = url + "commands/execute"
    payload = {"name": "camera.takePicture"}
    req = requests.post(
        url, json=payload)
    response = req.json()
    return response


pprint.pprint(info(url))

pprint.pprint(state(url, header))

pprint.pprint(takePicture(url, header))
