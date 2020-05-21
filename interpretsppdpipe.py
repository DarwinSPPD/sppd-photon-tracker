import json
import math
import time

# Public Photon API
photonparameters = {\
b'\xbf': b'RoomOptionFlags',\
b'\xc8': b'PluginVersion',\
b'\xc9': b'PluginName',\
b'\xcc': b'Plugins',\
b'\xd4': b'LobbyType',\
b'\xd5': b'LobbyName',\
b'\xdd': b'Secret',\
b'\xde': b'GameList',\
b'\xdf': b'Position',\
b'\xe3': b'MasterPeerCount',\
b'\xe4': b'GameCount',\
b'\xe5': b'PeerCount',\
b'\xe6': b'Address',\
b'\xf1': b'CleanupCacheOnLeave',\
b'\xf4': b'Code',\
b'\xf5': b'Data',\
b'\xf6': b'ReceiverGroup',\
b'\xf7': b'Cache',\
b'\xf8': b'GameProperties',\
b'\xf9': b'PlayerProperties',\
b'\xfa': b'Broadcast',\
b'\xfb': b'Properties',\
b'\xfc': b'ActorList',\
b'\xfd': b'TargetActorNr',\
b'\xfe': b'ActorNr',\
b'\xff': b'RoomName'}



CharacterNames = {\
1701: b'Calamity Heidi', \
1700: b'Bandita Sally', \
131: b'Smuggler Ike', \
140: b'Captain Wendy', \
27: b'Deckhand Butters', \
35: b'Gunslinger Kyle', \
50: b'Hookhand Clyde', \
92: b'Pirate Ship Timmy', \
200: b'Shaman Token', \
2114: b'Sharpshooter Shelly', \
205: b'Storyteller Jimmy', \
1276: b'Arrowstorm', \
1288: b'Barrel Dougie', \
1808: b'Buccaneer Bebe', \
134: b'Inuit Kenny', \
186: b'Lightning Bolt', \
28: b'Outlaw Tweek', \
8: b'Medicine Woman Sharon', \
45: b'Sheriff Cartman', \
12: b'Stan of Many Moons', \
2044: b'Swashbuckler Red', \
2266: b'Thunderbird', \
2209: b'Big Mesquite Murph', \
48: b'Incan Craig', \
10: b'Pocahontas Randy', \
24: b'Fireball', \
2013: b'Swordsman Garrison', \
55: b'Astronaut Butters', \
209: b'Enforcer Jimmy', \
203: b'Space Warrior Token', \
193: b'Alien Clyde', \
1949: b'Bounty Hunter Kyle', \
1824: b'Four-Assed Monkey', \
40: b'Freeze Ray', \
133: b'Gizmo Ike', \
52: b'Ice Sniper Wendy', \
1657: b'Poison', \
30: b'Program Stan', \
1805: b'Robo Bebe', \
1813: b'Visitors', \
46: b'Warboy Tweek', \
2101: b'Alien Drone', \
146: b'Cyborg Kenny', \
1269: b'Hyperdrive', \
49: b'Marine Craig', \
88: b'Mecha Timmy', \
1272: b'Mind Control', \
1311: b'Powerfist Dougie', \
2251: b'Sizzler Stuart', \
1509: b'Alien Queen Red', \
38: b'A.W.E.S.O.M.-O 4000', \
137: b'Sixth Element Randy', \
84: b'Choirboy Butters', \
1286: b'Power Bind', \
1273: b'Purify', \
86: b'Angel Wendy', \
1923: b'Cupid Cartman', \
208: b'Friar Jimmy', \
51: b'Hercules Clyde', \
138: b'Hermes Kenny', \
31: b'Poseidon Stan', \
1277: b'Regeneration', \
132: b'Scout Ike', \
1218: b'Youth Pastor Craig', \
158: b'Zen Cartman', \
1307: b'Energy Staff', \
85: b'Hallelujah', \
1983: b'Imp Tweek', \
2217: b'Jesus', \
1804: b'Medusa Bebe', \
1504: b'Prophet Dougie', \
1216: b'The Master Ninjew', \
201: b'Witch Doctor Token', \
44: b'Sexy Nun Randy', \
1274: b'Unholy Combustion', \
87: b'Pope Timmy', \
2043: b'Priest Maxi', \
57: b'Paladin Butters', \
37: b'Princess Kenny', \
1686: b'Underpants Gnomes', \
1806: b'Blood Elf Bebe', \
144: b'Canadian Knight Ike', \
91: b'Catapult Timmy', \
61: b'Dark Mage Craig', \
2042: b'Elven King Bradley', \
141: b'Shieldmaiden Wendy', \
29: b'Stan the Great', \
1656: b'Chicken Coop', \
1972: b'Dragonslayer Red', \
1506: b'Dwarf Engineer Dougie', \
179: b'Dwarf King Clyde', \
89: b'Kyle of the Drow Elves', \
206: b'Le Bard Jimmy', \
47: b'Robin Tweek', \
54: b'Rogue Token', \
135: b'The Amazingly Randy', \
176: b'Witch Garrison', \
1472: b'Cock Magic', \
2035: b'Mr. Slave Executioner', \
2210: b'Sorceress Liane', \
1655: b'Transmogrify', \
32: b'Grand Wizard Cartman', \
2200: b'Captain Diabetes', \
2117: b'Super Fart', \
2130: b'The Chomper', \
2132: b'Fastpass', \
2190: b'Lava!', \
2091: b'Mosquito', \
2202: b'Professor Chaos', \
2262: b'Super Craig', \
2144: b'Toolshed', \
2195: b'Doctor Timothy', \
2290: b'General Disarray', \
2143: b'Human Kite', \
2216: b'Mintberry Crunch', \
2098: b'Tupperware', \
2261: b'Wonder Tweek', \
2147: b'Mysterion', \
2141: b'The Coon', \
2136: b'Call Girl', \
1674: b'DogPoo', \
1872: b'Mr. Hankey', \
1666: b'Nelly', \
1407: b'Rat Swarm', \
1947: b'Towelie', \
1869: b'Marcus', \
2258: b'Mayor McDaniels', \
2074: b'Mr Mackey', \
15: b'Nathan', \
1886: b'PC Principal', \
1684: b'Pigeon Gang', \
1670: b'Starvin\' Marvin', \
1680: b'Terrance and Phillip', \
1665: b'Terrance Mephesto', \
1682: b'Big Gay Al', \
1973: b'Classi', \
1661: b'Mimsy', \
2030: b'President Garrison', \
2081: b'Santa Claus', \
1683: b'Officer Barbrady', \
2080: b'Satan', \
1672: b'ManBearPig', \
0: b'???'}

# 0: outgoing meta
# 1: incoming meta
# 2: outgoing battlefield data
# 3: incoming battlefield data
printcachelist = [[''],[''],[''],['']]
playeridcache = [[b''],[b'']]
timerstart = [None]
pingprintmessage = [None]

guifilepath = [r'C:\pathtooutput\sppd.darwingui']

upgrademap = [0,1,5,15,25,40,55,70,70,70,70,70]

nkxpmap = [0, \
	   0, \
	   10, \
	   10+25, \
	   10+25+50, \
	   10+25+50+100, \
	   10+25+50+100+200, \
	   10+25+50+100+200+325, \
	   10+25+50+100+200+325+500, \
	   10+25+50+100+200+325+500+700, \
	   10+25+50+100+200+325+500+700+850, \
	   10+25+50+100+200+325+500+700+850+1250, \
	   10+25+50+100+200+325+500+700+850+1250+1900, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000+12000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000+12000+15000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000+12000+15000+20000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000+12000+15000+20000+25000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000+12000+15000+20000+25000+30000, \
	   10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000+12000+15000+20000+25000+30000+45000]

assert (10+25+50+100+200+325+500+700+850+1250+1900+2250+2550+3000+3500+5000+7000+9000+12000+15000+20000+25000+30000+45000) == nkxpmap[25]
def logelementtocsv(param):
	(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = param
##		b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
##		csvkeylist = [(b'b', b'\x00'), (b'b', b'\x01'), (b'b', b'\x02'), (b'b', b'\x03'), \
##			      (b'b', b'\x04'), (b'b', b'\x05'), (b'b', b'\x06'), (b'b', b'\x07'), \
##			      (b'b', b'\x08'), (b'b', b'\t'), (b'b', b'\n'), (b'b', b'\x0b'), \
##			      (b'b', b'\x0c'), (b'b', b'\r'), (b'b', b'\x0e'), (b'b', b'\x0f')]
##		csvkeyexists = True
##		while True:
	updategui = False
	while True:
		if csvelem[0] == b'h':
			csvelemcopy = csvelem[1]
			csvelemcount = len(csvelemcopy)
			if csvcommandparam == (b'PlayerProperties' + b' ' + repr(b'\xf9').encode()):
				if csvelemcount == 1:
					csvi = 0
					csvelemsearch = list(csvelemcopy[csvi])[0]
					if csvelemsearch == (b'b', b'\xff'):
						w += b'\r\n' + wstatusprefix + b'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1]
						print (wstatusprefix.decode() + 'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1].decode(), flush=True)
						printcachelist[2] = ['']
						printcachelist[3] = ['']
						if wstatusprefix.decode() == ' >>> ':
							playeridcache[0][0] = csvelemcopy[csvi][csvelemsearch][1]
							printcachelist[0] = [wstatusprefix.decode() + 'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1].decode() + '\n']
						elif wstatusprefix.decode() == ' <<< ':
							playeridcache[1][0] = csvelemcopy[csvi][csvelemsearch][1]
							if not (playeridcache[0][0] != b'' and playeridcache[0][0] == playeridcache[1][0]):
								printcachelist[1] = [wstatusprefix.decode() + 'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1].decode() + '\n']
						else:
							print('Dropping duplicate player data for ' + csvelemcopy[csvi][csvelemsearch][1].decode(), flush=True)
						updategui = True
						break
					elif csvelemsearch == (b'i', b'\x00\x00\x00\x01') \
					     and csvelemcopy[csvi][csvelemsearch][0] == b'h':
						csvelemcopy = csvelemcopy[csvi][csvelemsearch][1]
						w += b'\r\n' + wstatusprefix + b'PlayerProperties encapsulated data follows: '
						print (wstatusprefix.decode() + 'PlayerProperties encapsulated data follows: ', flush=True)
					else:
						w += b'\r\n' + wstatusprefix + b'Unsupported PlayerProperties data: ' + repr(csvelemcopy).encode()
						print (wstatusprefix.decode() + 'Unsupported PlayerProperties data: ' + repr(csvelemcopy), flush=True)
						break
				else:
					w += b'\r\n' + wstatusprefix + b'PlayerProperties data follows: '
					print (wstatusprefix.decode() + 'PlayerProperties data follows: ', flush=True)
				
			csvi = 0
			csvelemcount = len(csvelemcopy)
			elementmeta = None
			elementdeck = None
			elementname = None
			elementteam = None
			elementid = None
			elementplayerid = None
			elementmatchrank = None
			elementrank = None
			elementelorank = None
			while csvi < csvelemcount:
				csvelemsearch = list(csvelemcopy[csvi])[0]
				if csvelemsearch == (b's', b'meta') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b's':
					elementmeta = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'deck') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b's':
					elementdeck = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'name') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b's':
					elementname = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'teamName') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b's':
					elementteam = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'profileId') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b's':
					elementid = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'playerId') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b'l':
					elementplayerid = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'matchmakingRank') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b'i':
					elementmatchrank = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'rank') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b'i':
					elementrank = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b's', b'eloRank') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b'i':
					elementelorank = csvelemcopy[csvi][csvelemsearch][1]
				elif csvelemsearch == (b'b', b'\xff') and \
				   csvelemcopy[csvi][csvelemsearch][0] == b's':
					w += b'\r\n' +  wstatusprefix + b'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1]
					print (wstatusprefix.decode() + 'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1].decode(), flush=True)
					printcachelist[2] = ['']
					printcachelist[3] = ['']
					if wstatusprefix.decode() == ' >>> ':
						printcachelist[0] = [wstatusprefix.decode() + 'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1].decode() + '\n']
					elif wstatusprefix.decode() == ' <<< ':
						printcachelist[1] = [wstatusprefix.decode() + 'PlayerProperties profile id: ' + csvelemcopy[csvi][csvelemsearch][1].decode() + '\n']
					updategui = True
				csvi += 1
			if elementmeta != None or elementdeck != None \
								  or elementname != None \
								  or elementteam != None \
								  or elementid != None:
				updategui = True
				print ('\n' + wstatusprefix.decode() + 'INTERPRETSPPD: Player details below', flush=True)
				printcache = ''
				printcachealreadyprinted = ''
				try:
					if elementname != None:
						print (wstatusprefix.decode() + "Name: " + elementname.decode(), flush=True)
						w += b'\r\n' + wstatusprefix + b"Name: " + elementname
						printcachealreadyprinted += wstatusprefix.decode() + "Name: " + elementname.decode() + '\n'
				except UnicodeEncodeError:
					if elementname != None:
						w += b'\r\n' + wstatusprefix + b"Unprintable Name: " + repr(elementname).encode()
						print (wstatusprefix.decode() + "Unprintable Name: " + repr(elementname), flush=True)
						printcachealreadyprinted += wstatusprefix.decode() + "Unprintable Name: " + repr(elementname) + '\n'
				try:
					if elementteam != None:
						print (wstatusprefix.decode() + "Team: " + elementteam.decode(), flush=True)
						w += b'\r\n' + wstatusprefix + b"Team: " + elementteam
						printcachealreadyprinted += wstatusprefix.decode() + "Team: " + elementteam.decode() + '\n'
				except UnicodeEncodeError:
					if elementteam != None:
						w += b'\r\n' + wstatusprefix + b"Unprintable Team: " + repr(elementteam).encode()
						print (wstatusprefix.decode() + "Unprintable Team: " + repr(elementteam), flush=True)
						printcachealreadyprinted += wstatusprefix.decode() + "Unprintable Team: " + repr(elementteam) + '\n'
				if elementid != None:
					if wstatusprefix.decode() == ' >>> ':
						playeridcache[0][0] = elementid
					elif wstatusprefix.decode() == ' <<< ':
						playeridcache[1][0] = elementid
					w += b'\r\n' + wstatusprefix + b"Profile ID: " + elementid
					printcache += wstatusprefix.decode() + "Profile ID: " + elementid.decode() + '\n'
				if elementplayerid != None:
					w += b'\r\n' + wstatusprefix + b"Player ID: " + str(int.from_bytes(elementplayerid, 'big')).encode()
					printcache += wstatusprefix.decode() + "Player ID: " + str(int.from_bytes(elementplayerid, 'big')) + '\n'
				if elementmatchrank != None or elementrank != None or elementelorank != None:
					w += b'\r\n' + wstatusprefix
					printcache += wstatusprefix.decode()
					if elementmatchrank != None:
						w += b"Matchmaking rank: " + str(int.from_bytes(elementmatchrank, 'big')).encode() + b','
						printcache += "Matchmaking rank: " + str(int.from_bytes(elementmatchrank, 'big')) + ','
					if elementrank != None:
						w += b"Rank: " + str(int.from_bytes(elementrank, 'big')).encode() + b','
						printcache += "Rank: " + str(int.from_bytes(elementrank, 'big')) + ','
					if elementelorank != None:
						w += b"Standing: " + str(int.from_bytes(elementelorank, 'big')).encode() + b','
						printcache += "Standing: " + str(int.from_bytes(elementelorank, 'big')) + ','
					printcache += '\n'
				if elementmeta != None:
					xpstring = "Player level: ?"
					xpi = 0
					elementmetad = json.loads(elementmeta)
					playerxp = int(elementmetad['PlayerExperience'])
					while xpi < len(nkxpmap):
						if nkxpmap[xpi] > playerxp:
							break
						else:
							xpstring = "Player level: "+str(xpi)
						xpi += 1
					if xpi < len(nkxpmap):
						xpstring += ", "
						assert xpi > 0
						xpstring += str(playerxp - nkxpmap[xpi-1]) + "/" + str(nkxpmap[xpi] - nkxpmap[xpi-1]) + " XP"
					else:
						xpstring += ", "
						assert xpi > 0
						xpstring += str(playerxp - nkxpmap[xpi-1]) + " XP"
					
					w += b'\r\n' + wstatusprefix + xpstring.encode()
					printcache += wstatusprefix.decode() + xpstring + "\n"
					w += b'\r\n' + wstatusprefix + b"Deck: "
					printcache += wstatusprefix.decode() + "Deck: "
					elementmetai = 0
					while elementmetai < len(elementmetad['Cards']):
						upgradeabovelevel = int(math.log2(elementmetad['Cards'][elementmetai]['TechTreeBits']+1))
						cardlevel = elementmetad['Cards'][elementmetai]['StarLevel']+1
						if elementmetad['Cards'][elementmetai]['Id'] not in CharacterNames:
							CharacterNames.update({elementmetad['Cards'][elementmetai]['Id']: \
									       b'Character#'+str(elementmetad['Cards'][elementmetai]['Id']).encode()})
						w += b'\r\n' + wstatusprefix + b'lvl '+str(cardlevel).encode() + b' ' + \
							CharacterNames[elementmetad['Cards'][elementmetai]['Id']] + \
							b' '+ str(upgrademap[cardlevel]+upgradeabovelevel).encode()+ b'/' + \
							str(upgrademap[cardlevel+1]).encode() +b', '
						printcache += 'lvl '+str(cardlevel) + ' ' + \
							CharacterNames[elementmetad['Cards'][elementmetai]['Id']].decode() + \
							' '+ str(upgrademap[cardlevel]+upgradeabovelevel)+ '/' + \
							str(upgrademap[cardlevel+1]) +', '
						elementmetai += 1
					printcache += " \n"
							
					
				print(printcache, flush=True)
				printcache = printcachealreadyprinted + printcache
				printcachelist[2] = ['']
				printcachelist[3] = ['']
				if wstatusprefix.decode() == ' >>> ':
					printcachelist[0] = [printcache]
				elif wstatusprefix.decode() == ' <<< ':
					if not (playeridcache[0][0] != b'' and playeridcache[0][0] == playeridcache[1][0]):
						printcachelist[1] = [printcache]
					else:
						print('Dropping duplicate player data for ' + playeridcache[1][0].decode(), flush=True)
				break
				
					
				
			
			csvelemcount = len(csvelem[1])
			csvi = 0
			printcache = ''
			keyzeroelementchecked = False
			while csvi < csvelemcount:
				csvw = b''
				csvw += b'"'+csvpackettime+b'"' #1
				csvw += b',"'+csvstream+b'"' #2
				csvw3 = b',"'+b'"' #3
				csvw3b = b','+str(csvtype).encode() #3b
				csvelemsearch = list(csvelem[1][csvi])[0]
				csvw4 = b',' #4
				csvw5 = b',' #5
				csvw6 = b',' #6
				csvw7 = b',' #7
				csvw8 = b',' #8
				csvw9 = b',' #9
				csvw10 = b',' #10
				csvw11 = b',' #11
				csvw12 = b',' #12
				csvw13 = b',' #13
				csvw14 = b',' #14
				csvw15 = b',' #15
				csvw16 = b',' #16
				csvw17 = b',' #17
				if csvelemsearch[0] == b'b':
					csvw3 = b',"'+b' Key = '+repr(csvelemsearch[1]).encode().replace(b'"', b'""')+b'"' #3
					if csvelem[1][csvi][csvelemsearch][0] == b'z':
						if csvelemsearch[1][0] >= 10 and csvelemsearch[1][0] <= 31:
							if keyzeroelementchecked == False:
								csvicopy = 0
								csvelemcountcopy = len(csvelem[1])
								keyzeroelementchecked = True
								while csvicopy < csvelemcountcopy:
									csvelemsearchcopy = list(csvelem[1][csvicopy])[0]
##									print ('csvelemsearchcopy='+repr(csvelemsearchcopy))
##									print ('csvelem[1][csvicopy][csvelemsearchcopy][0]='+repr(csvelem[1][csvicopy][csvelemsearchcopy][0]))
##									assert csvelemsearchcopy == (b'b', b'\x00')
##									assert csvelem[1][csvicopy][csvelemsearchcopy][0] == b'i'
									if csvelemsearchcopy == (b'b', b'\x00') and \
									   csvelem[1][csvicopy][csvelemsearchcopy][0] == b'i':
										temptimer = csvelem[1][csvicopy][csvelemsearchcopy][1]
										if timerstart[0] == None and temptimer != b'\x00\x00\x00\x00':
											timerstart[0] = temptimer
										if timerstart[0] != None and temptimer != b'\x00\x00\x00\x00':
											timercalctemp = int.from_bytes(temptimer, 'big') - int.from_bytes(timerstart[0], 'big')
											if timercalctemp < ((-1)*(1<<31)):
												timercalctemp += (1<<32)
											if timercalctemp >= ((1<<31)):
												timercalctemp -= (1<<32)
											w += b'\r\n' +  wstatusprefix + b'Timer = '+repr(timerstart[0]).encode() + b' + ' + \
											     '{0:.3f}'.format(timercalctemp/1000).encode() + b' seconds'
											printcache += wstatusprefix.decode() + 'Timer = ' + \
											     '{0:.3f}'.format(timercalctemp/1000) + ' seconds\n'
										else:
											w += b'\r\n' +  wstatusprefix + b'Timer is unavailable'
											printcache += wstatusprefix.decode() + 'Timer is unavailable\n'
										break
									csvicopy += 1
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##							csvw += b',"[0] i"' #5 instance
	##							csvw += b',"[1] o"' #6
	##							csvw += b',"[2] *"' #7
	##							csvw += b',"[3] i"' #8 target instance
	##							csvw += b',"[4] i"' #9
	##							csvw += b',"[5] k"' #10
	##							csvw += b',"[6] l"' #11 coordinates
	##							csvw += b',"[7] l"' #12 coordinates
	##							csvw += b',"[8] l"' #13 coordinates
	##							csvw += b',"[9] l"' #14
	##							csvw += b',"[10] d"' #15
	##							csvw += b',"[11] i"' #16 frames
	##							csvw += b',"[12] b"' #17
							csvelemlentemp = 0
							w += b'\r\n' + wstatusprefix
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									w += b'Instance#'+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()
									printcache += wstatusprefix.decode() + 'Instance#'+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True))
									if str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode() in characterinstances:
										characterinstancescharacter = characterinstances[str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()]
										if int(characterinstancescharacter) in CharacterNames:
											w += b' of ' + CharacterNames[int(characterinstancescharacter)]
											printcache += ' of ' + CharacterNames[int(characterinstancescharacter)].decode()
										else:
											w += b' of Character#' + characterinstancescharacter
											printcache += ' of Character#' + characterinstancescharacter.decode()
									csvw5 += b'"'
									w += b', '
	##									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
								
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'o':
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
##									printcache += '[1]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
								else:
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'*':
									csvw7 += b''
								else:
									csvw7 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									if csvelemlen == 13:
										w += b' Target Instance#'+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()
										printcache += ' Target Instance#'+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True))
										if str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode() in characterinstances:
											characterinstancescharacter = characterinstances[str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()]
											if int(characterinstancescharacter) in CharacterNames:
												w += b' of ' + CharacterNames[int(characterinstancescharacter)]
												printcache += ' of ' + CharacterNames[int(characterinstancescharacter)].decode()
											else:
												w += b' of Character#' + characterinstancescharacter
												printcache += ' of Character#' + characterinstancescharacter.decode()
										csvw8 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
										w += b', '
									else:
										printcache += '[3]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
								else:
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw9 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
									printcache += '[4]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
								else:
									csvw9 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'k':
									csvw10 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
									printcache += '[5]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
								else:
									csvw10 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							csvtmpint = None
							if csvelemlen > csvelemlentemp:
								printcache += ' at '
								if tmpelem[csvelemlentemp][0] == b'l':
									csvtmp = tmpelem[csvelemlentemp][1]
									w += b'Coordinates:'
									csvtmpint = int.from_bytes(csvtmp[0:8], 'big')
									w += b'x=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 0 ) ).encode()+ b','
									w += b'xsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 20 ) ).encode()+ b','
									w += b'z=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 21 ) ).encode()+ b','
									w += b'zsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 41 ) ).encode()+ b','
									w += b'y=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 42 ) ).encode()+ b','
									w += b'ysign=' + hex( ((1 << 2) - 1)  &  (csvtmpint >> 62 ) ).encode()+ b','
								else:
									csvw11 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'l':
									csvtmp = tmpelem[csvelemlentemp][1]
									w += b'NextCoordinates:'
									assert csvtmpint != None
									oldcsvtmpint = csvtmpint
									csvtmpint = int.from_bytes(csvtmp[0:8], 'big')
									w += b'x=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 0 ) ).encode()+ b','
									w += b'xsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 20 ) ).encode()+ b','
									w += b'z=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 21 ) ).encode()+ b','
									w += b'zsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 41 ) ).encode()+ b','
									w += b'y=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 42 ) ).encode()+ b','
									w += b'ysign=' + hex( ((1 << 2) - 1)  &  (csvtmpint >> 62 ) ).encode()+ b','
									
									printcache += 'x='
									if ( ((1 << 1) - 1)  &  (oldcsvtmpint >> 20 ) ):
										printcache += '-'
									else:
										printcache += '+'
									printcache += str( ((1 << 20) - 1)  &  (oldcsvtmpint >> 0 ) ) + '>'
									if ( ((1 << 1) - 1)  &  (csvtmpint >> 20 ) ):
										printcache += '-'
									else:
										printcache += '+'
									printcache += str( ((1 << 20) - 1)  &  (csvtmpint >> 0 ) ) + ','
									
									printcache += 'y='
									if ( ((1 << 1) - 1)  &  (oldcsvtmpint >> 62 ) ):
										printcache += '-'
									else:
										printcache += '+'
									printcache += str( ((1 << 20) - 1)  &  (oldcsvtmpint >> 42 ) ) + '>'
									if ( ((1 << 1) - 1)  &  (csvtmpint >> 62 ) ):
										printcache += '-'
									else:
										printcache += '+'
									printcache += str( ((1 << 20) - 1)  &  (csvtmpint >> 42 ) ) + ','
									
									printcache += 'z='
									if ( ((1 << 1) - 1)  &  (oldcsvtmpint >> 41 ) ):
										printcache += '-'
									else:
										printcache += '+'
									printcache += str( ((1 << 20) - 1)  &  (oldcsvtmpint >> 21 ) ) + '>'
									if ( ((1 << 1) - 1)  &  (csvtmpint >> 41 ) ):
										printcache += '-'
									else:
										printcache += '+'
									printcache += str( ((1 << 20) - 1)  &  (csvtmpint >> 21 ) ) + ','
										
									
								else:
									csvw12 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'l':
									csvtmp = tmpelem[csvelemlentemp][1]
									w += b'OpponentsCoordinates:'
									csvtmpint = int.from_bytes(csvtmp[0:8], 'big')
									w += b'x=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 0 ) ).encode()+ b','
									w += b'xsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 20 ) ).encode()+ b','
									w += b'z=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 21 ) ).encode()+ b','
									w += b'zsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 41 ) ).encode()+ b','
									w += b'y=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 42 ) ).encode()+ b','
									w += b'ysign=' + hex( ((1 << 2) - 1)  &  (csvtmpint >> 62 ) ).encode()+ b','
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'l':
									csvw14 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
									printcache += '[9]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
								else:
									csvw14 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'd':
									csvw15 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
									printcache += '[10]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
								else:
									csvw15 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw16 += b'"'+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')).encode()+b' frames"'
									printcache += '[frames]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
	##									csvw16 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw16 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'b':
									csvw17 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
##									printcache += '[12]=' + hex(int.from_bytes(tmpelem[csvelemlentemp][1], 'big')) + ','
								else:
									csvw17 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							printcache += '\n'
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x02')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] i"' #5 character id
	##								csvw += b',"[1] i"' #6
	##								csvw += b',"[2] l"' #7 location
	##								csvw += b',"[3] o"' #8
	##								csvw += b',"[4] i"' #9 card level
	##								csvw += b',"[5] y[i]"' #10 instance ID
	##								csvw += b',"[6] i"' #11
	##								csvw += b',"[7] i"' #12
	##								csvw += b',"[8] i"' #13
	##								csvw += b',"[9] d"' #14
	##								csvw += b',"[10] l"' #15
	##								csvw += b',"[11] i"' #16
	##								csvw += b',' #17
							csvelemlentemp = 0
							characterid = b'-1'
							w += b'\r\n' + wstatusprefix
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									if csvelemsearch == (b'b', b'\x04'):
										characterid = str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()
										if int(characterid) in CharacterNames:
											w += b' ' + CharacterNames[int(characterid)]
										else:
											w += b'Character#' + characterid
										w += b', '
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'l':
									if csvelemsearch == (b'b', b'\x04'):
										csvtmp = tmpelem[csvelemlentemp][1]
										w += b'Coordinates:'
										csvtmpint = int.from_bytes(csvtmp[0:8], 'big')
										w += b'x=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 0 ) ).encode()+ b','
										w += b'xsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 20 ) ).encode()+ b','
										w += b'z=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 21 ) ).encode()+ b','
										w += b'zsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 41 ) ).encode()+ b','
										w += b'y=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 42 ) ).encode()+ b','
										w += b'ysign=' + hex( ((1 << 2) - 1)  &  (csvtmpint >> 62 ) ).encode()+ b','
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'o':
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									if csvelemsearch == (b'b', b'\x04'):
										w += b'Card level:'+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)+1).encode()+b', '
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'y':
									csvw10elem = tmpelem[csvelemlentemp][1]
									csvw10len = len(csvw10elem)
									csvw10i = 0
									csvw10 += b'"'
									if csvelemsearch == (b'b', b'\x04'):
										csvw10 += b'Instance'
										w += b'Instance'
									while csvw10i < csvw10len:
										if csvw10elem[csvw10i][0] == b'i':
											if csvelemsearch == (b'b', b'\x04'):
												if int(characterid) in CharacterNames:
													w += b'#' + str(int.from_bytes(csvw10elem[csvw10i][1], 'big', signed=True)).encode() + b' of ' + CharacterNames[int(characterid)]
												else:
													w += b'#' + str(int.from_bytes(csvw10elem[csvw10i][1], 'big', signed=True)).encode() + b' of Character#' + characterid
												characterinstances.update({str(int.from_bytes(csvw10elem[csvw10i][1], 'big', signed=True)).encode():characterid})
												w += b' '
												csvw10 += b', '
											else:
												csvw10 += b'i ' + repr(csvw10elem[csvw10i][1]).encode().replace(b'"', b'""') + b', '
												w += b'i ' + repr(csvw10elem[csvw10i][1]).encode().replace(b'"', b'""') + b' '
										else:
											csvw10 += repr(csvw10elem[csvw10i]).encode().replace(b'"', b'""') + b', '
										csvw10i += 1
									csvw10 += b'"'
								else:
									csvw10 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
								w += b', '
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw11 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw11 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw12 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw12 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw13 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw13 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'd':
									csvw14 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw14 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'l':
									csvw15 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw15 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw16 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw16 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						elif b'\x04' == csvelemsearch[1] and (({(b'b', b'\x05'): (b'b', b'\n')} in csvelem[1]) or \
										      ({(b'b', b'\x05'): (b'b', b'\t')} in csvelem[1])):
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
							# damage packet?
	##								csvw += b',"[0] i"' #5 ? character hit id
	##								csvw += b',"[1] i"' #6 ? damage
	##								csvw += b',"[2] i"' #7 ? current hp
	##								csvw += b',"[3] o"' #8
	##								csvw += b',"[4] d"' #9 ? hit checksum
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							w += b'\r\n' + wstatusprefix
							temp_csvi = 0
							while temp_csvi < csvelemcount:
								temp_csvelemsearch = list(csvelem[1][temp_csvi])[0]
								if temp_csvelemsearch == (b'b', b'\x00'):
									key_00_value_packed = csvelem[1][temp_csvi][temp_csvelemsearch]
									if key_00_value_packed[0] == b'i':
										w += b'Received damage Instance#'+str(int.from_bytes(key_00_value_packed[1], 'big', signed=True)).encode()
										if str(int.from_bytes(key_00_value_packed[1], 'big', signed=True)).encode() in characterinstances:
											characterinstancescharacter = characterinstances[str(int.from_bytes(key_00_value_packed[1], 'big', signed=True)).encode()]
											if int(characterinstancescharacter) in CharacterNames:
												w += b' of ' + CharacterNames[int(characterinstancescharacter)]
											else:
												w += b' of Character#' + characterinstancescharacter
										w += b', '
										break
								temp_csvi += 1
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									w += b'Character hit Instance#'+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()
									if str(tmpelem[csvelemlentemp][1]).encode() in characterinstances:
										characterinstancescharacter = characterinstances[str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()]
										if int(characterinstancescharacter) in CharacterNames:
											w += b' of ' + CharacterNames[int(characterinstancescharacter)]
										else:
											w += b' of Character#' + characterinstancescharacter
									w += b', '
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									w += b'damage = '+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()
									w += b', '
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									w += b'current hp = '+str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()
									w += b', '
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'o':
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'd':
									w += b'hit checksum = '+repr(tmpelem[csvelemlentemp][1]).encode()
									w += b', '
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x0b')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] i"' #5
	##								csvw += b',"[1] i"' #6
	##								csvw += b',"[2] i"' #7
	##								csvw += b',"[3] b"' #8
	##								csvw += b',"[4] d"' #9
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw7 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw7 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'b':
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'd':
									csvw9 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw9 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x05')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] i"' #5 character id
	##								csvw += b',"[1] l"' #6 coordinates
	##								csvw += b',"[2] i"' #7
	##								csvw += b',"[3] d"' #8
	##								csvw += b',' #9
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							w += b'\r\n' + wstatusprefix
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
									characterid = str(int.from_bytes(tmpelem[csvelemlentemp][1], 'big', signed=True)).encode()
									if int(characterid) in CharacterNames:
										w += b' ' + CharacterNames[int(characterid)]
									else:
										w += b'Character#' + characterid
									w += b', '
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'l':
									csvtmp = tmpelem[csvelemlentemp][1]
									w += b'Coordinates:'
									csvtmpint = int.from_bytes(csvtmp[0:8], 'big')
									w += b'x=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 0 ) ).encode()+ b','
									w += b'xsign(opponent)=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 20 ) ).encode()+ b','
									w += b'z=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 21 ) ).encode()+ b','
									w += b'zsign=' + hex( ((1 << 1) - 1)  &  (csvtmpint >> 41 ) ).encode()+ b','
									w += b'y=' + str( ((1 << 20) - 1)  &  (csvtmpint >> 42 ) ).encode()+ b','
									w += b'ysign=' + hex( ((1 << 2) - 1)  &  (csvtmpint >> 62 ) ).encode()+ b','
								else:
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw7 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw7 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'd':
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x00')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] b"' #5
	##								csvw += b',"[1] i"' #6
	##								csvw += b',"[2] i"' #7
	##								csvw += b',"[3] d"' #8
	##								csvw += b',' #9
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'b':
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								pass
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								pass
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'd':
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw8 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x06')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] i"' #5
	##								csvw += b',"[1] i"' #6
	##								csvw += b',' #7
	##								csvw += b',' #8
	##								csvw += b',' #9
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x0c')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] i"' #5
	##								csvw += b',"[1] o"' #6
	##								csvw += b',' #7
	##								csvw += b',' #8
	##								csvw += b',' #9
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'i':
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
							csvelemlentemp += 1
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'o':
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw6 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x04')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] b"' #5
	##								csvw += b',' #6
	##								csvw += b',' #7
	##								csvw += b',' #8
	##								csvw += b',' #9
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'b':
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						elif b'\x04' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x08')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							csvelemlen = len(tmpelem)
							csvw4 += b'"z['+str(csvelemlen).encode()+b']:"'
	##								csvw += b',"[0] d"' #5
	##								csvw += b',' #6
	##								csvw += b',' #7
	##								csvw += b',' #8
	##								csvw += b',' #9
	##								csvw += b',' #10
	##								csvw += b',' #11
	##								csvw += b',' #12
	##								csvw += b',' #13
	##								csvw += b',' #14
	##								csvw += b',' #15
	##								csvw += b',' #16
	##								csvw += b',' #17
							csvelemlentemp = 0
							if csvelemlen > csvelemlentemp:
								if tmpelem[csvelemlentemp][0] == b'd':
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp][1]).encode().replace(b'"', b'""')+b'"'
								else:
									csvw5 += b'"'+repr(tmpelem[csvelemlentemp]).encode().replace(b'"', b'""')+b'"'
						else:
							csvw4 += b'"'+repr(csvelem[1][csvi][csvelemsearch]).encode().replace(b'"', b'""')+b'"'
					else:
##						w += b'\r\n' + wstatusprefix + b'DEBUG: ' + \
##						     b'csvelem[1][csvi][csvelemsearch][0] == ' + str(csvelem[1][csvi][csvelemsearch][0]).encode() + \
##						     b' and cselemsearch[1] == ' + str(csvelemsearch[1]).encode() + \
##						     b' and csvelem[1] == ' + str(csvelem[1]).encode()
						if csvelem[1][csvi][csvelemsearch][0] == b'i' and \
						     b'\x00' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x03')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							w += b'\r\n' + wstatusprefix
							w += b'Died Instance#'+str(int.from_bytes(tmpelem, 'big', signed=True)).encode()
							if str(int.from_bytes(tmpelem, 'big', signed=True)).encode() in characterinstances:
								characterinstancescharacter = characterinstances[str(int.from_bytes(tmpelem, 'big', signed=True)).encode()]
								if int(characterinstancescharacter) in CharacterNames:
									w += b' of ' + CharacterNames[int(characterinstancescharacter)]
								else:
									w += b' of Character#' + characterinstancescharacter
						elif csvelem[1][csvi][csvelemsearch][0] == b'i' and \
						     b'\x00' == csvelemsearch[1] and {(b'b', b'\x05'): (b'b', b'\x00')} in csvelem[1]:
							tmpelem = csvelem[1][csvi][csvelemsearch][1]
							w += b'\r\n' + wstatusprefix
							w += b'Charged Instance#'+str(int.from_bytes(tmpelem, 'big', signed=True)).encode()
							if str(int.from_bytes(tmpelem, 'big', signed=True)).encode() in characterinstances:
								characterinstancescharacter = characterinstances[str(int.from_bytes(tmpelem, 'big', signed=True)).encode()]
								if int(characterinstancescharacter) in CharacterNames:
									w += b' of ' + CharacterNames[int(characterinstancescharacter)]
								else:
									w += b' of Character#' + characterinstancescharacter
						else:
							csvw4 += b'"'+repr(csvelem[1][csvi][csvelemsearch]).encode().replace(b'"', b'""')+b'"'
				else:
					csvw4 += b'"? '+repr((b'h', [csvelem[1][csvi]])).encode().replace(b'"', b'""')+b'"'
				csvw += csvw3 + csvw3b + csvw4 + csvw5 + csvw6 + csvw7 + csvw8 + csvw9 + csvw10 + csvw11 + csvw12 + csvw13 + csvw14 + csvw15 + csvw16 + csvw17
				csvw += b'\r\n'
	##				t = csvfile.write(csvw)
				csvi += 1
			if printcache != '':
				updategui = True
				if wstatusprefix.decode() == ' >>> ':
					printcachelist[2] = [printcache]
				elif wstatusprefix.decode() == ' <<< ':
					printcachelist[3] = [printcache]
				pingprintmessagecache = 'Ping = ?\n'
				if pingprintmessage[0] != None:
					pingprintmessagecache = pingprintmessage[0] + '\n'
				print('\n\n\n'+pingprintmessagecache+printcachelist[0][0] + printcachelist[1][0] + printcachelist[2][0] + printcachelist[3][0], flush=True)

		elif csvelem[0] == b's' and csvcommandparam == (b'Data' + b' ' + repr(b'\xf5').encode()):
			w += b'\r\n' + wstatusprefix + b"Query: " + csvelem[1]
			print (wstatusprefix.decode() + "Query: " + csvelem[1].decode(), flush=True)
		else:
			csvw = b''
			csvw += b'"'+csvpackettime+b'"' #1
			csvw += b',"'+csvstream+b'"' #2
			csvw3 = b',"'+b'"' #3
			csvw3b = b','+str(csvtype).encode() #3b
			csvw4 = b',' #4
			csvw5 = b',' #5
			csvw6 = b',' #6
			csvw7 = b',' #7
			csvw8 = b',' #8
			csvw9 = b',' #9
			csvw10 = b',' #10
			csvw11 = b',' #11
			csvw12 = b',' #12
			csvw13 = b',' #13
			csvw14 = b',' #14
			csvw15 = b',' #15
			csvw16 = b',' #16
			csvw17 = b',' #17
			csvw4 += b'"??? '+repr(csvelem).encode().replace(b'"', b'""')+b'"'
			csvw += csvw3 + csvw3b + csvw4 + csvw5 + csvw6 + csvw7 + csvw8 + csvw9 + csvw10 + csvw11 + csvw12 + csvw13 + csvw14 + csvw15 + csvw16 + csvw17
			csvw += b'\r\n'
	##			t = csvfile.write(csvw)
		break
	pingprintmessagecache = ''
	if pingprintmessage[0] != None:
		pingprintmessagecache = pingprintmessage[0] + '\n'
	if (pingprintmessagecache != '' or \
	   printcachelist[0][0] != '' or \
	   printcachelist[1][0] != '' or \
	   printcachelist[2][0] != '' or \
	   printcachelist[3][0] != '') and updategui:
		with open(guifilepath[0], 'ab', buffering=0) as gui_f:
			gui_dict_1_header = b'h\x00\x01'
			gui_string_sppd = b'sppd'
			gui_sstring_sppd = b's'+(len(gui_string_sppd).to_bytes(2, byteorder='big'))+gui_string_sppd
			
			gui_dict_4_header = b'h\x00\x04'
			gui_string_sentmeta = b'sentmeta'
			gui_sstring_sentmeta = b's'+(len(gui_string_sentmeta).to_bytes(2, byteorder='big'))+gui_string_sentmeta
			gui_string_receivedmeta = b'receivedmeta'
			gui_sstring_receivedmeta = b's'+(len(gui_string_receivedmeta).to_bytes(2, byteorder='big'))+gui_string_receivedmeta
			gui_string_sentposition = b'sentposition'
			gui_sstring_sentposition = b's'+(len(gui_string_sentposition).to_bytes(2, byteorder='big'))+gui_string_sentposition
			gui_string_receivedposition = b'receivedposition'
			gui_sstring_receivedposition = b's'+(len(gui_string_receivedposition).to_bytes(2, byteorder='big'))+gui_string_receivedposition

			
			gui_string_sentmeta_ = (pingprintmessagecache+printcachelist[0][0]).encode()
			gui_sstring_sentmeta_ = b's'+(len(gui_string_sentmeta_).to_bytes(2, byteorder='big'))+gui_string_sentmeta_
			gui_string_receivedmeta_ = (printcachelist[1][0]).encode()
			gui_sstring_receivedmeta_ = b's'+(len(gui_string_receivedmeta_).to_bytes(2, byteorder='big'))+gui_string_receivedmeta_
			gui_string_sentposition_ = (printcachelist[2][0]).encode()
			gui_sstring_sentposition_ = b's'+(len(gui_string_sentposition_).to_bytes(2, byteorder='big'))+gui_string_sentposition_
			gui_string_receivedposition_ = (printcachelist[3][0]).encode()
			gui_sstring_receivedposition_ = b's'+(len(gui_string_receivedposition_).to_bytes(2, byteorder='big'))+gui_string_receivedposition_

			gui_dict_4 = gui_dict_4_header + \
				     gui_sstring_sentmeta + gui_sstring_sentmeta_ + \
				     gui_sstring_receivedmeta + gui_sstring_receivedmeta_ + \
				     gui_sstring_sentposition + gui_sstring_sentposition_ + \
				     gui_sstring_receivedposition + gui_sstring_receivedposition_

			gui_dict_1 = gui_dict_1_header + \
				     gui_sstring_sppd + gui_dict_4

			gui_header_size = len(b'\xfb\x00\x00\x00\x05')
			
			gui_buffer = b'\xfb' + (gui_header_size + len(gui_dict_1)).to_bytes(4, byteorder='big') + gui_dict_1
			assert len(gui_buffer) == int.from_bytes(gui_buffer[1:5], 'big')
			gui_temp = gui_f.write(gui_buffer)
	return (csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix)

	








def processelement(param):
	## params:
	# > ja: element count (1)
	# > haskeys: elements are being read from dictionary, reads key element and value element (False)
	# > b: input (b'')
	# > jbase + j: position at input (5), jbase: constant increment generated outside this function, j: variable increment generated by this function
	# > w: output (b'')
	# > splitindex, wi, d, stream: unused (0, 0, {}, b'')
	# > input parameter writeelem: write tree representation of element to output (False)
	# > output parameter elem: element
	# > wstatusprefix: prefix for tree representation (b'')
	
	(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, writeelem, wstatusprefix) = param
##	w += b'\r\n DEBUG: processelement received param = ' + repr((ja, haskeys, b, jbase, j, 'len(w) = ' + str(len(w)), splitindex, wi, d, stream, writeelem, wstatusprefix)).encode() +  b'\r\n'
	stack = {}
	elemprettyprint = b''
	elemprettyprintdepth = 1
	elem = (b'z', [])
	if haskeys:
		elem = (b'h', [])
	stack.update({1:(0, ja, haskeys, elem)})
	stackindex = 1
	while stackindex > 0:
		jc, ja, haskeys, elem = stack[stackindex]
		if jc in range(0, ja):
			key = None
			if haskeys:
				if b[jbase+j+0:jbase+j+1] == b's':
					jtemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
					w2 = b[jbase+j+3:jbase+j+jtemp+3]
					j += jtemp
					if len(w2) != jtemp:
						break
					key = (b's', w2)
					if elemprettyprintdepth != stackindex:
						elemprettyprint += b'\r\n' + wstatusprefix
						elemprettyprintdepth = stackindex
						p = elemprettyprintdepth
						while p > 1:
							elemprettyprint += b'\t'
							p -= 1
					elemprettyprint += b's ' + repr(w2).encode() + b': '
					j += ((jbase+3) - (jbase+0))
				elif b[jbase+j+0:jbase+j+1] == b'b':
					key = (b'b', b[jbase+j+1:jbase+j+2])
					if elemprettyprintdepth != stackindex:
						elemprettyprint += b'\r\n' + wstatusprefix
						elemprettyprintdepth = stackindex
						p = elemprettyprintdepth
						while p > 1:
							elemprettyprint += b'\t'
							p -= 1
					elemprettyprint += b'b ' + repr(b[jbase+j+1:jbase+j+2]).encode() + b': '
					j += ((jbase+2) - (jbase+0))
				elif b[jbase+j+0:jbase+j+1] == b'i':
					key = (b'i', b[jbase+j+1:jbase+j+5])
					if elemprettyprintdepth != stackindex:
						elemprettyprint += b'\r\n' + wstatusprefix
						elemprettyprintdepth = stackindex
						p = elemprettyprintdepth
						while p > 1:
							elemprettyprint += b'\t'
							p -= 1
					elemprettyprint += b'i ' + repr(b[jbase+j+1:jbase+j+5]).encode() + b': '
					j += ((jbase+5) - (jbase+0))
				else:
					if elemprettyprintdepth != stackindex:
						elemprettyprint += b'\r\n' + wstatusprefix
						elemprettyprintdepth = stackindex
						p = elemprettyprintdepth
						while p > 1:
							elemprettyprint += b'\t'
							p -= 1
					elemprettyprint += b'??? '
					w += b'/* Unsupported operation ' + repr(b[jbase+j+0:jbase+j+1]).encode() + b' at position ' + \
					     str(jbase+j+0).encode() + b' */ ' + repr(b[:]).encode()
					if writeelem:
						w += b'/* ' + elemprettyprint + b' */ '
					break
			if b[jbase+j+0:jbase+j+1] == b's':
				jtemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				w2 = b[jbase+j+3:jbase+j+jtemp+3]
				j += jtemp
				if len(w2) != jtemp:
					break
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b's ' + repr(w2).encode() + b', '
				if haskeys:
					elem[1].append({key:(b's', w2)})
				else:
					elem[1].append((b's', w2))
				j += ((jbase+3) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'l':
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'l ' + repr(b[jbase+j+1:jbase+j+9]).encode() + b', '
				if haskeys:
					elem[1].append({key:(b'l', b[jbase+j+1:jbase+j+9])})
				else:
					elem[1].append((b'l', b[jbase+j+1:jbase+j+9]))
				j += ((jbase+9) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'i':
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'i ' + repr(b[jbase+j+1:jbase+j+5]).encode() + b', '
				if haskeys:
					elem[1].append({key:(b'i', b[jbase+j+1:jbase+j+5])})
				else:
					elem[1].append((b'i', b[jbase+j+1:jbase+j+5]))
				j += ((jbase+5) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'o':
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'o ' + repr(b[jbase+j+1:jbase+j+2]).encode() + b', '
				if haskeys:
					elem[1].append({key:(b'o', b[jbase+j+1:jbase+j+2])})
				else:
					elem[1].append((b'o', b[jbase+j+1:jbase+j+2]))
				j += ((jbase+2) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'h':
				w2 = b[jbase+j+0:jbase+j+3]
				jatemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				if len(w2) != 3:
					break
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'h[' + str(jatemp).encode() + b'] '
				tempelem = (b'h', [])
				if haskeys:
					elem[1].append({key:tempelem})
				else:
					elem[1].append(tempelem)
				j += ((jbase+3) - (jbase+0))
				jc += 1
				stack.update({stackindex:(jc, ja, haskeys, elem)})
				haskeystemp = True
				stack.update({stackindex+1:(0, jatemp, haskeystemp, tempelem)})
				stackindex += 1
				continue
			elif b[jbase+j+0:jbase+j+1] == b'b':
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'b ' + repr(b[jbase+j+1:jbase+j+2]).encode() + b', '
				if haskeys:
					elem[1].append({key:(b'b', b[jbase+j+1:jbase+j+2])})
				else:
					elem[1].append((b'b', b[jbase+j+1:jbase+j+2]))
				j += ((jbase+2) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'y' and b[jbase+j+3:jbase+j+4] == b's':
				jatemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				tempelem = (b'y', [])
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'y['
				if haskeys:
					elem[1].append({key:tempelem})
				else:
					elem[1].append(tempelem)
				for jctemp in range(0, jatemp):
					jtemp = int.from_bytes(b[jbase+j+4:jbase+j+6], "big")
					elemprettyprint += b's ' + repr(b[jbase+j+6:jbase+j+jtemp+6]).encode() + b', '
					tempelem[1].append((b's', b[jbase+j+6:jbase+j+jtemp+6]))
					j += jtemp
					j += ((jbase+6) - (jbase+4))
				elemprettyprint += b'], '
				j += ((jbase+4) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'y' and b[jbase+j+3:jbase+j+4] == b'i':
				jatemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				tempelem = (b'y', [])
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'y['
				if haskeys:
					elem[1].append({key:tempelem})
				else:
					elem[1].append(tempelem)
				for jctemp in range(0, jatemp):
					elemprettyprint += b'i ' + repr(b[jbase+j+4:jbase+j+8]).encode() + b', '
					tempelem[1].append((b'i', b[jbase+j+4:jbase+j+8]))
					j += ((jbase+8) - (jbase+4))
				elemprettyprint += b'], '
				j += ((jbase+4) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'y' and b[jbase+j+3:jbase+j+4] == b'o':
				jatemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				tempelem = (b'y', [])
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'y['
				if haskeys:
					elem[1].append({key:tempelem})
				else:
					elem[1].append(tempelem)
				for jctemp in range(0, jatemp):
					elemprettyprint += b'o ' + repr(b[jbase+j+4:jbase+j+5]).encode() + b', '
					tempelem[1].append((b'o', b[jbase+j+4:jbase+j+5]))
					j += ((jbase+5) - (jbase+4))
				elemprettyprint += b'], '
				j += ((jbase+4) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'z':
				jatemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				tempelem = (b'z', [])
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'z[' + str(jatemp).encode() + b'] '
				if haskeys:
					elem[1].append({key:tempelem})
				else:
					elem[1].append(tempelem)
				j += ((jbase+3) - (jbase+0))
				jc += 1
				stack.update({stackindex:(jc, ja, haskeys, elem)})
				haskeystemp = False
				stack.update({stackindex+1:(0, jatemp, haskeystemp, tempelem)})
				stackindex += 1
				continue
			elif b[jbase+j+0:jbase+j+1] == b'*':
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'*, '
				if haskeys:
					elem[1].append({key:(b'*', b'')})
				else:
					elem[1].append((b'*', b''))
				j += ((jbase+1) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'k':
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'k ' + repr(b[jbase+j+1:jbase+j+3]).encode() + b', '
				if haskeys:
					elem[1].append({key:(b'k', b[jbase+j+1:jbase+j+3])})
				else:
					elem[1].append((b'k', b[jbase+j+1:jbase+j+3]))
				j += ((jbase+3) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'd':
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'd ' + repr(b[jbase+j+1:jbase+j+9]).encode() + b', '
				if haskeys:
					elem[1].append({key:(b'd', b[jbase+j+1:jbase+j+9])})
				else:
					elem[1].append((b'd', b[jbase+j+1:jbase+j+9]))
				j += ((jbase+9) - (jbase+0))
			elif b[jbase+j+0:jbase+j+1] == b'j':
				jatemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				tempelem = (b'j', [])
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'j[' + str(jatemp).encode() + b'] '
				if haskeys:
					elem[1].append({key:tempelem})
				else:
					elem[1].append(tempelem)
				j += ((jbase+3) - (jbase+0))
				jc += 1
				stack.update({stackindex:(jc, ja, haskeys, elem)})
				haskeystemp = False
				stack.update({stackindex+1:(0, jatemp, haskeystemp, tempelem)})
				stackindex += 1
				continue
			elif b[jbase+j+0:jbase+j+1] == b'x':
				jatemp = int.from_bytes(b[jbase+j+1:jbase+j+3], "big")
				tempelem = (b'x', [])
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'x[' + str(jatemp).encode() + b'] '
				if haskeys:
					elem[1].append({key:tempelem})
				else:
					elem[1].append(tempelem)
				j += ((jbase+3) - (jbase+0))
				jc += 1
				stack.update({stackindex:(jc, ja, haskeys, elem)})
				haskeystemp = False
				stack.update({stackindex+1:(0, jatemp, haskeystemp, tempelem)})
				stackindex += 1
				continue
			else:
				if elemprettyprintdepth != stackindex:
					elemprettyprint += b'\r\n' + wstatusprefix
					elemprettyprintdepth = stackindex
					p = elemprettyprintdepth
					while p > 1:
						elemprettyprint += b'\t'
						p -= 1
				elemprettyprint += b'??? '
				w += b'/* Unsupported operation ' + repr(b[jbase+j+0:jbase+j+1]).encode() + b' at position ' + \
				     str(jbase+j+0).encode() + b' */ ' + repr(b[:]).encode()
				if writeelem:
					w += b'/* ' + elemprettyprint + b' */ '
				break
			jc += 1
			stack.update({stackindex:(jc, ja, haskeys, elem)})
		else:
			stackindex -= 1
	if stackindex == 0:
		jc, ja, haskeys, elem = stack[1]
		if elem[0] == b'z' and len(elem[1]) == 1:
			elem = elem[1][0]
		if writeelem:
			w += b'/* ' + elemprettyprint + b' */ '
	else:
		w += b'\r\n DEBUG: processelement sent param = ' + repr((ja, haskeys, b, jbase, j, 'len(w) = ' + str(len(w)), splitindex, wi, d, stream, elem, wstatusprefix)).encode() +  b'\r\n'
		print('processelem crashed, setting pointer at the end of the data...', flush=True)
		j = len(b)-jbase
				
			
	return (ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix)








##def interpretsppd(param1, param2):

pingdictionary = [{}]
def interpretsppd(param1line, param2file, othervariables):
	#param1: output from tshark
	#csvpackettime0 + b', ' + b'0000 ' + csvpackettimehours + b':' + csvpackettimeminutes + b':' + csvpackettimeseconds + b'\t'
	# + source + b'\t'
	# + sourceport + b'\t'
	# + destination + b'\t'
	# + destinationport + b'\t' + b.hex().encode()
	# + b'\r\n'
	# param2file: file handle
	# type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})()
	# csvw: unused
	# b''
	# streamfilter: dictionary containing a list of sppd streams
	# {(b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport): (b'Command decoding below\r\n', b'Client')}
	# d: stores fragments of photon packets
	# {}
	# characterinstances: list of character instance ids
	# {}
	# csvfile: used in dead code
	# type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})()

	# 
	(csvw, streamfilter, d, characterinstances, csvfile) = othervariables


	s, s_ = param1line.split(b'\r\n')
	assert s_ == b''
	
	while True:
		w = b''
		if not (s == b'mpeg_packets_dump.lua only works in Wireshark' or s.startswith(b'Not representable')):
			if s:
				b = bytes.fromhex(s[s.rindex(b'\t')+1:].decode())
				stream = s[s.index(b'\t'):s.rindex(b'\t')]
				temp, source, sourceport, destination, destinationport = \
				      stream.split(b'\t')
				csvpackettime = s[:s.index(b'\t')]
				csvpackettime0, csvpackettime1 = csvpackettime.split(b', ')
				csvpackettime1split = csvpackettime1.split(b' ')
				csvpackettimehoursminutesseconds = csvpackettime1split[1]
				csvpackettimehours, csvpackettimeminutes, csvpackettimeseconds = csvpackettimehoursminutesseconds.split(b':')
				csvpackettimesecondsfloat = (int(csvpackettimehours)*60 + int(csvpackettimeminutes))*60 + float(csvpackettimeseconds)
				csvstream = s[s.index(b'\t')+1:s.rindex(b'\t')].replace(b'\t', b' ')
				wcache = b''
				wstatus = b''
				if ((not ((b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport) in streamfilter)) or \
				   (not ((b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport) in streamfilter))) and \
				   b[:1] == b'\xfb' and len(b[1:5]) == 4 and len(b) == int.from_bytes(b[1:5], 'big'):
					characterinstances = {}
					timerstart[0] = None
					pingdictionary[0] = {}
					pingprintmessage[0] = None
					if destinationport == b'4530' or destinationport == b'4531' or destinationport == b'4533':
						w += b'>>> \r\n>>> \r\n>>> \r\n >>> \r\n'
						wstatus = b'Client'
						streamfilter.update({stream:(b'\r\n???\r\n', wstatus)})
						streamfilter.update({(b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport):(b'\r\n???\r\n', b'Server')})
					else:
						w += b'<<< \r\n<<< \r\n<<< \r\n <<< \r\n'
						wstatus = b'Server'
						streamfilter.update({stream:(b'\r\n???\r\n', wstatus)})
						streamfilter.update({(b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport):(b'\r\n???\r\n', b'Client')})
						
				
				if (not ((b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport) in streamfilter)) and b == b'\x01\x00':
					characterinstances = {}
					wcache = b'<<< \r\n<<< \r\n<<< \r\n <<< ' + s[:s.rindex(b'\t')+1] + b'/* Welcome to our server! */ ' + repr(b).encode() + b'\r\n'
					wstatus = b'Init'
					streamfilter.update({stream:(wcache, wstatus)})
					timerstart[0] = None
					pingdictionary[0] = {}
					pingprintmessage[0] = None
##					continue
					break
				if (b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport) in streamfilter and \
				   streamfilter[b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport][1] == b'Init' and \
				   (b[:1] == b'\xf0' or b[:1] == b'\xfb' or b == b'\x01\x00'):
					w += streamfilter[b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport][0]
					timerstart[0] = None
					pingdictionary[0] = {}
					pingprintmessage[0] = None
					wstatus = b'Server'
					streamfilter.update({stream:(wcache, wstatus)})
					streamfilter.update({(b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport):(b'', b'Client')})
				if (b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport) in streamfilter and \
				   streamfilter[b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport][1] == b'Init' and \
				   (b[:1] == b'\xf0' or b[:1] == b'\xfb'):
					w += streamfilter[b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport][0]
					timerstart[0] = None
					pingdictionary[0] = {}
					pingprintmessage[0] = None
					wstatus = b'Client'
					streamfilter.update({stream:(b'', wstatus)})
					streamfilter.update({(b'\t'+destination+b'\t'+destinationport+b'\t'+source+b'\t'+sourceport):(wcache, b'Server')})
				while (b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport) in streamfilter:
					#continue goes here
					wstatus = streamfilter[b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport][1]
					wstatusprefix = b''
					if wstatus == b'Server':
						wstatusprefix = b' <<< '
					elif wstatus == b'Client':
						wstatusprefix = b' >>> '
					w += wstatusprefix
					splitindex = 0
					if stream in d:
						b2 = d[stream]
						btemp = b2 + b
						splitindex = len(b2)
						b = btemp[:]
						del d[stream]
					if b == b'\x01\x00':
						characterinstances = {}
						timerstart[0] = None
						pingdictionary[0] = {}
						pingprintmessage[0] = None
						w += b'<<< \r\n<<< \r\n<<< \r\n <<< ' + s[:s.rindex(b'\t')+1] + b'/* Welcome to our server! */ ' + repr(b).encode() + b'\r\n'
	##							wstatus = b'Init'
	##							streamfilter.update({stream:(wcache, wstatus)})
					elif b[:1] == b'\xf0':
						w += s[:s.rindex(b'\t')+1]
						w += b'/* Ping */ ' + repr(b[:1]).encode()
						j = 0
						servertime = None
						if wstatus == b'Server':
							servertime = b[1+j:5+j]
							w += b'/* Server time */ ' + repr(servertime).encode()
							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, b'Server time', (b'i', b[1+j:5+j]), csvfile, 0, characterinstances, w, wstatusprefix))
							j += 4
						clienttime = b[1+j:5+j]
						w += b'/* Client time */ ' + repr(clienttime).encode()
						w += b'\r\n'
						if servertime != None:
							if clienttime in pingdictionary[0]:
								csvpackettimesecondsfloatold = pingdictionary[0][clienttime]
								csvpackettimedelta = csvpackettimesecondsfloat - csvpackettimesecondsfloatold
								if csvpackettimedelta < 0:
									csvpackettimedelta += 24*60*60
								w += wstatusprefix + b'Ping = '+("{0:.3f}".format(csvpackettimedelta*1000)).encode() + b' ms\r\n'
								pingprintmessage[0] = wstatusprefix.decode() + 'Ping = '+("{0:.3f}".format(csvpackettimedelta*1000)) + ' ms'
								print (wstatusprefix.decode() + 'Ping = '+("{0:.3f}".format(csvpackettimedelta*1000)) + ' ms', flush=True)
								del pingdictionary[0][clienttime]
							else:
								w += wstatusprefix + b'Ping '+repr(clienttime).encode() +b' is missing!\r\n'
								pingprintmessage[0] = wstatusprefix.decode() + 'Ping '+repr(clienttime) + ' is missing!'
								print(wstatusprefix.decode() + 'Ping '+repr(clienttime) + ' is missing!', flush=True)
						else:
							pingdictionary[0].update({clienttime:csvpackettimesecondsfloat})
						if b[5+j:]:
							temp = b[5+j:]
							b = temp[:]
							continue
					elif b[:1] == b'\xfb':

						## data from https://github.com/rbrasga/sppd_mod/blob/master/BinaryMonitor.py

##						tempstring = b'b\x05b\x05b\x04z\x00\x04i\x00\x00'
##						tempinteger = bsafecopy.find(tempstring)
##						if tempinteger > (-1):
##							rbrasga_start = tempinteger + \
##									len(tempstring)
##							rbrasga_cardid = bsafecopy[rbrasga_start:rbrasga_start+2]
##							rbrasga_location_header = bsafecopy[rbrasga_start+2:rbrasga_start+2+1]
##							rbrasga_location = bsafecopy[rbrasga_start+3:rbrasga_start+3+8]
##							rbrasga_opponent = bsafecopy[rbrasga_start+14:rbrasga_start+14+2]
##							w += b'rbrasga_spellSearch: found '+str(tempstring).encode() + \
##							     b' at position ' +str(tempinteger).encode() + b' for data ' + str(bsafecopy).encode() + \
##							     b'; ['+str(rbrasga_start).encode() + b']cardid='+str(rbrasga_cardid).encode() + \
##							     b'; ['+str(rbrasga_start+2).encode() + b']location_header='+str(rbrasga_location_header).encode() + \
##							     b'; ['+str(rbrasga_start+3).encode() + b']location='+str(rbrasga_location).encode() + \
##							     b'; ['+str(rbrasga_start+14).encode() + b']opponent='+str(rbrasga_opponent).encode() + \
##							     b'\r\n'
##							print (wstatusprefix.decode() + 'rbrasga_spellSearch: found a match at position ' +str(tempinteger) + \
##							     '; cardid='+str(rbrasga_cardid) + \
##							     '; location_header='+str(rbrasga_location_header) + \
##							     '; location='+str(rbrasga_location) + \
##							     '; opponent='+str(rbrasga_opponent), flush=True)
##							w += wstatusprefix
##
##						
##						tempstring = b'b\x05b\x02b\x04z\x00\x0ci\x00\x00'
##						tempinteger = bsafecopy.find(tempstring)
##						if tempinteger > (-1):
##							rbrasga_start = tempinteger + \
##									len(tempstring)
##							rbrasga_cardid = bsafecopy[rbrasga_start:rbrasga_start+2]
##							rbrasga_opponent = bsafecopy[rbrasga_start+5:rbrasga_start+5+2]
##							rbrasga_location_header = bsafecopy[rbrasga_start+7:rbrasga_start+8]
##							rbrasga_location = bsafecopy[rbrasga_start+8:rbrasga_start+8+8]
##							rbrasga_card_level = bsafecopy[rbrasga_start+21:rbrasga_start+21+2]
##							rbrasga_unique_id = bsafecopy[rbrasga_start+21+2+3+1:rbrasga_start+21+2+3+1+4]
##							w += b'rbrasga_characterSearch: found '+str(tempstring).encode() + \
##							     b' at position ' +str(tempinteger).encode() + b' for data ' + str(bsafecopy).encode() + \
##							     b'; ['+str(rbrasga_start).encode() + b']cardid='+str(rbrasga_cardid).encode() + \
##							     b'; ['+str(rbrasga_start+5).encode() + b']opponent='+str(rbrasga_opponent).encode() + \
##							     b'; ['+str(rbrasga_start+7).encode() + b']location_header='+str(rbrasga_location_header).encode() + \
##							     b'; ['+str(rbrasga_start+8).encode() + b']location='+str(rbrasga_location).encode() + \
##							     b'; ['+str(rbrasga_start+21).encode() + b']card_level='+str(rbrasga_card_level).encode() + \
##							     b'; ['+str(rbrasga_start+21+2+3+1).encode() + b']unique_id='+str(rbrasga_unique_id).encode() + \
##							     b'\r\n'
##							print (wstatusprefix.decode() + 'rbrasga_characterSearch: found a match at position ' +str(tempinteger) + \
##							     '; cardid='+str(rbrasga_cardid) + \
##							     '; opponent='+str(rbrasga_opponent) + \
##							     '; location_header='+str(rbrasga_location_header) + \
##							     '; location='+str(rbrasga_location) + \
##							     '; card_level='+str(rbrasga_card_level) + \
##							     '; unique_id='+str(rbrasga_unique_id), flush=True)
##							w += wstatusprefix
##
##						tempstring = b'\xfb\x00\x00\x00%\x00\x01\xf3\x02\xfd\x00\x02\xf4b\xc8\xf5h\x00\x03b\x00i'
##						tempinteger = bsafecopy.find(tempstring)
##						if tempinteger > (-1):
##							rbrasga_start = tempinteger + \
##									len(tempstring)
##							rbrasga_unique_id = bsafecopy[rbrasga_start:rbrasga_start+4]
##							w += b'rbrasga_findDeath: found '+str(tempstring).encode() + \
##							     b' at position ' +str(tempinteger).encode() + b' for data ' + str(bsafecopy).encode() + \
##							     b'; ['+str(rbrasga_start).encode() + b']unique_id='+str(rbrasga_unique_id).encode() + \
##							     b'\r\n'
##							print (wstatusprefix.decode() + 'rbrasga_findDeath: found a match at position ' +str(tempinteger) + \
##							     '; unique_id='+str(rbrasga_unique_id), flush=True)
##							w += wstatusprefix
##
##						tempstring = b'\xfb\x00\x00\x00(\x00\x01\xf3\x04\xc8\x00\x02\xf5h\x00\x03b\x05b\x03b\x02'
##						tempinteger = bsafecopy.find(tempstring)
##						if tempinteger > (-1):
##							rbrasga_start = tempinteger + \
##									len(tempstring) + 5 + 2 + 1
##							rbrasga_unique_id = bsafecopy[rbrasga_start:rbrasga_start+4]
##							w += b'rbrasga_findOppDeath: found '+str(tempstring).encode() + \
##							     b' at position ' +str(tempinteger).encode() + b' for data ' + str(bsafecopy).encode() + \
##							     b'; ['+str(rbrasga_start).encode() + b']unique_id='+str(rbrasga_unique_id).encode() + \
##							     b'\r\n'
##							print (wstatusprefix.decode() + 'rbrasga_findOppDeath: found a match at position ' +str(tempinteger) + \
##							     '; unique_id='+str(rbrasga_unique_id), flush=True)
##							w += wstatusprefix
##
##						tempstring = b'\xfb\x00\x00\x00?\x00\x01\xf3\x02\xfd\x00\x02\xf4b\xc8\xf5h\x00\x04b\x00i'
##						tempinteger = bsafecopy.find(tempstring)
##						if tempinteger > (-1):
##							rbrasga_start = tempinteger + \
##									len(tempstring)
##							rbrasga_unique_id = bsafecopy[rbrasga_start:rbrasga_start+4]
##							w += b'rbrasga_findCharge: found '+str(tempstring).encode() + \
##							     b' at position ' +str(tempinteger).encode() + b' for data ' + str(bsafecopy).encode() + \
##							     b'; ['+str(rbrasga_start).encode() + b']unique_id='+str(rbrasga_unique_id).encode() + \
##							     b'\r\n'
##							print (wstatusprefix.decode() + 'rbrasga_findCharge: found a match at position ' +str(tempinteger) + \
##							     '; unique_id='+str(rbrasga_unique_id), flush=True)
##							w += wstatusprefix
##
##						tempstring = b'\xfb\x00\x00\x00B\x00\x01\xf3\x04\xc8\x00\x02\xf5h\x00\x04b\x05b\x00b\x04z\x00\x04b'
##						tempinteger = bsafecopy.find(tempstring)
##						if tempinteger > (-1):
##							rbrasga_start = tempinteger + \
##									len(tempstring)
##							rbrasga_unique_id = bsafecopy[rbrasga_start+30:rbrasga_start+30+4]
##							w += b'rbrasga_findOppCharge: found '+str(tempstring).encode() + \
##							     b' at position ' +str(tempinteger).encode() + b' for data ' + str(bsafecopy).encode() + \
##							     b'; ['+str(rbrasga_start+30).encode() + b']unique_id='+str(rbrasga_unique_id).encode() + \
##							     b'\r\n'
##							print (wstatusprefix.decode() + 'rbrasga_findOppCharge: found a match at position ' +str(tempinteger) + \
##							     '; unique_id='+str(rbrasga_unique_id), flush=True)
##							w += wstatusprefix
						###

						packetlen = int.from_bytes(b[1:5], 'big')
						bsafecopy = b[:packetlen]
						
						w += s[:s.rindex(b'\t')+1]
						if len(b[1:5]) != 4 or len(b[:int.from_bytes(b[1:5], 'big')]) != int.from_bytes(b[1:5], 'big'):
							w += b'/*** truncated ***/ \r\n'
							d.update({stream:b})
							break
						wi = len(w)

						photon_packet_data_5_7 = bsafecopy[5:7]
						photon_packet_data_7_9 = bsafecopy[7:9]

						if photon_packet_data_7_9 == b'\xf3\x02' \
						   or photon_packet_data_7_9 == b'\xf3\x03' \
						   or photon_packet_data_7_9 == b'\xf3\x04':
							w += b'/* Command ' + bsafecopy[5:9].hex().encode() + b' */ ' + repr(bsafecopy[:5]).encode()
							w += b' + ' + repr(photon_packet_data_5_7).encode() + b' + ' + repr(photon_packet_data_7_9).encode() + b'\r\n' 
							j = 0
							photon_packet_i_9 = 0
							skip_photon_param = False
							while (9+photon_packet_i_9+3+j) <= packetlen:
								photon_packet_data_9i0_9i1 = bsafecopy[9+photon_packet_i_9+0+j:9+photon_packet_i_9+1+j]
								photon_packet_data_9i1_9i3 = bsafecopy[9+photon_packet_i_9+1+j:9+photon_packet_i_9+3+j]
								w += b' + ' + repr(photon_packet_data_9i0_9i1).encode() + b' + ' + repr(photon_packet_data_9i1_9i3).encode() + b'\r\n'
##								if not ((9+photon_packet_i_9+3+j) < packetlen):
##									break
								photon_packet_signed_integer_9i1_9i3 = int.from_bytes(photon_packet_data_9i1_9i3, "big", signed=True)
								if photon_packet_signed_integer_9i1_9i3 < 0 or photon_packet_signed_integer_9i1_9i3 > 16384:
									photon_packet_signed_integer_9i1_9i3 = 1
									skip_photon_param = True
								photon_packet_i_9 += 3
								jj = 0
								while ((9+photon_packet_i_9+j) <= packetlen) and (jj < photon_packet_signed_integer_9i1_9i3):
									sppdparam = b''
									if not skip_photon_param:
										sppdparamdata = bsafecopy[9+photon_packet_i_9+0+j:9+photon_packet_i_9+1+j]
										sppdparam = repr(sppdparamdata).encode()
										if sppdparamdata in photonparameters:
											sppdparam = photonparameters[sppdparamdata] + b' ' + sppdparam
										w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
										photon_packet_i_9 += 1
									(ja, haskeys, bsafecopy, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, bsafecopy, 9+photon_packet_i_9, j, w, splitindex, wi, d, stream, True, wstatusprefix))
									(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, sppdparam, elem, csvfile, 0, characterinstances, w, wstatusprefix))
									w += b'\r\n'
									jj += 1
									if skip_photon_param:
										break
								if skip_photon_param:
									break
							if (9+photon_packet_i_9+j) < packetlen:
								w += b'/* Unknown data of length ' + str(packetlen-(9+photon_packet_i_9+j)).encode() + b' */ ' + repr(bsafecopy[(9+photon_packet_i_9+j):]).encode() + b'\r\n'
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue	
##						elif b[5:12] == b'\x00\x01\xf3\x02\xfe\x00\x00':
##							w += b'/* Command A0 */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:12]).encode()
##							w += b'\r\n'
##							j = 0
##							if b[12+j:]:
##								temp = b[12+j:]
##								b = temp[:]
##								continue
##						elif b[5:12] == b'\x00\x01\xf3\x04\xe6\x00\x01'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xe5\x00\x01'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xe6\x00\x01'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xe2\x00\x01'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xde\x00\x01':
##							w += b'/* Command ' + b[5:12].hex().encode() + b' */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:12]).encode() + b'\r\n' 
##							#1
##							sppdparam = repr(b[12:13]).encode()
##							if b[12:13] in photonparameters:
##								sppdparam = photonparameters[b[12:13]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 13, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, sppdparam, elem, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[13+j:]:
##								temp = b[13+j:]
##								b = temp[:]
##								continue
##						elif b[5:12] == b'\x00\x00\xf3\x02\xfd\x00\x02'\
##						or b[5:12] == b'\x00\x00\xf3\x04\xc9\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xc8\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xca\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xfd\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xe5\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xe3\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xfc\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xfe\x00\x02'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xd1\x00\x02':
##							w += b'/* Command ' + b[5:12].hex().encode() + b' */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:12]).encode()
##							w += b'\r\n' 
##							#1
##							sppdparam = repr(b[12:13]).encode()
##							if b[12:13] in photonparameters:
##								sppdparam = photonparameters[b[12:13]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 13, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1= elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#2
##							sppdparam = repr(b[13+j:14+j]).encode()
##							if b[13+j:14+j] in photonparameters:
##								sppdparam = photonparameters[b[13+j:14+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 14, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 1, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[14+j:]:
##								temp = b[14+j:]
##								b = temp[:]
##								continue
##						elif b[5:12] == b'\x00\x01\xf3\x02\xfc\x00\x03'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xfd\x00\x03'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xff\x00\x03'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xfd\x00\x03'\
##						or b[5:12] == b'\x00\x00\xf3\x04\xe2\x00\x03'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xe2\x00\x03'\
##						or b[5:12] == b'\x00\x01\xf3\x04\xfe\x00\x03'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xe3\x00\x03':
##							w += b'/* Command ' + b[5:12].hex().encode() + b' */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:12]).encode()
##							w += b'\r\n' 
##							#1
##							sppdparam = repr(b[12:13]).encode()
##							if b[12:13] in photonparameters:
##								sppdparam = photonparameters[b[12:13]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 13, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#2
##							sppdparam = repr(b[13+j:14+j]).encode()
##							if b[13+j:14+j] in photonparameters:
##								sppdparam = photonparameters[b[13+j:14+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 14, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#3
##							sppdparam = repr(b[14+j:15+j]).encode()
##							if b[14+j:15+j] in photonparameters:
##								sppdparam = photonparameters[b[14+j:15+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 15, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem3 = elem
##							csvsppdparam3 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam3, csvelem3, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[15+j:]:
##								temp = b[15+j:]
##								b = temp[:]
##								continue
##						elif b[5:12] == b'\x00\x01\xf3\x02\xfd\x00\x04'\
##						or b[5:12] == b'\x00\x01\xf3\x02\xe1\x00\x04':
##							w += b'/* Command ' + b[5:12].hex().encode() + b' */ ' + repr(b[:5+j]).encode()
##							w += b' + ' + repr(b[5:12]).encode()
##							w += b'\r\n' 
##							#1
##							sppdparam = repr(b[12:13]).encode()
##							if b[12:13] in photonparameters:
##								sppdparam = photonparameters[b[12:13]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 13, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#2
##							sppdparam = repr(b[13+j:14+j]).encode()
##							if b[13+j:14+j] in photonparameters:
##								sppdparam = photonparameters[b[13+j:14+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 14, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 2, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#3
##							sppdparam = repr(b[14+j:15+j]).encode()
##							if b[14+j:15+j] in photonparameters:
##								sppdparam = photonparameters[b[14+j:15+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 15, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem3 = elem
##							csvsppdparam3 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam3, csvelem3, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#4
##							sppdparam = repr(b[15+j:16+j]).encode()
##							if b[15+j:16+j] in photonparameters:
##								sppdparam = photonparameters[b[15+j:16+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 16, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem4 = elem
##							csvsppdparam4 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam4, csvelem4, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[16+j:]:
##								temp = b[16+j:]
##								b = temp[:]
##								continue
##						elif b[5:12] == b'\x00\x01\xf3\x02\xe3\x00\t':
##							w += b'/* Command A9 send opponents profile id and own data */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:12]).encode()
##							w += b'\r\n' 
##							#1
##							sppdparam = repr(b[12:13]).encode()
##							if b[12:13] in photonparameters:
##								sppdparam = photonparameters[b[12:13]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 13, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#2
##							sppdparam = repr(b[13+j:14+j]).encode()
##							if b[13+j:14+j] in photonparameters:
##								sppdparam = photonparameters[b[13+j:14+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 14, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#3
##							sppdparam = repr(b[14+j:15+j]).encode()
##							if b[14+j:15+j] in photonparameters:
##								sppdparam = photonparameters[b[14+j:15+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 15, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem3 = elem
##							csvsppdparam3 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam3, csvelem3, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#4
##							sppdparam = repr(b[15+j:16+j]).encode()
##							if b[15+j:16+j] in photonparameters:
##								sppdparam = photonparameters[b[15+j:16+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 16, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem4 = elem
##							csvsppdparam4 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam4, csvelem4, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#5
##							sppdparam = repr(b[16+j:17+j]).encode()
##							if b[16+j:17+j] in photonparameters:
##								sppdparam = photonparameters[b[16+j:17+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 17, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem5 = elem
##							csvsppdparam5 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam5, csvelem5, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#6
##							sppdparam = repr(b[17+j:18+j]).encode()
##							if b[17+j:18+j] in photonparameters:
##								sppdparam = photonparameters[b[17+j:18+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 18, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem6 = elem
##							csvsppdparam6 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam6, csvelem6, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#7
##							sppdparam = repr(b[18+j:19+j]).encode()
##							if b[18+j:19+j] in photonparameters:
##								sppdparam = photonparameters[b[18+j:19+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 19, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem7 = elem
##							csvsppdparam7 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam7, csvelem7, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#8
##							sppdparam = repr(b[19+j:20+j]).encode()
##							if b[19+j:20+j] in photonparameters:
##								sppdparam = photonparameters[b[19+j:20+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 20, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem8 = elem
##							csvsppdparam8 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam8, csvelem8, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n' 
##							#9
##							sppdparam = repr(b[20+j:21+j]).encode()
##							if b[20+j:21+j] in photonparameters:
##								sppdparam = photonparameters[b[20+j:21+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 21, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem9 = elem
##							csvsppdparam9 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam9, csvelem9, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[21+j:]:
##								temp = b[21+j:]
##								b = temp[:]
##								continue
##						elif b[5:15] == b'\x00\x01\xf3\x03\xe6\x00\x00*\x00\x00'\
##						or b[5:15] == b'\x00\x01\xf3\x03\xfc\x00\x00*\x00\x00'\
##						or b[5:15] == b'\x00\x01\xf3\x03\xe5\x00\x00*\x00\x00'\
##						or b[5:15] == b'\x00\x01\xf3\x03\xfe\x00\x00*\x00\x00':
##							w += b'/* Command B0 */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:15]).encode()
##							w += b'\r\n'
##							j = 0
##							if b[15+j:]:
##								temp = b[15+j:]
##								b = temp[:]
##								continue
##						elif b[5:15] == b'\x00\x01\xf3\x03\xe6\x00\x00*\x00\x02'\
##						or b[5:15] == b'\x00\x01\xf3\x03\xde\x00\x00*\x00\x02':
##							w += b'/* Command ' + b[5:15].hex().encode() + b' */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:15]).encode()
##							w += b'\r\n'
##							#1
##							sppdparam = repr(b[15:16]).encode()
##							if b[15:16] in photonparameters:
##								sppdparam = photonparameters[b[15:16]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 16, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#2
##							sppdparam = repr(b[16+j:17+j]).encode()
##							if b[16+j:17+j] in photonparameters:
##								sppdparam = photonparameters[b[16+j:17+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 17, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[17+j:]:
##								temp = b[17+j:]
##								b = temp[:]
##								continue
##						elif b[5:15] == b'\x00\x01\xf3\x03\xe3\x00\x00*\x00\x03'\
##						or b[5:15] == b'\x00\x01\xf3\x03\xe2\x00\x00*\x00\x03':
##							w += b'/* Command ' + b[5:15].hex().encode() + b' */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:15]).encode()
##							w += b'\r\n'
##							#1
##							sppdparam = repr(b[15:16]).encode()
##							if b[15:16] in photonparameters:
##								sppdparam = photonparameters[b[15:16]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 16, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#2
##							sppdparam = repr(b[16+j:17+j]).encode()
##							if b[16+j:17+j] in photonparameters:
##								sppdparam = photonparameters[b[16+j:17+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 17, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#3
##							sppdparam = repr(b[17+j:18+j]).encode()
##							if b[17+j:18+j] in photonparameters:
##								sppdparam = photonparameters[b[17+j:18+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 18, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem3 = elem
##							csvsppdparam3 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam3, csvelem3, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[18+j:]:
##								temp = b[18+j:]
##								b = temp[:]
##								continue
##						elif b[5:15] == b'\x00\x01\xf3\x03\xe1\x00\x00*\x00\x04' or \
##						     b[5:15] == b'\x00\x01\xf3\x03\xe2\x00\x00*\x00\x04':
##							w += b'/* Command B4 */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:15]).encode()
##							w += b'\r\n'
##							#1
##							sppdparam = repr(b[15:16]).encode()
##							if b[15:16] in photonparameters:
##								sppdparam = photonparameters[b[15:16]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 16, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#2
##							sppdparam = repr(b[16+j:17+j]).encode()
##							if b[16+j:17+j] in photonparameters:
##								sppdparam = photonparameters[b[16+j:17+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 17, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#3
##							sppdparam = repr(b[17+j:18+j]).encode()
##							if b[17+j:18+j] in photonparameters:
##								sppdparam = photonparameters[b[17+j:18+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 18, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem3 = elem
##							csvsppdparam3 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam3, csvelem3, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#4
##							sppdparam = repr(b[18+j:19+j]).encode()
##							if b[18+j:19+j] in photonparameters:
##								sppdparam = photonparameters[b[18+j:19+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 19, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem4 = elem
##							csvsppdparam4 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam4, csvelem4, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[19+j:]:
##								temp = b[19+j:]
##								b = temp[:]
##								continue
##						elif b[5:15] == b'\x00\x01\xf3\x03\xe3\x00\x00*\x00\x05':
##							w += b'/* Command B5 receive own data */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:15]).encode()
##							w += b'\r\n'
##							#1
##							sppdparam = repr(b[15:16]).encode()
##							if b[15:16] in photonparameters:
##								sppdparam = photonparameters[b[15:16]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 16, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#2
##							sppdparam = repr(b[16+j:17+j]).encode()
##							if b[16+j:17+j] in photonparameters:
##								sppdparam = photonparameters[b[16+j:17+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 17, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#3
##							sppdparam = repr(b[17+j:18+j]).encode()
##							if b[17+j:18+j] in photonparameters:
##								sppdparam = photonparameters[b[17+j:18+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 18, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem3 = elem
##							csvsppdparam3 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam3, csvelem3, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#4
##							sppdparam = repr(b[18+j:19+j]).encode()
##							if b[18+j:19+j] in photonparameters:
##								sppdparam = photonparameters[b[18+j:19+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 19, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem4 = elem
##							csvsppdparam4 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam4, csvelem4, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#5
##							sppdparam = repr(b[19+j:20+j]).encode()
##							if b[19+j:20+j] in photonparameters:
##								sppdparam = photonparameters[b[19+j:20+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 20, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem5 = elem
##							csvsppdparam5 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam5, csvelem5, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[20+j:]:
##								temp = b[20+j:]
##								b = temp[:]
##								continue
##						elif b[5:15] == b'\x00\x01\xf3\x03\xe2\x00\x00*\x00\x06':
##							w += b'/* Command B6 receive opponents data */ ' + repr(b[:5]).encode()
##							w += b' + ' + repr(b[5:15]).encode()
##							w += b'\r\n'
##							#1
##							sppdparam = repr(b[15:16]).encode()
##							if b[15:16] in photonparameters:
##								sppdparam = photonparameters[b[15:16]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 16, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem1 = elem
##							csvsppdparam1 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam1, csvelem1, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#2
##							sppdparam = repr(b[16+j:17+j]).encode()
##							if b[16+j:17+j] in photonparameters:
##								sppdparam = photonparameters[b[16+j:17+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 17, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem2 = elem
##							csvsppdparam2 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam2, csvelem2, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#3
##							sppdparam = repr(b[17+j:18+j]).encode()
##							if b[17+j:18+j] in photonparameters:
##								sppdparam = photonparameters[b[17+j:18+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 18, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem3 = elem
##							csvsppdparam3 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam3, csvelem3, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#4
##							sppdparam = repr(b[18+j:19+j]).encode()
##							if b[18+j:19+j] in photonparameters:
##								sppdparam = photonparameters[b[18+j:19+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 19, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem4 = elem
##							csvsppdparam4 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam4, csvelem4, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#5
##							sppdparam = repr(b[19+j:20+j]).encode()
##							if b[19+j:20+j] in photonparameters:
##								sppdparam = photonparameters[b[19+j:20+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 20, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem5 = elem
##							csvsppdparam5 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam5, csvelem5, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							#6
##							sppdparam = repr(b[20+j:21+j]).encode()
##							if b[20+j:21+j] in photonparameters:
##								sppdparam = photonparameters[b[20+j:21+j]] + b' ' + sppdparam
##							w += wstatusprefix + b'/* Param */ ' + sppdparam + b' '
##							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 21, j, w, splitindex, wi, d, stream, True, wstatusprefix))
##	##								if stream in d:
##	##									break
##							csvelem6 = elem
##							csvsppdparam6 = sppdparam
##							(csvpackettime, csvstream, csvcommandparam, csvelem, csvfile, csvtype, characterinstances, w, wstatusprefix) = logelementtocsv((csvpackettime, csvstream, csvsppdparam6, csvelem6, csvfile, 0, characterinstances, w, wstatusprefix))
##							w += b'\r\n'
##							if b[21+j:]:
##								temp = b[21+j:]
##								b = temp[:]
##								continue
						elif b[5:9] == b'\x00\x01\xf3\x82' or b[5:9] == b'\x00\x01\xf3\x83':
							w += b'/* Command C */ ' + repr(b[:5]).encode()
							w += b'/* Param 1 */ ' + repr(b[5:9]).encode()
							packetlen = int.from_bytes(b[1:5], 'big')
							w += b'/* Param 2 data of length ' + str(packetlen-9).encode() + b' */ ' + repr(b[9:packetlen]).encode() + b'\r\n'
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue
						elif b[5:18] == b'\x00\x01\xf3\x06\x00\x00\x01\x01x\x00\x00\x00`':
							w += b'/* Command C3 */ ' + repr(b[:5]).encode()
							w += b'/* Param 1 */ ' + repr(b[5:18]).encode()
							packetlen = int.from_bytes(b[1:5], 'big')
							w += b'/* Param 2 data of length ' + str(packetlen-18).encode() + b' */ ' + repr(b[18:packetlen]).encode() + b'\r\n'
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue
						elif b[5:21] == b'\x00\x01\xf3\x07\x00\x00\x00*\x00\x01\x01x\x00\x00\x00`':
							w += b'/* Command C4 */ ' + repr(b[:5]).encode()
							w += b'/* Param 1 */ ' + repr(b[5:21]).encode()
							packetlen = int.from_bytes(b[1:5], 'big')
							w += b'/* Param 2 data of length ' + str(packetlen-21).encode() + b' */ ' + repr(b[21:packetlen]).encode() + b'\r\n'
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue
						elif b[5:16] == b'\x00\x01\xf3\x00\x01\x06\x1eA\x01\x11\x00':
							w += b'/* Command D */ ' + repr(b[:5]).encode()
							w += b'/* Param 1 */ ' + repr(b[5:16]).encode()
							packetlen = int.from_bytes(b[1:5], 'big')
							w += b'/* Param 2 data of length ' + str(packetlen-16).encode() + b' */ ' + repr(b[16:packetlen]).encode() + b'\r\n'
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue
						elif b[5:12] == b'\x00\x01\xf3\x03\xe1\x7f\xf8' \
						     or b[5:12] == b'\x00\x01\xf3\x03\xfc\xff\xfe':
							w += b'/* Command E matchmaking message */ ' + repr(b[:5]).encode()
							w += b'/* Param 1 */ ' + repr(b[5:12]).encode()
							packetlen = int.from_bytes(b[1:5], 'big')
							w += b'/* Param 2 string */ '
							(ja, haskeys, b, jbase, j, w, splitindex, wi, d, stream, elem, wstatusprefix) = processelement((1, False, b, 12, j, w, splitindex, wi, d, stream, True, wstatusprefix))
	##								if stream in d:
	##									break
							w += b'/* Param 2 data of length ' + str(packetlen-(12+j)).encode() + b' */ ' + repr(b[12+j:packetlen]).encode() + b'\r\n'
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue
						elif b[5:10] == b'\x00\x01\xf3\x01\x00':
							w += b'/* Command F */ ' + repr(b[:5]).encode()
							w += b' + ' + repr(b[5:10]).encode() + b'\r\n'
							packetlen = int.from_bytes(b[1:5], 'big')
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue
						else:
							packetlen = int.from_bytes(b[1:5], 'big')
							w += b'/* Unknown command ' + repr(b[5:16]).encode() + b' ??? */ ' + repr(b[:packetlen]).encode() + b'\r\n'
							if b[packetlen:]:
								temp = b[packetlen:]
								b = temp[:]
								continue
					break
				#break goes here
			else:
				w += s + b'\r\n'
		t = param2file.write(w)
		break
	return (csvw, streamfilter, d, characterinstances, csvfile)


def debug_execute_photon_packet(b, photon_server = False):
	
##	def interpretsppd(param1line, param2file, othervariables):
##		(csvw, streamfilter, d, characterinstances, csvfile) = othervariables
##		#param1: output from tshark
##		#csvpackettime0 + b', ' + b'0000 ' + csvpackettimehours + b':' + csvpackettimeminutes + b':' + csvpackettimeseconds + b'\t'
##		# + source + b'\t'
##		# + sourceport + b'\t'
##		# + destination + b'\t'
##		# + destinationport + b'\t' + b.hex().encode()
##		# + b'\r\n'
##		# param2file: file handle
##		# type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})()
##		# csvw: unused
##		# b''
##		# streamfilter: dictionary containing a list of sppd streams
##		# {(b'\t'+source+b'\t'+sourceport+b'\t'+destination+b'\t'+destinationport): (b'Command decoding below\r\n', b'Client')}
##		# d: used in dead code
##		# {}
##		# characterinstances: list of character instance ids
##		# {}
##		# csvfile: used in dead code
##		# type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})()
	if photon_server: 
		(csvw, streamfilter, d, characterinstances, csvfile) = interpretsppd(b'???, 0000 00:00:00 \t0.0.0.0\t4533\t0.0.0.0\t0\t' + \
										     b.hex().encode() + b'\r\n', \
										     type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})(), (\
											     b'', \
											     {(b'\t0.0.0.0\t4533\t0.0.0.0\t0'): (b'Command decoding below\r\n', b'Server')}, \
											     {}, \
											     {}, \
											     type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})()))
	else: 
		(csvw, streamfilter, d, characterinstances, csvfile) = interpretsppd(b'???, 0000 00:00:00 \t0.0.0.0\t0\t0.0.0.0\t4533\t' + \
										     b.hex().encode() + b'\r\n', \
										     type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})(), (\
											     b'', \
											     {(b'\t0.0.0.0\t0\t0.0.0.0\t4533'): (b'Command decoding below\r\n', b'Client')}, \
											     {}, \
											     {}, \
											     type("", (), {"write": (lambda self, b: print(b.decode(), flush=True))})()))
##	print ('streamfilter = ' + repr(streamfilter), flush = True)


def photon_element_key (elem, key):
	value = None
	i = 0
	while i < len(elem[1]):
		key_temp = list(elem[1][i])[0]
		if key_temp == key:
			value = elem[1][i][key]
			break
		i += 1
##	if value == None:
##		raise KeyError(key)
	return value

