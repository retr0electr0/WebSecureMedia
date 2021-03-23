"""
WebSecureMedia: Scraper
"""
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://websecuremedia.com/modalpopupbox/').text

soup = BeautifulSoup(source, 'lxml')

# Creating or appending a .csv file
csv_file = open('Web Secure Media.csv', 'a')

fieldnames = ['Platform', 'Asset', 'Asset_link', 'Date Posted']
writer = csv.DictWriter(csv_file, delimiter=',', lineterminator='\n',fieldnames=fieldnames)
writer.writeheader()

# Getting the data
for asset in soup.find_all('div', {'class': 'td_module_10 td_module_wrap td-animation-stack td_module_no_thumb'}):

    asset_name = asset.find('div', {'class': 'td-excerpt'}).text.strip()
    print(asset_name)

    asset_link = asset.h3.a['href']
    print(asset_link)

    asset_date = asset.find('time', {'class': 'entry-date updated td-module-date'}).text.strip()
    print(asset_date)

    print()

    # Writing to .csv file
    writer.writerow({'Platform': 'Web Secure Media', 'Asset': asset_name, 'Asset_link': asset_link,
                     'Date Posted': asset_date})

csv_file.close()