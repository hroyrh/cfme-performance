"""Run before test"""
import yaml
import subprocess


stream = open("cfme-performance/conf/cfme_performance.yml", "r")
confyml = yaml.load(stream)

confyml['collect_logs'] = 'true'
#i = 0
#while i < len(confyml['tests']['workloads']['test_refresh_vms']['scenarios']):
#    if not 'rhos7' in confyml['tests']['workloads']['test_refresh_vms']['scenarios'][i]['name']:
#        del confyml['tests']['workloads']['test_refresh_vms']['scenarios'][i]
#    i = i + 1

with open("cfme-performance/conf/cfme_performance.yml", "w") as outfile:
    yaml.dump(confyml, outfile, default_flow_style=False)
