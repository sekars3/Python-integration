import sys
import yaml
import json


with open(sys.argv[1] + "/" + sys.argv[2], 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

print(data)