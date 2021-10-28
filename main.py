# IMPORT BEAUTIFUL SOUP
from urllib.request import urlopen
from bs4 import BeautifulSoup

# READING FILE
year_end_music = 'https://en.wikipedia.org/wiki/List_of_Billboard_Year-End_number-one_singles_and_albums'
year_end_html = urlopen(year_end_music)
soup = BeautifulSoup(year_end_html, 'html.parser')

# TEST TEXT
links = soup.find(title="Hey! Ba-Ba-Re-Bop")
print (links)

# print(year_end_html)
# with open()