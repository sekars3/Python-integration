import sys
import yaml
import json


with open("C:/ProgramData/Jenkins/.jenkins/workspace/create-execution-plan/plan_details.txt", 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

print(data)