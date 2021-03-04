# ping server with python

import subprocess
import platform

def ping(host):
    param = 'n' if platform.system() == 'windows' else '-c'
    command = ['ping', param, '5', host]
    return subprocess.call(command)

host = 'google.com'
print(ping(host))