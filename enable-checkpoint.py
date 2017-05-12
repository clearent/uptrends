import sys
import probes
import checkpointservers

user = sys.argv[1]
secret = sys.argv[2]
probeId = sys.argv[3]
checkpoint_name = sys.argv[4]

#get the probe to be updated and the id of the checkpoint to disable
checkpoint = checkpointservers.findCheckpointByName(checkpoint_name, user, secret)
print("Found checkpoint " + str(checkpoint["CheckPointID"])
      + " named " + checkpoint["CheckPointName"])

probe_list = []
if probeId == "all":
    probe_list = probes.getProbes(user, secret)
else:
    probe_list.append(probes.getProbe(probeId, user, secret))

for probe in probe_list:
    print("Adding checkpoint " + str(checkpoint["CheckPointID"])
          + " to probe " + probe["Name"])
    probes.addCheckpoint(checkpoint["CheckPointID"], probe, user, secret)

print("Complete")
