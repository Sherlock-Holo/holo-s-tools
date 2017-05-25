#!/usr/bin/env python3

import dbus
import requests
from systemd import journal
from time import sleep


def ping(addr):
    try:
        r = requests.get(addr, timeout=1)
        return r.ok

    except requests.exceptions.ConnectionError:
        return False


def service(name, handle='restart'):
    if '.service' in name:
        servicename = name
    else:
        servicename = name + '.service'

    sysbus = dbus.SystemBus()
    systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
    manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')

    if handle == 'restart':
        job = manager.RestartUnit(servicename, 'fail')
        journal.send('service is restarting...')

    elif handle == 'stop':
        job = manager.StopUnit(servicename, 'fail')
        journal.send('service is stopping...')

    elif handle == 'start':
        job = manager.StartUnit(servicename, 'fail')
        journal.send('service is starting...')


if __name__ == '__main__':
    while 1:
        rs = ping('https://www.google.com')

        if rs:
            pass
        else:
            service('network', 'restart')

        sleep(60)
