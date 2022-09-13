from itertools import count
import sys
import requests
import json
import os
import ctypes

def weather():
    if len(sys.argv) == 2:
        request = requests.post('http://ip-api.com/json/').json()

        return 'API is working (' + request['city'] + ') but couldn''t fetch the temperature.'
    else:
        return "Too many arguments."

def openApp():
    if len(sys.argv) != 2:
        return 'Missing application name.'

    try:
        os.system(sys.argv[2])
    except:
        return 'Couldn''t open the application.'

def whoami():
    request = requests.post('http://ip-api.com/json/').json()

    return os.environ['UserName'] + ' (' + os.environ['COMPUTERNAME'] + ')' + " [" + request['query'] + "]"

def pcInfo():
    request = requests.post('http://ip-api.com/json/').json()

    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()

    return [ request['country'], request['countryCode'], request['regionName'], request['region'], request['city'], request['zip'],
    request['lat'], request['lon'], request['timezone'], request['isp'], request['org'], request['as'], request['query'], 'Admin permissions: ' + str(is_admin)]

commands = {
    'weather': weather(),
    'open': openApp(), #WIP
    'whoami': whoami(),
    'info': pcInfo()
}

print(commands[sys.argv[1]])
