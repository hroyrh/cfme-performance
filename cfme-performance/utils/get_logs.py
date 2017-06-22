"""Collect evm logs from appliance"""
from utils.conf import cfme_performance
from utils.log import logger
import subprocess

def collect_logs():
    logger.info('Starting evm log collection')
    command_str = "scp root@" + cfme_performance['appliance']['ip_address'] + ":/var/www/miq/vmdb/log/evm.log* cfme-performance/log/"
    print subprocess.Popen(command_str, shell=True, stdout=subprocess.PIPE).stdout.read()
    logger.info('evm log collection Finished')
