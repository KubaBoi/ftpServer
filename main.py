#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def runFileServer():
    authorizer = DummyAuthorizer()

    authorizer.add_user('kuba', 'heslo', os.getcwd(), perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.masquerade_address = '130.61.38.75'
    handler.passive_ports = range(60000, 60099)
    handler.banner = "pyftpdlib based ftpd ready."

    address = ('', 21)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == "__main__":
    runFileServer()