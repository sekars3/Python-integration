import yaml, json

with open(r"IN_Exec_Plan.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

# Print the values as a dictionary
print(data)

with open("yaml_source.json", "w") as outfile:
    json.dump(data, outfile, indent=4)