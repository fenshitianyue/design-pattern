#!/usr/bin/python2
# -*- coding:UTF-8 -*-
"""
这是一段web应用的授权模板代码

"""

from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenthcate()
        return f(*args, **kwargs)
    return decorated

