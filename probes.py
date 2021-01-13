import json
import requests

def getProbes(user, secret):
    probe_response = requests.get("https://api.uptrends.com/v4/Monitor",
                                  headers={'Accept': 'application/json'}, auth=(user, secret))
    probe_response.raise_for_status()
    probes = probe_response.json()
    return probes

def getProbe(probeId, user, secret):
    probe_response = requests.get("https://api.uptrends.com/v4/Monitor/"+probeId,
                                  headers={'Accept': 'application/json'}, auth=(user, secret))
    probe_response.raise_for_status()
    probe = probe_response.json()
    return probe

def addCheckpoint(checkpointId, probe, user, secret):
    if "Checkpoints" not in probe["SelectedCheckpoints"]:
        probe["SelectedCheckpoints"]["Checkpoints"] = []
    if checkpointId not in probe["SelectedCheckpoints"]["Checkpoints"]:
        print("Adding checkpoint " + str(checkpointId)
              + " to probe " + str(probe["MonitorGuid"] + " - " + probe["Name"]))
        probe["SelectedCheckpoints"]["Checkpoints"].append(checkpointId)
        updateProbe(probe["MonitorGuid"], probe, user, secret)

def removeCheckpoint(checkpointId, probe, user, secret):
    if "Checkpoints" not in probe["SelectedCheckpoints"]:
        print("No checkpoints defined for probe " + str(probe["MonitorGuid"] + " - " + probe["Name"]))
        return
        
    if checkpointId in probe["SelectedCheckpoints"]["Checkpoints"]:
        print("Removing checkpoint " + str(checkpointId)
              + " from probe " + str(probe["MonitorGuid"] + " - " + probe["Name"]))
        probe["SelectedCheckpoints"]["Checkpoints"].remove(checkpointId)
        updateProbe(probe["MonitorGuid"], probe, user, secret)

def updateProbe(probeId, payload, user, secret):
    update_data = {"MonitorGuid": payload["MonitorGuid"],
                   "SelectedCheckpoints": {"Checkpoints": payload["SelectedCheckpoints"]["Checkpoints"]
                                           }
                   }
    response = requests.patch("https://api.uptrends.com/v4/Monitor/" + probeId,
                             headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
                             auth=(user, secret),
                             data=str(json.dumps(update_data)))
    response.raise_for_status()
    return response
