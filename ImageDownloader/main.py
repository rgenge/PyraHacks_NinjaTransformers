from bs4 import *
import requests
import os
import sys
import re

def img_converter(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    image_tags = soup.find_all('img')
    urls = [img['src'] for img in image_tags]
    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|png))$', url)
        with open(('images/'+ filename.group(1)), 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(link, url)
            response = requests.get(url)
            f.write(response.content)
if __name__ == "__main__":

    link = input("Enter the url you want to analyse starting with 'https://':\n")
    if not os.path.exists('images'):
        os.makedirs('images')
    try:
        response = requests.get(link)
        if response.status_code == 200:
            img_converter(link)
    except:
        sys.exit("Type a valid addres starting with 'https://'\n")

