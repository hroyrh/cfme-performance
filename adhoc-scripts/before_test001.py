"""Run before test"""
import yaml
import subprocess


stream = open("cfme-performance/conf/cfme_performance.yml", "r")
confyml = yaml.load(stream)

for scenario in list(confyml['tests']['workloads']['test_refresh_vms']['scenarios']):
    if not 'rhos7' in scenario:
        del confyml['tests']['workloads']['test_refresh_vms']['scenarios'][scenario]

with open("cfme-performance/conf/cfme_performance.yml", "w") as outfile:
    yaml.dump(confyml, outfile, default_flow_style=False)
