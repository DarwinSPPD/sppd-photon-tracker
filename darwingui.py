import tkinter
import interpretsppdpipe
import tkinter.font

guifilepath = [r'C:\pathtooutput\sppd.darwingui']


tk_top = tkinter.Tk()
tk_left = tkinter.Label(tk_top, anchor='nw', justify='left', relief="groove", \
			text = 'Sent meta data goes here...\n\nExample')
tk_right = tkinter.Label(tk_top, anchor='nw', justify='left', relief="groove", \
			text = 'Received meta data goes here...\n\nExample')
tk_leftbottom = tkinter.Label(tk_top, anchor='nw', justify='left', relief="groove", \
			text = 'Sent position data goes here...\n\nExample')
tk_rightbottom = tkinter.Label(tk_top, anchor='nw', justify='left', relief="groove", \
			text = 'Received position data goes here...\n\nExample')

tk_left.place(x=0, y=0, height=300, width=300)
tk_right.place(x=300, y=0, height=300, width=300)
tk_leftbottom.place(x=0, y=300, height=400, width=300)
tk_rightbottom.place(x=300, y=300, height=400, width=300)
tk_top.geometry("610x710")

filepositionhint = [0]
tk_charactertranslationlist = [\
	('\\x', '\n\\x'), \
	(', ', ', \n'), \
	(',', ',\n'), \
	('-', '-\n'), \
	('', '\n')]
def tk_insertnewlinesforlabeltext(param):
	(tk_text, tk_font, tk_widthinpixels) = param

	textsplit = tk_text.split('\n')
	i = 0
	while i < len(textsplit):
		j = 0
		while j < len(tk_charactertranslationlist) and \
		      len(textsplit[i]) > 1 and \
		      tkinter.font.nametofont(tk_font).measure(textsplit[i]) > tk_widthinpixels:
			bestreplacement = None
			k = 0
			textline = textsplit[i]
			while True:
				ktemp = textline.find(tk_charactertranslationlist[j][0], k)
				if ktemp >= 0:
					bestreplacementtemp = (textline[:ktemp] + \
							      tk_charactertranslationlist[j][1] + \
							      textline[ktemp+len(tk_charactertranslationlist[j][0]):]).split('\n')
					if tkinter.font.nametofont(tk_font).measure(bestreplacementtemp[0]) <= tk_widthinpixels:
						l = 0
						l_flag_set = False
						while l < len(bestreplacementtemp):
							if not bestreplacementtemp[l]:
								l_flag_set = True
								break
							l += 1
						if not l_flag_set:
							bestreplacement = bestreplacementtemp
					else:
						break
				else:
					break
				k = ktemp + 1
			#break goes here
			if bestreplacement != None:
				textsplit[i] = bestreplacement[0]
				m = 1
				while m < len(bestreplacement):
					textsplit.insert(i+m, bestreplacement[m])
					m += 1
				break
			j += 1
		#break goes here
		i += 1
	tk_text = '\n'.join(textsplit)

	return (tk_text, tk_font, tk_widthinpixels)

def tk_after():
##	print('tk_after() called')
	with open(guifilepath[0], 'rb') as f:
		t = f.seek(filepositionhint[0])
		b = b''
		while True:
			btemp = f.read(5)
			if len(btemp) == 5:
				assert btemp[0:1] == b'\xfb'
			else:
				break
			btemp += f.read(int.from_bytes(btemp[1:5], 'big') - 5)
			if len(btemp) == int.from_bytes(btemp[1:5], 'big'):
				b = btemp
				filepositionhint[0] = f.tell()
			else:
				break
##		print('tk_after(): b = ' + repr(b))
		if b != b'':
			assert len(b) > 5
			(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = \
			     interpretsppdpipe.processelement((1, False, b, 5, 0, b'', 0, 0, {}, b'', False, b''))
			if w != b'':
				print('GUI: decoding failed, stopping user interface updates!', flush = True)
				print('GUI: ' + w.decode(), flush = True)
				return
			sentmeta = elem[1][0][(b's', b'sppd')][1][0][(b's', b'sentmeta')][1].decode()
			receivedmeta = elem[1][0][(b's', b'sppd')][1][1][(b's', b'receivedmeta')][1].decode()
			sentposition = elem[1][0][(b's', b'sppd')][1][2][(b's', b'sentposition')][1].decode()
			receivedposition = elem[1][0][(b's', b'sppd')][1][3][(b's', b'receivedposition')][1].decode()
			
			(sentmeta, tk_font, tk_widthinpixels) = tk_insertnewlinesforlabeltext((sentmeta, tk_left['font'], 295))
			(receivedmeta, tk_font, tk_widthinpixels) = tk_insertnewlinesforlabeltext((receivedmeta, tk_right['font'], 295))
			(sentposition, tk_font, tk_widthinpixels) = tk_insertnewlinesforlabeltext((sentposition, tk_leftbottom['font'], 295))
			(receivedposition, tk_font, tk_widthinpixels) = tk_insertnewlinesforlabeltext((receivedposition, tk_rightbottom['font'], 295))
			
			tk_left.config(text=sentmeta)
			tk_right.config(text=receivedmeta)
			tk_leftbottom.config(text=sentposition)
			tk_rightbottom.config(text=receivedposition)
			
			
			
			
			
	tk_top.after(50, tk_after)

tk_top.after(50, tk_after)
tk_top.mainloop()
