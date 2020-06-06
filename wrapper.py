
print('WRAPPER: testing dependencies...', flush = True)

testfailed = False

DEF_universal_newlines_True = [False]

try:
	print('\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\n' + \
	      'sppd-photon-tracker: gives you data when game treats you rough\n' + \
	      '\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\u0660\u4e36\n', \
	      flush = True)
	print('WRAPPER: unicode characters: SUPPORTED', flush = True)
except UnicodeEncodeError as tmpe:
	print('WRAPPER: unicode characters: MISSING', flush = True)
	DEF_universal_newlines_True[0] = True
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
try:
	import win32file
	print('WRAPPER: import win32file: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import win32file: FAILURE', flush = True)
try:
	import struct
	print('WRAPPER: import struct: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import struct: FAILURE', flush = True)
try:
	import win32con
	print('WRAPPER: import win32con: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import win32con: FAILURE', flush = True)
try:
	import winioctlcon
	print('WRAPPER: import winioctlcon: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import winioctlcon: FAILURE', flush = True)
try:
	import socket
	print('WRAPPER: import socket: SUCCESS', flush = True)
except ModuleNotFoundError as tmpe:
	testfailed = True
	print('WRAPPER: import socket: FAILURE', flush = True)




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

sshdump_path = [r'C:\Program Files\Wireshark\extcap\sshdump.exe']
sshdumplinked = [False]
signal.signal(signal.SIGINT, signal.default_int_handler)


hJob = win32job.CreateJobObject(None, "")
extended_info = win32job.QueryInformationJobObject(hJob, win32job.JobObjectExtendedLimitInformation)
extended_info['BasicLimitInformation']['LimitFlags'] = win32job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
win32job.SetInformationJobObject(hJob, win32job.JobObjectExtendedLimitInformation, extended_info)

perms = win32con.PROCESS_TERMINATE | win32con.PROCESS_SET_QUOTA

pid = 0
pythonexepath = psutil.Process().cmdline()[0]
while True:
	print('WRAPPER: running process...', flush = True)
	sppd_cmd=[pythonexepath, r'runtsharksppdpipe.py', r'sshdumpprocesspid='+str(pid) ]
##	print('sys.stdout = ' + repr(sys.stdout), flush = True)

	# allows python child process to print unicode characters to console without UnicodeEncodeError exception

	my_env = os.environ
	my_env['PYTHONIOENCODING'] = 'utf-8'
	# TODO: find more portable solution without setting enviroment variable.
	# Entering command in cmd.exe shell + Enter button does allow to print unicode characters
	# PYTHONIOENCODING enviroment variable is supposed to work only with python children processes
	
	if DEF_universal_newlines_True[0]:
		proc=subprocess.Popen(sppd_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags = subprocess.CREATE_NO_WINDOW, env = my_env, universal_newlines=True)
	else:
		proc=subprocess.Popen(sppd_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags = subprocess.CREATE_NO_WINDOW, env = my_env)
	real_sppd_cmd = psutil.Process(proc.pid).cmdline()
	runner_hProcess = win32api.OpenProcess(perms, False, proc.pid)
	win32job.AssignProcessToJobObject(hJob, runner_hProcess)

	print("--- runtsharksppdpipe.py configured to terminate if wrapper.py dies ---", flush=True)
	
##	print('proc.stdout.fileno() = ' + repr(proc.stdout.fileno()), flush = True)
	tmpe = None
	try:
		if DEF_universal_newlines_True[0]:
			while proc.poll() is None:
				line = proc.stdout.readline()
				if line:
					print(line, flush = True, end='')
		else:
			while proc.poll() is None:
				bytes_variable = os.read(proc.stdout.fileno(), 2 << 16)
				if bytes_variable:
					sys.stdout.buffer.write(bytes_variable)
					sys.stdout.flush()

				
		returnvalue = proc.poll()
		if returnvalue > (2 << 30):
			returnvalue -= (2 << 31)
		pid = (-1) * returnvalue
		if pid <= 0:
			print('WRAPPER: process returned ' + str((-1) * pid) + ', exiting...', flush = True)
			break
		else:
			print('WRAPPER: process returned ' + str((-1) * pid) + ', sleeping 20 seconds before restarting...', flush = True)
			if not sshdumplinked[0] and psutil.Process(pid).cmdline()[0] == sshdump_path:
				ssh_hProcess = win32api.OpenProcess(perms, False, pid)

				win32job.AssignProcessToJobObject(hJob, gui_hProcess)

				print("--- sshdump configured to terminate if wrapper.py dies ---", flush=True)

				sshdumplinked[0] = True
			time.sleep(20)
		continue
	except KeyboardInterrupt as tmpe:
		pass
	except psutil.NoSuchProcess as tmpe:
		pass
	
##		print('WRAPPER: sending interrupt to process...', flush = True)
##		signal_cmd=[pythonexepath, r'-c', \
##			    r'import ctypes; ' + \
##			    r'import psutil; ' + \
##			    r'kernel = ctypes.windll.kernel32; ' + \
##			    r'kernel.FreeConsole(); ' + \
##			    r'kernel.AttachConsole(' + str(proc.pid) + r'); ' + \
##			    r'assert psutil.Process(' + str(proc.pid) + r').cmdline() == ' + str(real_sppd_cmd) + r'; ' + \
##			    r'kernel.SetConsoleCtrlHandler(None, 1); ' + \
##			    r'kernel.GenerateConsoleCtrlEvent(0, 0); ' + \
##			    r'']
##		signalproc=subprocess.Popen(signal_cmd, creationflags = subprocess.CREATE_NO_WINDOW)
	if DEF_universal_newlines_True[0]:
		while proc.poll() is None:
			line = proc.stdout.readline()
			if line:
				print(line, flush = True, end='')
	else:
		while proc.poll() is None:
			bytes_variable = os.read(proc.stdout.fileno(), 2 << 16)
			if bytes_variable:
				sys.stdout.buffer.write(bytes_variable)
				sys.stdout.flush()

			
	print('WRAPPER: reading remaining process output...', flush = True)
	tmptuple = proc.communicate()
	print('WRAPPER: process stdout below...', flush = True)
	if DEF_universal_newlines_True[0]:
		print(tmptuple[0], flush = True)
	elif tmptuple[0]:
		sys.stdout.buffer.write(tmptuple[0])
	print('WRAPPER: process stderr below...', flush = True)
	if DEF_universal_newlines_True[0]:
		print(tmptuple[1], flush = True)
	elif tmptuple[1]:
		sys.stdout.buffer.write(tmptuple[1])
	print('WRAPPER: process returned ' + str(proc.poll()) + ', exiting...', flush = True)
	raise Exception from tmpe
	break

