from flask import Blueprint

import os

bp = Blueprint('ups', __name__, url_prefix='/ups/')

@bp.route('/')
def get_ups_status():
    # get ups status to json
    cmd = '/sbin/apcaccess'
    if os.path.exists(cmd):
        with os.popen(cmd) as f:
            for i in f.readlines():
                if 'STATUS' in i:
                    return {'STATUS': i.split(":")[-1].strip()}
            return {'STATUS': f'{f.read()}'}
    else:
        return {'msg': f'{cmd}: command not found'}
    
