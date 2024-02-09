import json
import yaml

from CICD.import_plan_json import create_nested_json

with open(r"IN_Exec_Plan_Sequential.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

filename = "impEP_" + data['ep_label'] + ".json"

# Task details
child_parts = []
plans = data['sequential']

root_task = plans.pop(0)

nested_json = {
    "planParts": {
        "childParts": [create_nested_json(plans)],
        "partType": "NONE",
        "planPartTaskId": root_task["label"],
        "useParalle": False
    }
}



# Plan details
dict_plan_det = {
    "desc": data['ep_description'],
    "execPlanRollBack": "test1",
    "execPlanTimeOut": "1000",
    "label": data['ep_label'],
    "pauseOnError": "true"
}

dict_plan_det["planParts"] = nested_json["planParts"]





# Adding nested element
dict_plan = {
    "actionName": "importExecutionPlan",
    "authPass": "admin",
    "authUser": "admin@company.com",
    "result": {"ExecutionPlan": [dict_plan_det]}
}

with open(filename, "w") as outfile:
    json.dump(dict_plan, outfile, indent=4)
