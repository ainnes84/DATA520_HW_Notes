#html-to-list1.py
import requests, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
pagetext = requests.get(url)
HTML = pagetext.text
text = obo.stripTags(HTML).lower()
#wordlist = text.split() # now commented out
wordlist = obo.stripNonAlphaNum(text) # RegEx and split done together

print(wordlist[0:150])
