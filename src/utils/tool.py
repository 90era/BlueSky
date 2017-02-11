# -*- coding: utf8 -*-

import re
import requests
import hashlib
import datetime
from uuid import uuid4
from base64 import b32encode
from .log import Syslog
from config import SSO, REDIS

ip_pat        = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
mail_pat      = re.compile(r"([0-9a-zA-Z\_*\.*\-*]+)@([a-zA-Z0-9\-*\_*\.*]+)\.([a-zA-Z]+$)")
Universal_pat = re.compile(r"[a-zA-Z\_][0-9a-zA-Z\_]*")
logger        = Syslog.getLogger()
md5           = lambda pwd:hashlib.md5(pwd).hexdigest()
gen_token     = lambda :b32encode(uuid4().hex)[:32]
gen_requestId = lambda :str(uuid4())
ParseRedis    = STORAGE["Connection"].split("redis://")[-1].split(":")
RedisConnection = Redis(host=ParseRedis[0], port=ParseRedis[1], password=ParseRedis[2] if len(ParseRedis) >= 3 else None, db=0, socket_timeout=5, socket_connect_timeout=5)


def ip_check(ip):
    if isinstance(ip, (str, unicode)):
        return ip_pat.match(ip)

def isLogged_in(cookie_str):
    ''' check username is logged in '''

    SSOURL = SSO.get("SSO.URL")
    if cookie_str and not cookie_str == '..':
        username, expires, sessionId = cookie_str.split('.')
        #success = Requests(SSOURL+"/sso/").post(data={"username": username, "time": expires, "sessionId": sessionId}).get("success", False)
        success = requests.post(SSOURL+"/sso/", data={"username": username, "time": expires, "sessionId": sessionId}, timeout=5, verify=False, headers={"User-Agent": "Template"}).json().get("success", False)
        logger.info("check login request, cookie_str: %s, success:%s" %(cookie_str, success))
        return success
    else:
        logger.info("Not Logged in")
        return False
