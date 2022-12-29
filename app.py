from requests_html import HTMLSession
import pandas as pd
url = 'https://www.digitaltrends.com/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

master_list =[]

session = HTMLSession()

res = session.get(url,headers=headers)

articles = res.html.find('div.b-river-post__content') #list

for article in articles:

	h3_tag = article.find('h3.b-river-post__title.dt-clamp.dt-clamp-4',first=True).text.strip()
	title_link = article.find('a',first=True).attrs['href']
	try:
		summary = article.find('div.b-river-post__excerpt',first=True).text.strip()
	except:
		summary= "None"
	master_list.append({'title':h3_tag,'url':title_link,'summary':summary})

print(f'Numbers of post scraped {len(master_list)}')

df = pd.DataFrame(master_list)
df.to_csv('digitaltrends.csv',index=False,encoding="utf-8")
print(df)