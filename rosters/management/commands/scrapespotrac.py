import requests
import time
import re
from BeautifulSoup import BeautifulSoup

teams = ["atlanta-hawks","boston-celtics","brooklyn-nets",
"charlotte-hornets","chicago-bulls","cleveland-cavaliers",
"dallas-mavericks","denver-nuggets","detroit-pistons",
"golden-state-warriors","houston-rockets","indiana-pacers",
"los-angeles-clippers","los-angeles-lakers","memphis-grizzlies",
"miami-heat","milwaukee-bucks","minnesota-timberwolves",
"new-orleans-pelicans","new-york-knicks","oklahoma-city-thunder",
"orlando-magic","philadelphia-76ers","phoenix-suns",
"portland-trail-blazers","sacramento-kings","san-antonio-spurs",
"toronto-raptors","utah-jazz","washington-wizards"]

URL = 'http://www.spotrac.com/nba/{}/cap/'


# URL = 'http://www.spotrac.com/nba/rankings/'

# soup.findAll({'title' : True, 'p' : True})

for t in teams:
	r = requests.get(URL.format(t))
	soup = BeautifulSoup(r.text)
	table = soup.find("table")
	rows = table.findAll('tr')

	for r in rows[1:]:
		try:
			player_name = r.find(attrs={'class':'player'}).a.string
			cap_hit = r.find(title=re.compile('Cap Figure')).string
			print "player {} has a cap hit of {}".format(player_name, cap_hit)
		except (UnicodeEncodeError, UnicodeDecodeError) as e:
			player_name = 'Dennis Schroeder'
			print "player {} has a cap hit of {}".format(player_name, cap_hit)




	# for i in range(0, len(cells)):
	# 	if i % 11 == 0:
	# 		print cells[i].a.string
	# 	if i % 11 == 9:
	# 		print str(int(cells[i].span.string.replace("$","").replace(",","").replace(" ","")))
	time.sleep(2)

# 	# player name
# 	[cells[i].a.string for i in range(0, 165, 11)]

# 	# salary
# 	[cells[i].span.string for i in range(9, 165, 11)]


# # http://www.spotrac.com/assets/images/thumb/lakers.png


# for i in range(0, len(cells)):
# 	# if i % 4 == 1:
# 	# 	print "team {}".format(cells[i].a.img['src'][43:-4])
# 	if i % 4 == 2:
# 		print "player {}".format(cells[i].h3.a.string)
# 	# if i % 4 == 3:
# 		# print "salary {}".format(int(cells[i].span.string.replace("$","").replace(",","").replace(" ","")))


