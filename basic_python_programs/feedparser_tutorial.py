import json
import feedparser

data = feedparser.parse('https://www.esakal.com/c14-feeds.xml')
entries = data['entries']
list1 = []


def get_latest_news():
	for i in entries:
		temp_dict = {'news_title': i['title']}
		print(temp_dict)
		list1.append(temp_dict)
	return list1


get_latest_news()

# list2 = get_latest_news()
#
# dumped = json.dumps(list2, indent=4)
# print(dumped)
