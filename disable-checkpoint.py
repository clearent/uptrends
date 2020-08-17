import sys
import probes
import checkpointservers
from requests import exceptions

user = sys.argv[1]
secret = sys.argv[2]
probeId = sys.argv[3]
checkpoint_name = sys.argv[4]

#get the probe to be updated and the id of the checkpoint to disable
checkpoint = checkpointservers.findCheckpointByName(checkpoint_name, user, secret)
print("Found checkpoint " + str(checkpoint["Id"])
      + " named " + checkpoint["Attributes"]["CheckpointName"])

probe_list = []
if probeId == "all":
    probe_list = probes.getProbes(user, secret)
else:
    probe_list.append(probes.getProbe(probeId, user, secret))

update_failures = []
for probe in probe_list:
    print("Removing checkpoint " + str(checkpoint["Id"])
          + " from probe " + probe["Name"])
    try:
        probes.removeCheckpoint(checkpoint["Id"], probe, user, secret)
    except exceptions.HTTPError as err:
        print("Failed to remove checkpoint from probe " + probe["Name"] + " - " + str(err))
        update_failures.append(probe)

print("Complete")
if len(update_failures) > 0:
    print("\nNOTE: Failed to remove checkpoint from following probe(s).  Please update manually.")
    for probe in update_failures:
        print(probe["Name"])
