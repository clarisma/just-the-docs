### `-b`, <code>--bbox=<em>&lt;W&gt;,&lt;S&gt;,&lt;E&gt;,&lt;N&gt;</em></code> {#option-bbox}

Defines the rectangular area (*bounding box*) to which the command should be applied.
Coordinates are specified in WGS-84 (degrees longitude and latitude) and take
the form `<west>,<south>,<east>,<north>`. Coordinates must not be separated by spaces
(otherwise, they would be interpreted as separate arguments).

As an alternative, this option accepts a tile descriptor in the form `z/x/y`. 
