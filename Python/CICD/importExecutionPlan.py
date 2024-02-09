import json
import yaml
from CICD.import_plan_json import create_parallel_json, create_nested_json, create_plan_parts

with open(r"IN_Exec_Plan.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

with open("yaml_source.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

# Print the values as a dictionary
# print(data)
filename = "impEP_" + data['ep_label'] + ".json"

# Initializing planParts dictionary
# planParts = create_plan_parts(data)

planParts = create_plan_parts(data)

planParts["planId"] = data['ep_label']
planParts["useParalle"] = True
planParts["partType"] = "NONE"

# Plan details)
dict_plan_det = {
    "desc": data['ep_description'],
    "execPlanRollBack": "test1",
    "execPlanTimeOut": "1000",
    "label": data['ep_label'],
    "pauseOnError": "true"
}

dict_plan_det["planParts"] = planParts

# Adding nested element
dict_plan = {
    "actionName": "importExecutionPlan",
    "authPass": "admin",
    "authUser": "admin@company.com",
    "result": {"ExecutionPlan": [dict_plan_det]}
}

with open(filename, "w") as outfile:
    json.dump(dict_plan, outfile, indent=4)
