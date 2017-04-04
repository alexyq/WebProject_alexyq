import requests
from bs4 import BeautifulSoup

# Scrape YouTube with requests
#url = 'https://www.youtube.com/results?sp=CAMSAggF&q=music+video'
url = 'https://www.youtube.com/results?q=music+video&sp=CAMSAggF'
page = requests.get(url)

# Prepare for parsing YouTube with BeautifulSoup
soup = BeautifulSoup(page.content, 'lxml')

position = soup.find('div', class_='yt-lockup-dismissable yt-uix-tile')
badposition = soup.find('ul', class_='shelf-content')
if position.parent.parent != badposition:
    title = position.find('h3', class_='yt-lockup-title ').find('a').string
    length = position.find('span', class_='accessible-description').string.split('Duration: ')[1].split('.')[0]
    videoLink = 'https://www.youtube.com' + position.find('h3', class_='yt-lockup-title ').find('a').get('href')
    uploaded = position.find('ul', class_='yt-lockup-meta-info').find('li').string
    views = position.find('ul', class_='yt-lockup-meta-info').find('li').next_sibling.string.split(' views')[0]
    channel = position.find('div', class_='yt-lockup-byline ').find('a').string
    channelLink = 'https://www.youtube.com' + position.find('div', class_='yt-lockup-byline ').find('a').get('href')
#description = position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').next_element +\
     #         position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').next_element + \
    #          position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').next_element.next_element
##description = ''
##if position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').next_element:
   ## description = position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').next_element
    ##if position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').next_element:
       ## for nextPosition in soup.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a'):
        ##    description = description + nextPosition.next_element
    ##description = description + position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').get('href')
    ##description = description + position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').next_element.next_element
    #description = description + position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').find('a').get('href')
    #description = description + position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').next_sibling.next_element
    #description = description + position.find('div', class_='yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2').find('a').next_sibling.next_element

print(title)
print(length)
print(videoLink)
print(uploaded)
print(views)
print(channel)
print (channelLink)
##print(description)
