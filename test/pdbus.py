import dbus
from time import sleep


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
        print('service is restarting...')

    elif handle == 'stop':
        job = manager.StopUnit(servicename, 'fail')
        print('service is stopping...')

    elif handle == 'start':
        job = manager.StartUnit(servicename, 'fail')
        print('service is starting...')

if __name__ == '__main__':
    while 1:
        service('network', 'restart')
