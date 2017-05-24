#!/usr/bin/python

import os
import socket
import json

def mk_packet(src, intm, dest, payload):
	packet = {}
	packet["src"] = src
	packet["int"] = intm
	packet["dest"] = dest
	packet["payload"] = payload
	return json.dumps(packet)

def send_packet(packet)
	client = socket.socket()
	c.connect((packet["dest"], port))
	c.send(mk_packet(packet))


def ping(host):
	status = os.system("ping -c3 -t1 " + host)
	return status == 0







