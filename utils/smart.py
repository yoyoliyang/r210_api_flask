from flask import Blueprint

import os
# http://192.168.1.123:9999/python-3.8.6-docs-html/library/shlex.html
from shlex import quote

bp = Blueprint('smart', __name__, url_prefix='/smart')

@bp.route('/<device_name>')
def get_hd_info(device_name):
    # get hardisk information to html
    if os.path.exists('/dev/' + device_name):
        with os.popen(f'/sbin/smartctl --all {quote(device_name)}') as f:
            return f'<pre>{f.read()}</pre>'
    else:
        return f'<pre>error {device_name} not found!</pre>'

@bp.route("/ps")
def get_hdd_ps():
        # 硬盘列表
        devs = 'abcd'

        # 硬盘状态列表
        ps = []

        # uptime
        uptime: str = os.popen('uptime').read().strip()

        for i in devs:
                cmd = f'/sbin/smartctl -i -n standby /dev/sd{i}'
                pow_sts = os.popen(cmd).readlines()[-1].strip()
                if 'STANDBY' in pow_sts:
                        ps.append(f'sd{i}: STANDBY')
                else:
                        ps.append(f'sd{i}: ACTIVE')

        return '|'.join(ps) + '|' + uptime
