#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 20251126

import os
import sys
import subprocess
import threading
import time
from datetime import datetime

# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

ip_lists = ['192.168.1.1']
default_username = 'admin'
default_password = 'Linksys123!'
output_file = "sysinfo.txt"

class wget_sysinfo_runner:
    target_ip = None
    device_username=default_username
    device_password=default_password
    output_file = None
    wget_interval = 3600
    sysinfo_filename = 'sysinfo.cgi'
    keep_wget = True

    def __init__(self, ip_address):
        if ip_address:
            self.target_ip = ip_address
            self.output_file = output_file
            self.wget_thread = threading.Thread(target=self.keep_wget)
            self.wget_thread.start()

    def keep_wget(self):
        next_start_time = datetime.now().timestamp() - 1
        while self.keep_wget:
            while datetime.now().timestamp() > next_start_time:
                next_start_time += self.wget_interval
                current_time_stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
                try:
                    wget_result = subprocess.Popen(
                        'wget --http-user={username} --http-password={password} --no-check-certificate http://{device_ip}/sysinfo.cgi'.format(
                            username=self.device_username,
                            password=self.device_password,
                            device_ip=self.target_ip),
                        stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

                    result_file_name = "{device_ip}_sysinfo_{time_stamp}.txt".format(
                        device_ip=self.target_ip,
                        time_stamp=current_time_stamp)
                    os.replace(self.sysinfo_filename, result_file_name)
                    print("{} : wget {} finish.".format(
                        current_time_stamp, self.target_ip))
                except:
                    print("{} : wget {} unknown error!".format(
                    current_time_stamp, self.target_ip))
            time.sleep(1)

for target_ip in ip_lists:
    print(wget_sysinfo_runner(target_ip))
