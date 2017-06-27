"""Collect evm logs from appliance"""
from utils.conf import cfme_performance
from utils.log import logger
import subprocess

def collect_logs():
    logger.info('Starting evm log collection')
    subprocess.check_call(["mkdir", "-p", "cfme-performance/log/vmdb-logs/"])
    logstr = "root@" + cfme_performance['appliance']['ip_address'] + ":/var/www/miq/vmdb/log/*"
    subprocess.check_call(["scp", logstr, "cfme-performance/log/vmdb-logs/"])

    subprocess.check_call(["mkdir", "-p", "cfme-performance/log/system-logs/"])
    logstr = "root@" + cfme_performance['appliance']['ip_address'] + ":/var/log/*"
    subprocess.check_call(["scp", logstr, "cfme-performance/log/system-logs/"])

    subprocess.check_call(["sleep", "300"])

    logger.info('evm log collection Finished')
    #command_str = "mkdir -p cfme-performance/log/vmdb-logs/ ; scp root@" + cfme_performance['appliance']['ip_address'] + ":/var/www/miq/vmdb/log/* cfme-performance/log/vmdb-logs/"
    #print subprocess.Popen(command_str, shell=True, stdout=subprocess.PIPE).stdout.read()
    #command_str = "mkdir -p cfme-performance/log/system-logs/ ; scp root@" + cfme_performance['appliance']['ip_address'] + ":/var/log/* cfme-performance/log/system-logs/"
    #print subprocess.Popen(command_str, shell=True, stdout=subprocess.PIPE).stdout.read()
    #logger.info('evm log collection Finished')
