import pandas as pd 
import requests 
from bs4 import BeautifulSoup

web_url ="https://parsehub.com/sandbox/showtimes"
fetch_page = requests.get(web_url)
soup = BeautifulSoup(fetch_page.text,'html.parser')

titles ,urls ,times = [],[],[]
for i in soup.find_all('a',class_='title'):
    titles.append(i.string)
    urls.append(i.get('href') )

for showtime in soup.find_all('span',class_='showtime'):
    times.append(showtime.string)

raw_data ={
    'movie_title':titles,
    'movie_url':urls
  
}    
df = pd.DataFrame(raw_data)
df.to_csv('scrapped_file.csv',index=False)
print(df)







