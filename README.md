# uptrends
Python scripts for interacting with the Uptrends API

## disable-checkpoint.py
Adds a checkpoint to the exclusion list for a given probe/monitor.
<pre>python disable-checkpoint.py account_username account_password probe_id checkpoint_name</pre>

## enable-checkpoint.py
Removes a checkpoint from the exclusion list on the probe/monitor.
<pre>python enable-checkpoint.py account_username account_password probe_id checkpoint_name</pre>
