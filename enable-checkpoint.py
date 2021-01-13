import probes
import checkpointservers
from requests import exceptions

user = input("Enter your Uptrends API user ID: ")
secret = input("Enter your Uptrends API secret: ")
probeId = input("Enter name of probe/monitor to update (or enter 'all' to update all probes under your account): ")
checkpoint_name = input("Enter name of checkpoint to enable: ")

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
    if "Regions" in probe["SelectedCheckpoints"]:
        print("Probe " + probe["Name"] + " is using region(s) instead of individual checkpoints - skipping")
    else:
        print("Adding checkpoint " + str(checkpoint["Id"])
              + " to probe " + probe["Name"])
        try:
            probes.addCheckpoint(checkpoint["Id"], probe, user, secret)
        except exceptions.HTTPError as err:
            print("Failed to add checkpoint to probe " + probe["Name"] + " - " + str(err))
            update_failures.append(probe)

print("Complete")
if len(update_failures) > 0:
    print("\nNOTE: Failed to add checkpoint to following probe(s).  Please update manually.")
    for probe in update_failures:
        print(probe["Name"])
