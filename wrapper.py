
print('WRAPPER: testing dependencies...', flush = True)

testfailed = False

try:
	import subprocess
	print('WRAPPER: import subprocess: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import subprocess: FAILURE', flush = True)
try:
	import sys
	print('WRAPPER: import sys: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import sys: FAILURE', flush = True)
try:
	import signal
	print('WRAPPER: import signal: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import signal: FAILURE', flush = True)
try:
	import time
	print('WRAPPER: import time: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import time: FAILURE', flush = True)
try:
	import psutil
	print('WRAPPER: import psutil: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import psutil: FAILURE', flush = True)
try:
	import ctypes
	print('WRAPPER: import ctypes: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import ctypes: FAILURE', flush = True)
try:
	import win32pipe
	print('WRAPPER: import win32pipe: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import win32pipe: FAILURE', flush = True)
try:
	import win32file
	print('WRAPPER: import win32file: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import win32file: FAILURE', flush = True)
try:
	import threading
	print('WRAPPER: import threading: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import threading: FAILURE', flush = True)
try:
	import json
	print('WRAPPER: import json: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import json: FAILURE', flush = True)
try:
	import math
	print('WRAPPER: import math: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import math: FAILURE', flush = True)
try:
	import os
	print('WRAPPER: import os: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import os: FAILURE', flush = True)
try:
	import win32api
	print('WRAPPER: import win32api: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import win32api: FAILURE', flush = True)
try:
	import win32con
	print('WRAPPER: import win32con: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import win32con: FAILURE', flush = True)
try:
	import win32job
	print('WRAPPER: import win32job: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import win32job: FAILURE', flush = True)
try:
	import pywintypes
	print('WRAPPER: import pywintypes: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import pywintypes: FAILURE', flush = True)
try:
	import netifaces
	print('WRAPPER: import netifaces: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import netifaces: FAILURE', flush = True)
if sys.version_info.major > 3 or (sys.version_info.major == 3 and sys.version_info.minor >= 7):
	print("WRAPPER: python version is at least 3.7: SUCCESS", flush = True)
else:
	testfailed = True
	print("WRAPPER: python version is at least 3.7: FAILURE", flush = True)
if os.path.isdir(r'C:\pathtooutput'):
	print("WRAPPER: os.path.isdir(r'C:\\pathtooutput'): SUCCESS", flush = True)
else:
	testfailed = True
	print("WRAPPER: os.path.isdir(r'C:\\pathtooutput'): FAILURE", flush = True)
if os.path.isfile(r'C:\pathtooutput\ssh_key.pem'):
	print("WRAPPER: os.path.isfile(r'C:\\pathtooutput\\ssh_key.pem'): SUCCESS", flush = True)
else:
	testfailed = True
	print("WRAPPER: os.path.isfile(r'C:\\pathtooutput\\ssh_key.pem'): FAILURE", flush = True)
if os.path.isdir(r'C:\Program Files\Wireshark'):
	print("WRAPPER: os.path.isdir(r'C:\\Program Files\\Wireshark'): SUCCESS", flush = True)
else:
	testfailed = True
	print("WRAPPER: os.path.isdir(r'C:\\Program Files\\Wireshark'): FAILURE", flush = True)
if os.path.isfile(r'C:\Program Files\Wireshark\extcap\sshdump.exe'):
	print("WRAPPER: os.path.isfile(r'C:\\Program Files\\Wireshark\\extcap\\sshdump.exe'): SUCCESS", flush = True)
else:
	testfailed = True
	print("WRAPPER: os.path.isfile(r'C:\\Program Files\\Wireshark\\extcap\\sshdump.exe'): FAILURE", flush = True)
if os.path.isfile(r'C:\Program Files\Wireshark\tshark.exe'):
	print("WRAPPER: os.path.isfile(r'C:\\Program Files\\Wireshark\\tshark.exe'): SUCCESS", flush = True)
else:
	testfailed = True
	print("WRAPPER: os.path.isfile(r'C:\\Program Files\\Wireshark\\tshark.exe'): FAILURE", flush = True)
if testfailed:
	sys.exit()


signal.signal(signal.SIGINT, signal.default_int_handler)

pid = 0
pythonexepath = psutil.Process().cmdline()[0]
while True:
	print('WRAPPER: running process...', flush = True)
	sppd_cmd=[pythonexepath, r'runtsharksppdpipe.py', r'sshdumpprocesspid='+str(pid) ]
	proc=subprocess.Popen(sppd_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags = subprocess.CREATE_NO_WINDOW, universal_newlines=True)
	real_sppd_cmd = psutil.Process(proc.pid).cmdline()
	try:
		while proc.poll() is None:
			line = proc.stdout.readline()
			if line:
				print(line, flush = True, end='')
		returnvalue = proc.poll()
		if returnvalue > (2 << 30):
			returnvalue -= (2 << 31)
		pid = (-1) * returnvalue
		if pid <= 0:
			print('WRAPPER: process returned ' + str((-1) * pid) + ', exiting...', flush = True)
			break
		else:
			print('WRAPPER: process returned ' + str((-1) * pid) + ', sleeping 60 seconds before restarting...', flush = True)
			time.sleep(60)
	except KeyboardInterrupt as tmpe:
		print('WRAPPER: sending interrupt to process...', flush = True)
		signal_cmd=[pythonexepath, r'-c', \
			    r'import ctypes; ' + \
			    r'import psutil; ' + \
			    r'kernel = ctypes.windll.kernel32; ' + \
			    r'kernel.FreeConsole(); ' + \
			    r'kernel.AttachConsole(' + str(proc.pid) + r'); ' + \
			    r'assert psutil.Process(' + str(proc.pid) + r').cmdline() == ' + str(real_sppd_cmd) + r'; ' + \
			    r'kernel.SetConsoleCtrlHandler(None, 1); ' + \
			    r'kernel.GenerateConsoleCtrlEvent(0, 0); ' + \
			    r'']
		signalproc=subprocess.Popen(signal_cmd, creationflags = subprocess.CREATE_NO_WINDOW)
		while proc.poll() is None:
			line = proc.stdout.readline()
			if line:
				print(line, flush = True, end='')
		print('WRAPPER: reading remaining process output...', flush = True)
		tmptuple = proc.communicate()
		print('WRAPPER: process stdout below...', flush = True)
		print(tmptuple[0], flush = True)
		print('WRAPPER: process stderr below...', flush = True)
		print(tmptuple[1], flush = True)
		print('WRAPPER: process returned ' + str(proc.poll()) + ', exiting...', flush = True)
		raise KeyboardInterrupt from tmpe
