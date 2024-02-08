input_json = {
    "project": "Kinaxis",
    "sequential": [
        {"label": "D_task_1", "condition": "none"},
        {"label": "D_task_2", "condition": "on_ok"},
        {"label": "D_task_3", "condition": "on_ok"},
        {"label": "D_task_4", "condition": "on_ok"},
    ]
}

def create_nested_json(tasks):
    if not tasks:
        return None
    first_task = tasks.pop(0)
    nested_json = {
        "partType": first_task["condition"].upper(),
        "planPartTaskId": first_task["label"],
        "useParalle": False
    }

    if tasks:
        nested_json["childParts"] = [create_nested_json(tasks)]

    return nested_json

nested_json = {
    "planParts": {
        "childParts": [create_nested_json(input_json["sequential"])]
        #"partType": "ON_OK",
        #"planPartTaskId": "D_task_Custom_Kinaxis_SAPECC_Transform_Part_BT_MC4"
    }
}

import json
print(json.dumps(nested_json, indent=2))

with open("nested_json.json", "w") as outfile:
    json.dump(nested_json, outfile, indent=4)