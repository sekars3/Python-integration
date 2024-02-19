import sys
import json
import yaml
from import_plan_json import create_parallel_json, create_nested_json, create_plan_parts

with open(sys.argv[1] + "/" + sys.argv[2], 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

with open("yaml_source.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

# Print the values as a dictionary
# print(data)
filename = "impEP_" + sys.argv[5] + ".json"

# Initializing planParts dictionary
# planParts = create_plan_parts(data)

planParts = create_plan_parts(data)

planParts["planId"] = sys.argv[5]
planParts["useParalle"] = True
planParts["partType"] = "NONE"

# Plan details)
dict_plan_det = {
    "desc": sys.argv[6],
    "execPlanRollBack": "test1",
    "execPlanTimeOut": "1000",
    "label": sys.argv[5],
    "pauseOnError": sys.argv[7]
}

dict_plan_det["planParts"] = planParts

# Adding nested element
dict_plan = {
    "actionName": "importExecutionPlan",
    "authPass": sys.argv[4],
    "authUser": sys.argv[3],
    "result": {"ExecutionPlan": [dict_plan_det]}
}

with open(filename, "w") as outfile:
    json.dump(dict_plan, outfile, indent=4)
