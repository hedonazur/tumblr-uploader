import requests
import json
r = requests.get("https://www.youtube.com/user/carolcastillo17/videos?sort=dd&live_view=500&flow=list&view=0")
r.text
data = json.loads(r.text)

# Loop through the result. 
for item in data['data']['items']:
	print "Video Title: %s" % (item['title'])
	print "Embed URL: %s" % (item['player']['default'])
	print