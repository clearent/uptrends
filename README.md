# uptrends
Python scripts for interacting with the Uptrends API

## disable-checkpoint.py
Add checkpoint(s) to the Checkpoints list for a given probe/monitor.
<pre>python disable-checkpoint.py</pre>
You'll be prompted for your API username/password, the name of the probe/monitor you wish you to update, and the name
of the checkpoint to disable. You will have the option to enter "all" for the probe/monitor name to update all probes 
under your account.

## enable-checkpoint.py
Remove checkpoint(s) from the Checkpoints list on the probe/monitor.
<pre>python enable-checkpoint.py</pre>
You'll be prompted for your API username/password, the name of the probe/monitor you wish you to update, and the name
of the checkpoint to enable. You will have the option to enter "all" for the probe/monitor name to update all probes 
under your account.
