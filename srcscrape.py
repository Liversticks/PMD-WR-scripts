# srcscrape.py
# Obtains WR times and runner names from sr.c
# BETA 1.0: Formats information as README

# Oliver X. (Liversticks)

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

# Leaderboards are normally dynamically generated. However, they can be accessed via below static pages:

# Blue Rescue Team and Red Rescue Team

# any%, No WM No QS
rtENGanySS = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6868&game=pmdredblue&verified=1&category=3035&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# any%, No WM
rtENGanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=94552&game=pmdredblue&verified=1&category=3035&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# any%, Unrestricted
rtENGanyUR = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6867&game=pmdredblue&verified=1&category=3035&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# any% JPN, No WM No QS
rtJPNanySS = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6868&game=pmdredblue&verified=1&category=88521&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# any% JPN, No WM
rtJPNanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=94552&game=pmdredblue&verified=1&category=88521&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# any% JPN, Unrestricted
rtJPNanyUR = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6867&game=pmdredblue&verified=1&category=88521&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# All Icons, No WM No QS
rtENGiconsSS = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6868&game=pmdredblue&verified=1&category=32380&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# All Icons, No WM
rtENGiconsNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=94552&game=pmdredblue&verified=1&category=32380&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# All Icons, Unrestricted
rtENGiconsUR = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6867&game=pmdredblue&verified=1&category=32380&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# REA, No WM No QS
rtENGreaSS = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6868&game=pmdredblue&verified=1&category=74562&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# REA, No WM
rtENGreaNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=94552&game=pmdredblue&verified=1&category=74562&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# REA, Unrestricted
rtENGreaUR = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6867&game=pmdredblue&verified=1&category=74562&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# Low%, Unrestricted
rtENGlowUR = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6867&game=pmdredblue&verified=1&category=60218&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='
# All Dungeons, No WM No QS
rtENGadSS = 'https://www.speedrun.com/ajax_leaderboard.php?variable2121=6868&game=pmdredblue&verified=1&category=69329&region=&platform=&variable251=&emulator=0&video=&obsolete=&date='

# Explorers of Time and Explorers of Darkness

# any%, WM
tdENGanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64433&variable30535=102484&variable30536=102486&variable31003=104426&game=pmdtimedarkness&verified=1&category=3049&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='
# any%, no WM
tdENGanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64434&variable30535=102484&variable30536=102486&variable31003=104426&game=pmdtimedarkness&verified=1&category=3049&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='
# any% JPN, WM
tdJPNanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64434&variable30535=102484&variable30536=102486&variable31003=104425&game=pmdtimedarkness&verified=1&category=88526&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='
# any% JPN, no WM
tdJPNanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64434&variable30535=102484&variable30536=102486&variable31003=104426&game=pmdtimedarkness&verified=1&category=88526&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='
# Darkrai, WM
tdENGdarkWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64434&variable30535=102483&variable30536=102486&variable31003=104425&game=pmdtimedarkness&verified=1&category=87239&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='
# Darkrai, no WM
tdENGdarkNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64434&variable30535=102484&variable30536=102486&variable31003=104425&game=pmdtimedarkness&verified=1&category=87239&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='
# REA, unlimited WM
tdENGreaUW = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64434&variable30535=102483&variable30536=102485&variable31003=104425&game=pmdtimedarkness&verified=1&category=87241&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='
# REA, minimum WM
tdENGreaMW = 'https://www.speedrun.com/ajax_leaderboard.php?variable19600=64434&variable30535=102483&variable30536=102486&variable31003=104425&game=pmdtimedarkness&verified=1&category=87241&region=&platform=&variable6446=&emulator=0&video=&obsolete=&date='

# Explorers of Sky

# any%, WM
skyENGanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65386&variable22018=72935&variable27650=93444&variable31004=104428&variable37354=126157&game=pmdsky&verified=1&category=3050&region=&platform=&emulator=0&video=&obsolete=&date='
# any%, no WM
skyENGanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50768&variable19867=65386&variable22018=72935&variable27650=93444&variable31004=104428&variable37354=126157&game=pmdsky&verified=1&category=3050&region=&platform=&emulator=0&video=&obsolete=&date='
# any% JPN, WM
skyJPNanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65386&variable22018=72935&variable27650=93444&variable31004=104427&variable37354=126157&game=pmdsky&verified=1&category=88527&region=&platform=&emulator=0&video=&obsolete=&date='
# any% JPN, no WM
skyJPNanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65386&variable22018=72935&variable27650=93444&variable31004=104428&variable37354=126157&game=pmdsky&verified=1&category=88527&region=&platform=&emulator=0&video=&obsolete=&date='
# Darkrai, WM
skyENGdarkWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65386&variable22018=72935&variable27650=93444&variable31004=104427&variable37354=126157&game=pmdsky&verified=1&category=48164&region=&platform=&emulator=0&video=&obsolete=&date='
# Darkrai, no WM
skyENGdarkNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72935&variable27650=93444&variable31004=104427&variable37354=126157&game=pmdsky&verified=1&category=48164&region=&platform=&emulator=0&video=&obsolete=&date='
# Darkrai JPN, WM
skyJPNdarkWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72935&variable27650=93444&variable31004=104427&variable37354=126156&game=pmdsky&verified=1&category=98801&region=&platform=&emulator=0&video=&obsolete=&date='
# Darkrai JPN, no WM
skyJPNdarkNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72935&variable27650=93444&variable31004=104427&variable37354=126157&game=pmdsky&verified=1&category=98801&region=&platform=&emulator=0&video=&obsolete=&date='
# REA, WM
skyENGreaWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72935&variable27650=93444&variable31004=104427&variable37354=126156&game=pmdsky&verified=1&category=82042&region=&platform=&emulator=0&video=&obsolete=&date='
# REA, no WM
skyENGreaNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72935&variable27650=93445&variable31004=104427&variable37354=126156&game=pmdsky&verified=1&category=82042&region=&platform=&emulator=0&video=&obsolete=&date='
# All Icons, WM
skyENGiconsWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72935&variable27650=93445&variable31004=104427&variable37354=126156&game=pmdsky&verified=1&category=71260&region=&platform=&emulator=0&video=&obsolete=&date='
# All Icons, no WM
skyENGiconsNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72936&variable27650=93445&variable31004=104427&variable37354=126156&game=pmdsky&verified=1&category=71260&region=&platform=&emulator=0&video=&obsolete=&date='
# All Special Episodes
skyENGase = 'https://www.speedrun.com/ajax_leaderboard.php?variable15249=50769&variable19867=65385&variable22018=72936&variable27650=93445&variable31004=104427&variable37354=126156&game=pmdsky&verified=1&category=18548&region=&platform=&emulator=0&video=&obsolete=&date='

# WiiWare
wiiJPNany = 'https://www.speedrun.com/ajax_leaderboard.php?game=pmdwii&verified=1&category=6565&region=&platform=&variable593=&emulator=2&video=&obsolete=&date='

# Gates to Infinity

# any%, WM
gtiENGanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable37118=125354&variable40725=139147&variable40726=139148&game=pmdgti&verified=1&category=3045&region=&platform=&emulator=0&video=&obsolete=&date='
# any%, no WM
gtiENGanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable37118=125355&variable40725=139147&variable40726=139148&game=pmdgti&verified=1&category=3045&region=&platform=&emulator=0&video=&obsolete=&date='
# any% JPN, WM
gtiJPNanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable37118=125354&variable40725=139146&variable40726=139148&game=pmdgti&verified=1&category=88528&region=&platform=&emulator=0&video=&obsolete=&date='
# any% JPN, no WM
gtiJPNanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable37118=125354&variable40725=139147&variable40726=139148&game=pmdgti&verified=1&category=88528&region=&platform=&emulator=0&video=&obsolete=&date='
# REA, WM
gtiENGreaWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable37118=125354&variable40725=139146&variable40726=139148&game=pmdgti&verified=1&category=91144&region=&platform=&emulator=0&video=&obsolete=&date='
# REA, no WM
gtiENGreaNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable37118=125354&variable40725=139146&variable40726=139149&game=pmdgti&verified=1&category=91144&region=&platform=&emulator=0&video=&obsolete=&date='

# Super Mystery Dungeon

# any%, WM
smdENGanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable24326=81503&variable24328=81505&variable31005=104429&game=psmd&verified=1&category=19402&region=&platform=&emulator=2&video=&obsolete=&date='
# any%, no WM
smdENGanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable24326=81504&variable24328=81505&variable31005=104429&game=psmd&verified=1&category=19402&region=&platform=&emulator=2&video=&obsolete=&date='
# any% JPN, WM
smdJPNanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable24326=81503&variable24328=81505&variable31005=104429&game=psmd&verified=1&category=88529&region=&platform=&emulator=2&video=&obsolete=&date='
# any% JPN, no WM
smdJPNanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable24326=81503&variable24328=81505&variable31005=104430&game=psmd&verified=1&category=88529&region=&platform=&emulator=2&video=&obsolete=&date='
# 100%, WM
smdENG100WM = 'https://www.speedrun.com/ajax_leaderboard.php?variable24326=81503&variable24328=81505&variable31005=104430&game=psmd&verified=1&category=75625&region=&platform=&emulator=2&video=&obsolete=&date='
# as of now no 100%, no WM category exists

# Rescue Team DX

# any%, WM
rtdxENGanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable40519=138361&game=pmddx&verified=1&category=105777&platform=&variable40520=&emulator=0&video=&obsolete=&date='
# any%, no WM
rtdxENGanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable40519=138362&game=pmddx&verified=1&category=105777&platform=&variable40520=&emulator=0&video=&obsolete=&date='
# any% JPN, WM
rtdxJPNanyWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable40519=138361&game=pmddx&verified=1&category=105793&platform=&variable40520=&emulator=0&video=&obsolete=&date='
# any% JPN, no WM
rtdxJPNanyNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable40519=138362&game=pmddx&verified=1&category=105793&platform=&variable40520=&emulator=0&video=&obsolete=&date='
# All Icons, WM
rtdxENGiconsWM = 'https://www.speedrun.com/ajax_leaderboard.php?variable40519=138361&game=pmddx&verified=1&category=105888&platform=&variable40520=&emulator=0&video=&obsolete=&date='
# All Icons, no WM
rtdxENGiconsNW = 'https://www.speedrun.com/ajax_leaderboard.php?variable40519=138362&game=pmddx&verified=1&category=105888&platform=&variable40520=&emulator=0&video=&obsolete=&date='
