import sys
import jenkins
import yaml
import json
 
jenkins = jenkins.Jenkins('http://desktop-p57l4i5:8080')

workspace = jenkins.get_job(sys.argv[1]).get_workspace()

with open(workspace + '/' + sys.argv[2], 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

print(data)