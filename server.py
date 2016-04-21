#!C:/Python27/python.exe
# -*-coding:utf-8 -*-
# Script python standard qui permet de démarrer un serveur sur le port 8888

import BaseHTTPServer
import CGIHTTPServer

PORT = 8888
server_address = ("", PORT)

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print "Serveur actif sur le port :", PORT

httpd = server(server_address, handler)
httpd.serve_forever()