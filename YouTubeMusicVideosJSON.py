import requests
import datetime
from bs4 import BeautifulSoup
import json

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape YouTube with requests
url = 'https://www.youtube.com/results?q=music+video&sp=CAMSAggF'

parse = True
i = 1

#Parse YouTube url
#while parse == True:
while i < 2:
    page = requests.get(url)
    # Prepare for parsing YouTube with BeautifulSoup
    soup = BeautifulSoup(page.content, 'lxml')

    # parse each page

    for position in soup.find_all('div', class_='yt-lockup-dismissable yt-uix-tile'):
        badposition = soup.find('ul', class_='shelf-content')
        if position.parent.parent.parent != badposition:
            title = position.find('h3', class_='yt-lockup-title ').find('a').string
            length = position.find('span', class_='accessible-description').string.split('Duration: ')[1].split('.')[0]
            videoLink = 'https://www.youtube.com' + position.find('h3', class_='yt-lockup-title ').find('a').get('href')
            uploaded = position.find('ul', class_='yt-lockup-meta-info').find('li').string
            views = position.find('ul', class_='yt-lockup-meta-info').find('li').next_sibling.string.split(' views')[0]
            channel = position.find('div', class_='yt-lockup-byline ').find('a').string
            channelLink = 'https://www.youtube.com' + position.find('div', class_='yt-lockup-byline ').find('a').get('href')

            # Make changes to response
            response.append({'Title': title, 'Video Link': videoLink, 'Duration': length, 'Uploaded': uploaded, 'Views': views,
                     'Channel': channel, 'Channel Link': channelLink})
    parse = False
    for nextPosition in soup.find_all('span', class_='yt-uix-button-content'):
        if nextPosition.string == 'Next »':
            url = 'https://www.youtube.com/' + nextPosition.parent.get('href')
            parse = True
            i += 1
            # print(i)


# Write response to JSON file
today= str(datetime.datetime.now().date())
postingsFile = '/Users/Alex/SCHOOLJUNIOR/CSC3130/WebProject_alexyq/' + today + '.YouTubeMusicVideos.json'

#Write response to JSON file in another location
#postingsFile = '/YouTube/' + today + '.YouTubeMusicVideos.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()
