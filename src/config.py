# -*- coding: utf8 -*-

import os

GLOBAL={

    "Host": os.getenv("BlueSky_host", "0.0.0.0"),
    #Application run network address, you can set it `0.0.0.0`, `127.0.0.1`, ``.

    "Port": os.getenv("BlueSky_port", 10200),
    #Application run port, default port.

    "LogLevel": os.getenv("BlueSky_loglevel", "DEBUG"),
    #Application to write the log level, currently has DEBUG, INFO, WARNING, ERROR, CRITICAL.
}


PRODUCT={

    "ProcessName": "BlueSky",
    #Custom process, you can see it with "ps aux|grep ProcessName".

    "ProductType": os.getenv("BlueSky_producttype", "tornado"),
    #Production environment starting method, optional `gevent`, `tornado`.
}


SSO={

    "SSO.URL": os.getenv("BlueSky_ssourl", "https://passport.saintic.com"),
    #The passport(SSO Authentication System) Web Site URL.

    "SSO.PROJECT": PRODUCT["ProcessName"],
    #SSO request application.
}

REDIS=os.getenv("BlueSky_REDIS", "redis://ip:port:password")
