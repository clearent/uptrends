# uptrends
Python scripts for interacting with the Uptrends API

## disable-checkpoint.py
Adds a checkpoint to the Checkpoints list for a given probe/monitor.
<pre>python disable-checkpoint.py {account_username} {account_password} {probe_id} {checkpoint_name}</pre>

Add a checkpoint to the Checkpoints list for ALL probes/monitors.
<pre>python disable-checkpoint.py {account_username} {account_password} all {checkpoint_name}</pre>

## enable-checkpoint.py
Removes a checkpoint from the Checkpoints list on the probe/monitor.
<pre>python enable-checkpoint.py {account_username} {account_password} {probe_id} {checkpoint_name}</pre>

Remove a checkpoint from the Checkpoints list for ALL probes/monitors.
<pre>python enable-checkpoint.py {account_username} {account_password} all {checkpoint_name}</pre>
