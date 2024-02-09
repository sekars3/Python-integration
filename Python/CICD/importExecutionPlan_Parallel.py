import json
import yaml

with open(r"IN_Exec_Plan_Parallel.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

filename = "impEP_" + data['ep_label'] + ".json"

# Task details
child_parts = []
plans = data['parallel']
for plan in plans:

    # create the current child part
    child_part = {
        "partType": "PARALLEL",
        "planPartTaskId": plan['label']
    }

    child_parts.append(child_part)


# Plan details
dict_plan_det = {
    "desc": data['ep_description'],
    "execPlanRollBack": "test1",
    "execPlanTimeOut": "1000",
    "label": data['ep_label'],
    "pauseOnError": "true",
    "planParts": {
        "childParts": child_parts,
        "planId": data['ep_label'],
        "useParalle": True,
        "partType": "NONE"}
}

# Adding nested element
dict_plan = {
    "actionName": "importExecutionPlan",
    "authPass": "admin",
    "authUser": "admin@company.com",
    "result": {"ExecutionPlan": [dict_plan_det]}
}

with open(filename, "w") as outfile:
    json.dump(dict_plan, outfile, indent=4)
