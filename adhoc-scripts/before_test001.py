"""Run before test"""
import yaml
import subprocess


stream = open("cfme-performance/conf/cfme_performance.yml", "r")
confyml = yaml.load(stream)

for scenario in list(confyml['tests']['workloads']['test_refresh_vms']):
    if not 'rhos7' in scenario:
        del confyml['tests']['workloads']['test_refresh_vms'][scenario]

confile = open("cfme-performance/conf/cfme_performance.yml", "w")
confile.write(confyml)
confile.close()
