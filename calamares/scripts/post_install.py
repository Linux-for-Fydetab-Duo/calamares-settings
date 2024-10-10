# /usr/bin/env python3 
# -*- coding: utf-8 -*-

import os
import subprocess

# Remove live user service
rm_live_user_service = '''
[Unit]
Description=Remove live user

[Service]
Type=oneshot
ExecStartPre=userdel -rf arch
ExecStart=systemctl disable remove-live-user.service

[Install]
WantedBy=multi-user.target
'''
# remove calamares service

rm_calamares_service = '''
[Unit]
Description=Remove Calamares

[Service]
Type=oneshot
ExecStartPre=sudo pacman -Rncsu --noconfirm calamares calamares-settings-fydetab
ExecStart=systemctl disable remove-calamares.service

[Install]
WantedBy=multi-user.target'''
with open('/usr/lib/systemd/system/remove-live-user.service', 'w') as f:
    f.write(rm_live_user_service)
with open('/usr/lib/systemd/system/remove-calamares.service', 'w') as f:
    f.write(rm_calamares_service)
subprocess.run(['systemctl', 'daemon-reload'])
subprocess.run(['systemctl', 'enable', 'remove-live-user.service'])
subprocess.run(['systemctl', 'enable', 'remove-calamares.service'])
try:
    #/etc/sudoers.d/g_wheel
    #/etc/polkit-1/rules.d/49-nopasswd_global.rules
    os.remove('/etc/sudoers.d/g_wheel')
    os.remove('/etc/polkit-1/rules.d/49-nopasswd_global.rules')
except OSError as e:
    print(e)
    pass

# TODO: remove autologin from gdm

