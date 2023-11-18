# -*- encoding=utf8 -*-
__author__ = "ASK"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1700279601888.png", record_pos=(0.385, -0.04), resolution=(2560, 1440)))
sleep(2)
if exists(Template(r"tpl1700280598556.png", record_pos=(-0.112, 0.2), resolution=(2560, 1440))):
    touch(Template(r"tpl1700280598556.png", record_pos=(-0.112, 0.2), resolution=(2560, 1440)))
sleep(2)


swipe(Template(r"tpl1700280484142.png", record_pos=(0.033, -0.083), resolution=(2560, 1440)), vector=[-0.2051, 0.0056])
touch(Template(r"tpl1700280506684.png", record_pos=(0.313, -0.008), resolution=(2560, 1440)))
sleep(2)

touch(Template(r"tpl1700279613596.png", record_pos=(-0.046, 0.12), resolution=(2560, 1440)))

sleep(2)

while(1):
    if exists(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440))):
        
        touch(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440)))
        sleep(2)
    else:
        continue
        
    while(1):
        if exists(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440))):
        
            touch(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440)))
            sleep(2)
            break
        else:
            continue
    touch(Template(r"tpl1700279639594.png", record_pos=(0.345, -0.109), resolution=(2560, 1440)))
        
    while(1):
        if exists(Template(r"tpl1700280039185.png", record_pos=(0.147, 0.105), resolution=(2560, 1440))):
            touch(Template(r"tpl1700280039185.png", record_pos=(0.147, 0.105), resolution=(2560, 1440)))
            sleep(2)
            break
        else:
            sleep(10)
            continue
    else:
        sleep(10)
        continue



# -*- encoding=utf8 -*-
__author__ = "ASK"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1700279601888.png", record_pos=(0.385, -0.04), resolution=(2560, 1440)))
sleep(2)
if exists(Template(r"tpl1700280598556.png", record_pos=(-0.112, 0.2), resolution=(2560, 1440))):
    touch(Template(r"tpl1700280598556.png", record_pos=(-0.112, 0.2), resolution=(2560, 1440)))
sleep(2)


swipe(Template(r"tpl1700280484142.png", record_pos=(0.033, -0.083), resolution=(2560, 1440)), vector=[-0.2051, 0.0056])
touch(Template(r"tpl1700280506684.png", record_pos=(0.313, -0.008), resolution=(2560, 1440)))
sleep(2)

touch(Template(r"tpl1700279613596.png", record_pos=(-0.046, 0.12), resolution=(2560, 1440)))

sleep(2)

while(1):
    if exists(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440))):
        
        touch(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440)))
        sleep(2)
    else:
        sleep(2)
        continue
        
    while(1):
        if exists(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440))):
        
            touch(Template(r"tpl1700279619195.png", record_pos=(0.326, 0.15), resolution=(2560, 1440)))
            sleep(2)
            break
        else:
            continue
    touch(Template(r"tpl1700279639594.png", record_pos=(0.345, -0.109), resolution=(2560, 1440)))
        
    while(1):
        if exists(Template(r"tpl1700280039185.png", record_pos=(0.147, 0.105), resolution=(2560, 1440))):
            touch(Template(r"tpl1700280039185.png", record_pos=(0.147, 0.105), resolution=(2560, 1440)))
            sleep(2)
            break
        else:
            sleep(10)
            continue


