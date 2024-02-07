import json
import yaml

with open(r"C:\Users\SSLTP11522\OneDrive - SightSpectrum Technology Solutions Pvt. "
          r"Ltd\Documents\Python\Talend_CICD\IN_Exec_Plan.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

# Print the values as a dictionary
print(data['sequential'][0]['label'])
filename = "impEP_" + data['ep_label'] + ".json"

# Task details
child_parts = []
plans = data['sequential']
for i in range(1, len(plans)):
    partType = plans[i]['condition'].upper()
    planPartTaskId = plans[i]['label']

    # creat the current child part
    child_part = {
        "partType": partType,
        "planPartTaskId": planPartTaskId
    }
    if i == 0:
        child_parts.append(child_part)
    elif partType == "PARALLEL":
        child_parts.append(child_part)
    else:
        child_part_nested = [child_part]
        child_parts_nested = {"childParts": child_part_nested}
        child_parts.append(child_parts_nested)


# Plan details
dict_plan_det = {
    "desc": data['ep_description'],
    "execPlanRollBack": "test1",
    "execPlanTimeOut": "1000",
    "label": data['ep_label'],
    "pauseOnError": "true",
    "planParts": {
        "childParts": child_parts,
        "planPartTaskId": plans[0]['label']}
}

# Adding nested element
dict_plan = {
    "actionName": "importExecutionPlan",
    "authPass": "admin",
    "authUser": "admin@company.com",
    "result": {"ExecutionPlan": [dict_plan_det]}
}

with open(filename, "w") as outfile:
    json.dump(dict_plan, outfile)
