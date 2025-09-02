# ClassiDash Demonlist Updater
# https://github.com/ClassiDash/Tools
# classidash.com

import sys, json

ARGUMENTS = sys.argv

if len(ARGUMENTS) < 3:
    exit("Usage: listupdater input.json output.json")

INPUT_PATH = ARGUMENTS[1]
OUTPUT_PATH = ARGUMENTS[2]

if not INPUT_PATH.endswith(".json"):
    json_correct = input("Your input file doesn't begin with .json, are you sure this is correct?")
    if not json_correct.lower() != "y" and json_correct.lower() != "yes":
        exit("Cancelled.")

OUTPUT_FORMAT = {
    "id": "",
    "name": "name",
    "ingameId": "_id",
    "creator": "creators",
    "verifierName": "verifier",
    "verifierId": "",
    "videoUrl": "video"
}

input_list = json.load(
    open(INPUT_PATH, "r")
)

output_list = []

for i, input_level in enumerate(input_list):
    level = {}

    for k, v in OUTPUT_FORMAT.items():
        if k == "ID":
            level[k] = i
            continue
        
        if v.startswith("_"):
            level[k] = int(input_level.get(v[1:], 0))
            continue

        level[k] = input_level.get(v, "")

    output_list.append(level)

json.dump(
    output_list, 
    open(OUTPUT_PATH, "w+"),
    indent=2
)