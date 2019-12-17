import requests

def getCheckpoints(user, secret):
    checkpoints_response = requests.get("https://api.uptrends.com/v4/Checkpoint",
        headers={'Accept': 'application/json'}, auth=(user, secret))
    checkpoints_response.raise_for_status()
    checkpoints = checkpoints_response.json()
    return checkpoints

def findCheckpointByName(checkpoint_name, user, secret):
    #get all the available checkpoints
    checkpoints = getCheckpoints(user, secret)

    #walk the list until we find the one that matches
    checkpoint = None
    for item in checkpoints["Data"]:
        if checkpoint_name in item["Attributes"]["CheckpointName"]:
            checkpoint = item
    return checkpoint
