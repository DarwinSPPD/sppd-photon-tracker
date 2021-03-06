# sppd-photon-tracker

Real time tracker for South Park: Phone Destroyer player versus player mode.

---

Usage commands (use one from the following): 
=============
* Full support with dependency test
```
python.exe wrapper.py
```
* Fallback option if wrapper.py fails
```
python.exe runtsharksppdpipe.py
```
* GUI test
```
python.exe darwingui.py
```

---

Debug API: 
=============
* Execute photon command in python shell (will print decoded output)
```
import interpretsppdpipe
interpretsppdpipe.debug_execute_photon_packet(b'\xfb\x00\x00\x00\x1f\x00\x01\xf3\x03\xe1\x7f\xf8s\x00\x0eNo match found\x00\x00')
```

---

How to stop tracker:
=============
* CTRL + C keystroke at console window

---

Requirements:
=============
* Python version 3.7 or newer
* Remote capture SSH server installed at gateway IP address, port 15432 (PCAP Remote Android app or equivalent)
* Directory C:\pathtooutput
* SSH server key installed at path C:\pathtooutput\ssh_key.pem
* Full Wireshark installation (protocol TSDNS Teamspeak3 should be disabled, it corrupts TCP streams containing photon stream)
* Python libraries:

	* subprocess
	* sys
	* signal
	* time
	* psutil
	* ctypes
	* win32pipe
	* win32file
	* threading
	* json
	* math
	* os
	* win32api
	* win32con
	* win32job
	* pywintypes
	* netifaces
	* win32file
	* struct
	* win32con
	* winioctlcon
	* socket
