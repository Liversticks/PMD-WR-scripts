#!
# apiscrape.py - use the sr.c API instead
# 04-28-2020 - shelved indefinitely because I don't want to deal with the sr.c API when my own web scraper is less of a hassle

# DX - nd2e0rrd
# DX any% category ID: ndx9ll5d
# DX any% WM variable ID: 9l716y9l
# DX any% WM flag: zqod85x1
# DX any% no WM flag: 0133o2x1  

# Format:
# GET /api/v1/leaderboards/[GAME ID]/category/[CATEGORY ID]?var-[VARIABLE]=[FLAG]
# This will return a leaderboard object, meaning need to extract the first run
# VARIABLE represents WM/No WM in all games but RT and Unrestricted/No WM/No WM No QS in RT
# FLAG has 2 values (non-RT), three values (RT), or 1 value (WiiWare or Sky All Special Episodes)

import requests
import json
import math
from datetime import datetime


#TODO: make data structures for game id, category id, variables, and flags
# Format: game ID, [list of category IDs], [variable IDs], [lists of flag IDs]
pmdRT = ['k6qwpm6g', [['Any% - ENG', 'mkerqxd6'], ['Any% - JPN', 'jdz7646k'], ['All Icons', 'vdo413o2'], ['Recruit Em All', 'n2y39ezd'], ['Low%', 'zdn48oqk'], ['All Dungeons', 'ndx1y4v2']], ['6nj40pn4'], [['Unrestricted', '814enkld'], ['No WM', '21ddpv51'], ['No WM No QS', 'z19gw4l4']]]

# Time/Darkness game ID: '76r34v68' 
# Time/Darkness ['Any% - ENG', 'xd17grd8'], 'onv6xr08', [['with WM', '9qjzrpo1'], ['no WM', 'jq64m8o1']]

# Time/Darkness ['Any% - JPN', 'zd38omrk'], '789j199n',[['with WM', '21g484n1'], ['no WM', 'jqz5p5gq']]


# Time/Darkness ['Beat Darkrai', '7kj13oxk'], '38djw5e8', [['with WM', '5lm4w98l'], ['no WM', '81wdrkmq']]

# Time/Darkness ['Recruit Em All', 'z27lrwgd'], 'r8roqwr8', [['Unlimited WM', 'zqo3275q'], ['Minimum WM', '013m4yrl']]

# Need to rewrite with separate variables per flag
# Sky game ID: 'j1lqnj6g'
# Sky ['Any% - ENG', '']

# Sky ['Any% - JPN', '']

# Sky ['Beat Darkrai - ENG', '']

# Sky ['Beat Darkrai - JPN', '']

# Sky ['Recruit Em All', '']

# Sky ['All Icons', '']

# Sky ['All Special Episodes', '']

pmdWii = []
# Need to rewrite with separate variables per flag
pmdGates = ['v1pxlz68', [], '', []]
# Need to rewrite with separate variables per flag
pmdSuper = ['76ro4468', [],'', []]
pmdRTDX = ['nd2e0rrd', [['Any% - ENG', 'ndx9ll5d'], ['Any% - JPN', 'jdz90432'], ['All Icons', 'xk9r14yk']], '9l716y9l', [['With WM', 'zqod85x1'], ['No WM', '0133o2x1']]]


for test in test:
	#formatted string
	address = 
	apiData = json.loads(requests.get(address).text)
	
	
	#TODO: parse run information for runner name (need to do a separate lookup based on the ID) and time (need to convert from primary_t, which represents only seconds)
	
	preConvertTime = int(apiData['data']['runs'][0]['run']['times']['primary_t'])
	hours = math.floor(preConvertTime/3600)
	preConvertTime -= (hours * 3600)
	minutes = math.floor(preConvertTime/60)
	seconds = preConvertTime - (minutes * 60)
	
	formatTime = (str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's ')

#TODO: write this shit to a file with markdown
#format: [CATEGORY]: [TIME] by [RUNNER]