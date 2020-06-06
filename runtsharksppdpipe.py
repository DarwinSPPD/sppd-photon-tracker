import win32pipe
import win32file
import subprocess
import threading
##import http
##import http.client
import time
import interpretsppdpipe
import sys
import os
import win32api
import win32con
import win32job
import pywintypes
import netifaces
import signal
import psutil
import win32file
import struct
import win32con
import winioctlcon
import socket

maincommandline = [psutil.Process().cmdline()]
print("python command received: "+str(maincommandline[0]), flush=True)
assert maincommandline[0][1] == 'runtsharksppdpipe.py'
argi = 2
processpid = 0
while argi < len(maincommandline[0]):
	argitem = maincommandline[0][argi]
	if argitem.startswith('sshdumpprocesspid='):
		processpid = int(argitem[len('sshdumpprocesspid='):])
	argi += 1
	

class CustomException(Exception):
	pass
##print('sys.getdefaultencoding() = ' + repr(sys.getdefaultencoding()), flush = True)
print("--- Starting SPPD monitoring engine ---", flush=True)

gateways = netifaces.gateways()
defaultgateway = gateways['default'][netifaces.AF_INET][0]

hJob = win32job.CreateJobObject(None, "")
extended_info = win32job.QueryInformationJobObject(hJob, win32job.JobObjectExtendedLimitInformation)
extended_info['BasicLimitInformation']['LimitFlags'] = win32job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
win32job.SetInformationJobObject(hJob, win32job.JobObjectExtendedLimitInformation, extended_info)


guifilepath = [r'C:\pathtooutput\sppd.darwingui']

print("--- Clearing "+repr(guifilepath[0])+" ---", flush=True)
with open(guifilepath[0], 'wb', buffering=0) as temp_f:
	pass
assert os.path.getsize(guifilepath[0]) == 0

print("--- Enabling NTFS compression for "+repr(guifilepath[0])+" ---", flush=True)

guifile_handle = win32file.CreateFile(guifilepath[0], \
				      win32file.GENERIC_READ | win32file.GENERIC_WRITE, \
				      0, None, win32file.OPEN_EXISTING, 0, None)
guifile_buffer = struct.pack('H', win32con.COMPRESSION_FORMAT_DEFAULT)
win32file.DeviceIoControl(Device = guifile_handle, IoControlCode = winioctlcon.FSCTL_SET_COMPRESSION, \
			  InBuffer = guifile_buffer, OutBuffer = None)
win32file.CloseHandle(guifile_handle)

print("--- Launching GUI ---", flush=True)
pythonexepath = psutil.Process().cmdline()[0]
sppdgui_cmd=[pythonexepath, r'darwingui.py']
gui_proc=subprocess.Popen(sppdgui_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags = subprocess.CREATE_NO_WINDOW, universal_newlines=True)

perms = win32con.PROCESS_TERMINATE | win32con.PROCESS_SET_QUOTA
gui_hProcess = win32api.OpenProcess(perms, False, gui_proc.pid)

win32job.AssignProcessToJobObject(hJob, gui_hProcess)

print("--- darwingui.py configured to terminate if runtsharksppdpipe.py dies ---", flush=True)


def guiprocessoutputredirect(proc):
	while proc.poll() is None:
			line = proc.stdout.readline()
			if line:
				print(line, flush = True, end='')
	tmptuple = proc.communicate()
	print('darwingui.py process stdout below...', flush = True)
	print(tmptuple[0], flush = True)
	print('darwingui.py process stderr below...', flush = True)
	print(tmptuple[1], flush = True)
	print("--- darwingui.py died with a return code "+str(proc.poll())+" ---", flush=True)

gui_th = threading.Thread(target=guiprocessoutputredirect, args=(gui_proc, ))
gui_th.daemon = True
gui_th.start()


sshpcappath = r'C:\pathtooutput\ssh.pcap'



sshdump_cmd = [r'C:\Program Files\Wireshark\extcap\sshdump.exe', r'--extcap-interface', r'sshdump', \
	       r'--fifo', sshpcappath, r'--capture', r'--remote-host', \
	       defaultgateway, r'--remote-port', r'15432', r'--sshkey', \
	       r'C:\pathtooutput\ssh_key.pem']


start_time = [time.time()]



def exceptionthrowthread(param1):
	raise Exception from param1

sshdumpendpointisunusable = False

while True:
	if processpid > 0:
		print("--- Checking sshdumpprocesspid parameter... ---", flush=True)
		try:
			if (sshdump_cmd == psutil.Process(processpid).cmdline()):
				break
			else:
				print("sshdumpprocesspid parameter links to process with different command line parameters!", flush=True)
				print("sshdump command received: "+str(psutil.Process(processpid).cmdline()), flush=True)
				print("sshdump command expected: "+str(sshdump_cmd), flush=True)
		except psutil.NoSuchProcess as tmpe:
			print("sshdumpprocesspid parameter links to nonexistent process!", flush=True)
		raise ValueError("invalid parameter: sshdumpprocesspid")
	assert processpid == 0
		
	
	print("--- Deleting "+repr(sshpcappath)+" ---", flush=True)

	if os.path.exists(sshpcappath):
		os.remove(sshpcappath)

	print("--- Checking sshdump endpoint... ---", flush=True)
	
	sshdumpendpointisunusable = False
	sshdumps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sshdumps.settimeout(0.0)
	sshdumps_counter_0 = 0
	while True:
		sshdumps_counter_0 += 1
		sshdumps_ret = sshdumps.connect_ex((defaultgateway, 15432))
		print("--- ("+str(sshdumps_counter_0)+")connect_ex() == "+str(sshdumps_ret)+" ---", flush=True)
		assert (sshdumps_ret == 0 or sshdumps_ret == 10035 or sshdumps_ret == 10056 or sshdumps_ret == 10022)
		if sshdumps_ret == 10035:
			time.sleep(1)
			continue
		tmpe2 = None
		if sshdumps_ret == 0 or sshdumps_ret == 10056:
			sshdumpendpointready = False
			sshdumps_counter = 0
			while True:
				time.sleep(1)
				try:
					sshdumps_data = sshdumps.recv(1024)
					print("--- recv() == "+str(sshdumps_data)+" ---", flush=True)
					assert sshdumps_data == b'SSH-2.0-libssh_0.8.90\r\n'
					sshdumpendpointready = True
					break
				except BlockingIOError as tmpe:
					sshdumps_counter += 1
					tmpe2 = tmpe
					print("--- ("+str(sshdumps_counter)+")sshdump endpoint "+ defaultgateway + ":"+str(15432)+" is not responding, retrying to receive data... ---", flush=True)
##					thtemp = threading.Thread(target=exceptionthrowthread, args=(tmpe2, ))
##					thtemp.daemon = True
##					thtemp.start()
					if sshdumps_counter >= 60:
						break
					continue
	##				pass
			if sshdumpendpointready:
				break
		sshdumpendpointisunusable = True
##		print("--- connect_ex() == "+str(sshdumps_ret)+" ---", flush=True)
		print("--- sshdump endpoint "+ defaultgateway + ":"+str(15432)+" is not responding, unreachable or already in use ---", flush=True)
		if tmpe2 != None:
			thtemp = threading.Thread(target=exceptionthrowthread, args=(tmpe2, ))
			thtemp.daemon = True
			thtemp.start()
		break

	sshdumps.close()
	if sshdumpendpointisunusable:
		break
##	assert (sshdumpendpointisunusable == False)		
	
	print("--- Launching sshdump ---", flush=True)

	sshdumpproc=subprocess.Popen(sshdump_cmd, cwd=r'C:\Program Files\Wireshark', creationflags = subprocess.CREATE_NO_WINDOW)

	# Convert process id to process handle:

	##hProcess = win32api.OpenProcess(perms, False, sshdumpproc.pid)
	##
	##win32job.AssignProcessToJobObject(hJob, hProcess)

	#print("--- sshdump configured to terminate if python dies ---")

	processpid = sshdumpproc.pid
	sshdumproccommandline = [psutil.Process(processpid).cmdline()]
	print("sshdump command received: "+str(sshdumproccommandline[0]), flush=True)
	print("sshdump command sent: "+str(sshdump_cmd), flush=True)
	assert sshdumproccommandline[0] == sshdump_cmd

	break

#runtsharksppdpipe



startsshdumpwatchdogthread = [False]
##sshdumpreturnvalue = [None]
threadkillswitch = [[None]]
sshdumpdied = [False]

def pushsshpcaptotshark (pipe, param, killswitch):
	(path,) = param
	with open(r'C:\pathtooutput\sppdtransmitlog2.txt', 'w', buffering=1) as f:
		copied = 0
		total = 24
		start_time[0] = time.time()
		while True:
			exceptionrethrow = None
			try:
				sshcapmessagecounter = 0
				while sshcapmessagecounter < 60:
					sshcapmessagecounter += 1
##					if sshdumpreturnvalue[0] != None:
##						print ('sshdump died', flush=True)
##						raise CustomException
					if killswitch[0]:
						print ('pushsshpcaptotshark requested to terminate', flush=True)
						raise CustomException
					if not os.path.exists(path) or os.stat(path).st_size == 0:
						print("("+str(sshcapmessagecounter)+")waiting for sshdump output...", flush=True)
						time.sleep(1)
						continue
					else:
						print("("+str(sshcapmessagecounter)+")sshdump output found", flush=True)
						startsshdumpwatchdogthread[0] = True
						break
				if not os.path.exists(path) or os.stat(path).st_size == 0:
					sshdumpdied[0] = True
					break
				while True:
					if killswitch[0]:
						print ('pushsshpcaptotshark requested to terminate', flush=True)
						raise CustomException
					if copied < total:
						start_time[0] = time.time()
						totaltemp = os.path.getsize(path)
						if totaltemp < total:
							print ('sshdump failed to produce output!', flush=True)
							raise CustomException
						pcapf = open(path, 'rb', buffering=0)
						pcapf.seek(copied, 0)
						data = pcapf.read(total-copied)
						pcapf.close()
						assert len(data) == (total-copied)
						f.write ('file range ' + str(total) + '-' + str(copied) + ' responded with ' + \
						       str(len(data)) + ' bytes\n' )
						copied = total
						if (total + (1 << 16)) >= totaltemp:
							total = totaltemp
						else:
							total += (1 << 16)
						win32file.WriteFile(pipe, data)
					else:
						total = os.path.getsize(path)
						if (time.time() - start_time[0]) < 0.1:
							time.sleep(0.1)
						start_time[0] = time.time()
			except ConnectionRefusedError as e:
				exceptionrethrow = e
			except TimeoutError as e:
				exceptionrethrow = e
			except ConnectionResetError as e:
				exceptionrethrow = e
			except OSError as e:
				exceptionrethrow = e
			except AssertionError as e:
				exceptionrethrow = e
			except pywintypes.error as e:
				#TODO: figure out why tshark randomly crashes. Sending same data after restarting tshark will not crash it
				#unless size is in tens of megabytes
				print("tshark pipe crashed while receiving data up to position "+ str(copied), flush=True)
				exceptionrethrow = e
			except CustomException:
				pass
			if exceptionrethrow != None:
				thtemp = threading.Thread(target=exceptionthrowthread, \
							  args=(exceptionrethrow, ))
				thtemp.daemon = True
				thtemp.start()
			break
		#print ('pushsshpcaptotshark: Link to file died, killing connection to tshark...')
		threadkillswitch[0][0] = True
		#win32pipe.DisconnectNamedPipe(pipe)


##def sshdumpwatchdog (processhandle, tsharkproc, killswitch):
def sshdumpwatchdog (processpid, tsharkproc, killswitch):
	try:
		time.sleep(10)
		while not startsshdumpwatchdogthread[0]:
			if killswitch[0]:
				raise CustomException
			time.sleep(10)
		try:
			while psutil.Process(processpid).cmdline() == sshdump_cmd:
				if killswitch[0]:
					raise CustomException

				sshdumps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sshdumps.settimeout(0.0)
				sshdumpendpointisunusable = False
				while True:
					sshdumps_ret = sshdumps.connect_ex((defaultgateway, 15432))
					assert (sshdumps_ret == 0 or sshdumps_ret == 10035 or sshdumps_ret == 10056 or sshdumps_ret == 10022)
					if sshdumps_ret == 10035:
						time.sleep(1)
						continue
					tmpe = None
					if sshdumps_ret == 0 or sshdumps_ret == 10056:
						time.sleep(1)
						try:
							sshdumps_data = sshdumps.recv(1024)
							print("--- sshdumpwatchdog: recv() == "+str(sshdumps_data)+" ---", flush=True)
		##					assert sshdumps_data == b'SSH-2.0-libssh_0.8.90\r\n'
		##					break
						except BlockingIOError as tmpe:
							pass
						break
					print("--- sshdumpwatchdog: unknown connect_ex() response "+str(sshdumps_ret)+" ---", flush=True)
					threadkillswitch[0][0] = True
##					sshdumpendpointisunusable = True
##			##		print("--- connect_ex() == "+str(sshdumps_ret)+" ---", flush=True)
##					print("--- sshdump endpoint "+ defaultgateway + ":"+str(15432)+" is not responding, unreachable or already in use ---", flush=True)
##					if tmpe != None:
##						thtemp = threading.Thread(target=exceptionthrowthread, args=(tmpe, ))
##						thtemp.daemon = True
##						thtemp.start()
					break
				sshdumps.close()
				time.sleep(10)
		except psutil.NoSuchProcess as tmpe:
			pass
##		while processhandle.poll() is None: 
##			if killswitch[0]:
##				raise CustomException
##			time.sleep(10)
##		sshdumpreturnvalue[0] = processhandle.poll()
		if startsshdumpwatchdogthread[0]:
			print ('sshdump died, killing tshark in 10 secs...', flush=True)
			sshdumpdied[0] = True
			#win32pipe.DisconnectNamedPipe(pipe)
			time.sleep(10)
			tsharkproc.kill()
	except CustomException:
		print ('sshdumpwatchdog requested to terminate', flush=True)
		print ('killing tshark in 10 secs...', flush=True)
##		if not (processhandle.poll() is None):
##			sshdumpdied[0] = True
		time.sleep(10)
		tsharkproc.kill()


signal.signal(signal.SIGINT, signal.default_int_handler)
tsharkstartcount = [0]
try:
	
	print("--- Creating pipe... ---", flush=True)
	pipe = win32pipe.CreateNamedPipe(
	    r'\\.\pipe\tshark_sppd2',
	    win32pipe.PIPE_ACCESS_OUTBOUND,
	    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
	    1, 1024*1024, 1024*1024,
	    0,
	    None)
	while (tsharkstartcount[0] < 10):
		if sshdumpdied[0] or sshdumpendpointisunusable:
			print ('can\'t start SPPD interpreter without a running instance of sshdump!', flush=True)
			break
		threadkillswitch[0] = [False]
		killswitchmain = threadkillswitch[0]
		assert threadkillswitch[0][0] != None
		assert killswitchmain[0] != None
		tsharkstartcount[0] = tsharkstartcount[0] + 1
		wireshark_cmd=[r'C:\Program Files\Wireshark\tshark.exe', r'-i', \
		       r'\\.\pipe\tshark_sppd2', r'-Y', r"data.len>0", r'-Tfields', \
		       r'-e', r'frame.time', r'-e', r'ip.src', r'-e', r'tcp.srcport', \
		       r'-e', r'ip.dst', r'-e', r'tcp.dstport', r'-e', r'data', r'-l']
		proc=subprocess.Popen(wireshark_cmd, stdout=subprocess.PIPE, creationflags = subprocess.CREATE_NO_WINDOW)


		# Convert process id to process handle:
		perms = win32con.PROCESS_TERMINATE | win32con.PROCESS_SET_QUOTA
		hProcess = win32api.OpenProcess(perms, False, proc.pid)

		win32job.AssignProcessToJobObject(hJob, hProcess)

		print("--- ("+str(tsharkstartcount[0])+")tshark configured to terminate if runtsharksppdpipe.py dies ---", flush=True)
		print("--- Connecting input pipe to tshark... ---", flush=True)
		win32pipe.ConnectNamedPipe(pipe, None)
		

		print("--- ("+str(tsharkstartcount[0])+")Connected in %s seconds ---" % (time.time() - start_time[0]), flush=True)

		exceptionrethrow = None

		startsshdumpwatchdogthread[0] = False
##		sshdumpreturnvalue[0] = None

		th = threading.Thread(target=pushsshpcaptotshark, args=(pipe, (sshpcappath, ), threadkillswitch[0]))
		th.daemon = True
		th.start()

		print("--- ("+str(tsharkstartcount[0])+")Launching sshdump process watchdog ---", flush=True)
		watchdogth = threading.Thread(target=sshdumpwatchdog, args=(processpid, proc, threadkillswitch[0]))
		watchdogth.daemon = True
		watchdogth.start()

		csvw = b''
		streamfilter = {}
		d = {}
		characterinstances = {}
		csvfile = None
		tsharkemptyresponsecounter = 0

		#main loop
		with open(r'C:\pathtooutput\tsharkout2.txt', 'wb', buffering=0) as output, \
			open(r'C:\pathtooutput\sppddecoderout2.txt', 'wb', buffering=0) as f2:
			while True:
				if killswitchmain[0]:
					print ('main loop requested to terminate', flush=True)
					break
				line = proc.stdout.readline()
				if not line:
					tsharkemptyresponsecounter += 1
					if tsharkemptyresponsecounter >= 10:
						print("("+str(tsharkemptyresponsecounter)+")tshark returned " + repr(line) + ", exiting...", flush=True)
						break
					else:
						print("("+str(tsharkemptyresponsecounter)+")tshark returned " + repr(line) + "...", flush=True)
						time.sleep(1)
						continue
				else:
					tsharkemptyresponsecounter = 0
				output.write(line)
				(csvw, streamfilter, d, characterinstances, csvfile) = \
					interpretsppdpipe.interpretsppd(line, f2, \
									(csvw, streamfilter, d, \
									characterinstances, \
									csvfile))
									
		threadkillswitch[0][0] = True
		#proc.kill()
		#print('main loop: killing the pipe...')
		#win32pipe.DisconnectNamedPipe(pipe)
		print ('sleeping 10 secs before trying to restart main loop...', flush=True)
		time.sleep(10)

except pywintypes.error as tmpe:
	print ('pipe died, preparing to restart the process. Printing exception...', flush=True)
	thtemp2 = threading.Thread(target=exceptionthrowthread, args=(tmpe, ))
	thtemp2.daemon = True
	thtemp2.start()
	print ('sleeping 10 secs before trying to restart...', flush=True)
	time.sleep(10)
	print ('setting exit code equal to sshdump\'s processpid ' +str(processpid)+' ...', flush=True)
	sys.exit((-1) * processpid)

except KeyboardInterrupt as tmpe:
	hProcess = win32api.OpenProcess(perms, False, sshdumpproc.pid)
	if sshdumproccommandline[0] == psutil.Process(processpid).cmdline():
		win32job.AssignProcessToJobObject(hJob, hProcess)
	raise KeyboardInterrupt from tmpe
	
#os.system('pause')






