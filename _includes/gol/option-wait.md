{% comment %}

### `-w`, <code>--wait=<em>&lt;TIMESPAN&gt;</em></code>  ~~0.2~~ {#option-wait}

Length of time to wait for the GOL file to become available, in case it has been 
locked by another process.

The value is in seconds, or another time unit (`ms`, `s`, `m`, `h` or `d`). E.g. `--wait=600` or `--wait=10m` both cause the program to wait 10 minutes for the library to become unlocked.

If no wait is specified, the program blocks indefinitely.

{% endcomment %}
