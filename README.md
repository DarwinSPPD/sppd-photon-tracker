# sppd-photon-tracker

Real time tracker for South Park: Phone Destroyer player versus player mode.

---

Usage command (includes dependency test): 
=============
* python.exe wrapper.py

---

Requirements:
=============
* Remote capture SSH server installed at gateway IP address, port 15432 (PCAP Remote Android app or equivalent)
* SSH server key installed at path C:\pathtooutput\ssh_key.pem
* Full Wireshark installation
* Passes included dependency test, expected output below.

	* WRAPPER: import subprocess: SUCCESS
	* WRAPPER: import sys: SUCCESS
	* WRAPPER: import signal: SUCCESS
	* WRAPPER: import time: SUCCESS
	* WRAPPER: import psutil: SUCCESS
	* WRAPPER: import ctypes: SUCCESS
	* WRAPPER: import win32pipe: SUCCESS
	* WRAPPER: import win32file: SUCCESS
	* WRAPPER: import threading: SUCCESS
	* WRAPPER: import json: SUCCESS
	* WRAPPER: import math: SUCCESS
	* WRAPPER: import os: SUCCESS
	* WRAPPER: import win32api: SUCCESS
	* WRAPPER: import win32con: SUCCESS
	* WRAPPER: import win32job: SUCCESS
	* WRAPPER: import pywintypes: SUCCESS
	* WRAPPER: import netifaces: SUCCESS
	* WRAPPER: python version is at least 3.7: SUCCESS
	* WRAPPER: os.path.isdir(r'C:\pathtooutput'): SUCCESS
	* WRAPPER: os.path.isfile(r'C:\pathtooutput\ssh_key.pem'): SUCCESS
	* WRAPPER: os.path.isdir(r'C:\Program Files\Wireshark'): SUCCESS
	* WRAPPER: os.path.isfile(r'C:\Program Files\Wireshark\extcap\sshdump.exe'): SUCCESS
	* WRAPPER: os.path.isfile(r'C:\Program Files\Wireshark\tshark.exe'): SUCCESS
