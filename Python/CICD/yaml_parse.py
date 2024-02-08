import yaml, json

with open(r"IN_Exec_Plan_Sequential.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

# Print the values as a dictionary
print(data)