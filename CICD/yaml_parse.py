import yaml, json

with open(r"C:\Users\SSLTP11522\OneDrive - SightSpectrum Technology Solutions Pvt. Ltd\Documents\Python\Talend_CICD\IN_Exec_Plan.yaml") as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

# Print the values as a dictionary
print(data)