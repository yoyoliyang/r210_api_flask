from flask import Blueprint, jsonify, current_app

import os
# http://192.168.1.123:9999/python-3.8.6-docs-html/library/shlex.html
from shlex import quote

bp = Blueprint('smart', __name__, url_prefix='/smart')

"""
@bp.route('/')
def index():
    """
    

@bp.before_request
def check_hd_path():
    msg = {}
    for device in current_app.config['HD_DEVICES']:
        if not os.path.exists('/dev/' + device):
            msg[device] = 'not found'
    return jsonify(msg)


@bp.route('/<device_name>')
def get_hd_info(device_name):
    # get hardisk information to html
    with os.popen(f'/sbin/smartctl --all {quote(device_name)}') as f:
        return f'<pre>{f.read()}</pre>'

@bp.route("/ps")
def get_hdd_ps():

        # 硬盘状态列表
        ps = {}

        # uptime
        uptime: str = os.popen('uptime').read().strip()
        ps['uptime'] = uptime

        for device in current_app.config['HD_DEVICES']:
                cmd = f'/sbin/smartctl -i -n standby /dev/sd{device}'
                pow_sts = os.popen(cmd).readlines()[-1].strip()
                if 'STANDBY' in pow_sts:
                        ps[f'sd{device}']= 'STANDBY'
                else:
                        ps[f'sd{device}']= 'ACTIVE'

        return jsonify(ps)
