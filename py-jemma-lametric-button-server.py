#!/usr/bin/python

import ConfigParser
import SimpleHTTPServer
import SocketServer
import LametricHandler

# parsing properties

config = ConfigParser.RawConfigParser()
config.read('py-jemma-lametric-button-server.properties')
server_port = int(config.get('General', 'server_port'));

# Starting server

print "Starting py-jemma-lametric-button-server on port " + str(server_port)
httpd = SocketServer.TCPServer(("", server_port), LametricHandler)
httpd.serve_forever()
