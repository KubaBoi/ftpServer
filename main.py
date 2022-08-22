#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
server = servers.FTPServer(address, FTPHandler)
server.serve_forever()