"""Run before test"""
import yaml
import subprocess


stream = open("cfme-performance/conf/cfme_performance.yml", "r")
confyml = yaml.load(stream)

for scenario in confyml['tests']['workloads']['test_refresh_vms']:
    if not 'rhevm' in scenario:
        del confyml['tests']['workloads']['test_refresh_vms'][scenario]
        
