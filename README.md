# GDPS Tools
A collection of small scripts/tools useful for GDPS creation.

## replacer.py
Replaces strings Geometry Dash uses for communicating with its servers with custom ones.

Example (PC):\
    `py replacer.py GeometryDash.exe https://classidash.com`

Example (Android):\
    `py replacer.py -a com.classidash.geometryjump https://classidash.com`\
    NOTE: Your **libcocos2dcpp.so** file must be located in the same directory as the replacer script