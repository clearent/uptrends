import json
import requests

def getProbe(probeId, user, secret):
    probe_response = requests.get("https://api.uptrends.com/v3/probes/"+probeId,
        headers={'Accept': 'application/json'}, auth=(user, secret))
    probe_response.raise_for_status()
    probe = probe_response.json()
    return probe

def addCheckpointExclusion(checkpointId, probe, user, secret):
    #the checkpoints are stored as a json-formatted string, so we have to reparse it
    checkpoints = json.loads(probe["Checkpoints"])
    if not "ExcludeLocations" in checkpoints:
        checkpoints["ExcludeLocations"] = []
    excludes = checkpoints["ExcludeLocations"]
    if checkpointId not in excludes:
        print("Updating probe " + str(probe["Guid"]) + " - " + probe["Name"])
        excludes.append(checkpointId)
        checkpoints["ExcludeLocations"] = excludes
        checkpoints = json.dumps(checkpoints) #dump it back to a json string
        updateProbe(probe["Guid"], '{"Checkpoints":' + checkpoints + '}', user, secret)

def removeCheckpointExclusion(checkpointId, probe, user, secret):
    #the checkpoints are stored as a json-formatted string, so we have to reparse it
    checkpoints = json.loads(probe["Checkpoints"])
    if "ExcludeLocations" not in checkpoints:
        checkpoints["ExcludeLocations"] = []
    excludes = checkpoints["ExcludeLocations"]
    if checkpointId in excludes:
        print("Updating probe " + str(probe["Guid"]) + " - " + probe["Name"])
        excludes.remove(checkpointId)
        checkpoints["ExcludeLocations"] = excludes
        checkpoints = json.dumps(checkpoints) #dump it back to a json string
        updateProbe(probe["Guid"], '{"Checkpoints":' + checkpoints + '}', user, secret)

def updateProbe(probeId, payload, user, secret):
    response = requests.post("https://api.uptrends.com/v3/probes/" + probeId,
        headers={'Content-type': 'application/json', 'Accept': 'application/json'},
        auth=(user, secret),
        json=json.loads(payload))
    response.raise_for_status()
    return response
