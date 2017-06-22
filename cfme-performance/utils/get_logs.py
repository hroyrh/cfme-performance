"""Collect evm logs from appliance"""
from utils.conf import cfme_performance
from utils.log import logger
import subprocess

def collect_logs():
    logger.info('Starting evm log collection')
    command_str = "mkdir -p cfme-performance/log/vmdb-logs/ ; scp root@" + cfme_performance['appliance']['ip_address'] + ":/var/www/miq/vmdb/log/* cfme-performance/log/vmdb-logs/"
    print subprocess.Popen(command_str, shell=True, stdout=subprocess.PIPE).stdout.read()
    command_str = "mkdir -p cfme-performance/log/system-logs/ ; scp root@" + cfme_performance['appliance']['ip_address'] + ":/var/log/* cfme-performance/log/system-logs/"
    print subprocess.Popen(command_str, shell=True, stdout=subprocess.PIPE).stdout.read()
    logger.info('evm log collection Finished')
