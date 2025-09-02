# Geometry Dash Server URL Replacer
# https://github.com/ClassiDash/Tools
# classidash.com

import sys, base64

BASE_URL = "http://www.boomlings.com/database"
BASE_PACKAGE = "robtopx"
BASE_LENGTH = len(BASE_URL)
ARGUMENTS = sys.argv

ANDROID = len(ARGUMENTS) > 1 and ARGUMENTS[1].lower() == "-a"

if len(ARGUMENTS) < 3:
    exit(
        f"Usage: replacer [-a] {'com.GDPSNAME.geometryjump' if ANDROID else 'path/to/gdps.exe'} https://yourserver.com\
        {'' if ANDROID else '\n\nOptions:\n-a      Replace Android strings'}"
    )

if ANDROID:
    executable = "libcocos2dcpp.so"
else:
    executable = ARGUMENTS[1]
    if not executable.split(".")[-1] == "exe":
        executable += ".exe"

replacement_url = ARGUMENTS[2]

if not replacement_url.startswith("http"):
    http_correct = input("Your replacement URL doesn't begin with http:// or https://, are you sure this is correct? (Y/N): ")
    if not http_correct.lower() != "y" and http_correct.lower() != "yes":
        exit("Cancelled.") 

input_length = len(replacement_url)

if not ANDROID:
    if input_length > BASE_LENGTH:
        exit(f"The length of your replacement url ({input_length}) is longer than 24 characters!")

    if input_length < BASE_LENGTH:
        replacement_url += "/" * (BASE_LENGTH - input_length)

permitted = input(f"All instances of {BASE_URL} in {executable} will be replaced with {replacement_url}, do you want to continue? (Y/N): ")
if permitted.lower() != "y" and permitted.lower() != "yes":
    exit("Cancelled.")

BASE_B64 = base64.b64encode(BASE_URL.encode())
REPLACEMENT_B64 = base64.b64encode(replacement_url.encode())

input_bytes = open(executable, "rb").read()
output_bytes = input_bytes\
    .replace(BASE_URL.encode(), replacement_url.encode())\
    .replace(BASE_B64, REPLACEMENT_B64)

if ANDROID:
    output_bytes = output_bytes.replace(b"robtopx", executable.encode())

out = "libcocos2dcpp_Replaced.so" if ANDROID else executable[:-4] + "_Replaced.exe"
open(out, "wb+").write(output_bytes)
print(f"Strings have been replaced, your modified file is saved as {out}")
if ANDROID: print("Remember to rename libcocos2dcpp_Replaced.so back to libcocos2dcpp.so")