# IMPORT BEAUTIFUL SOUP
from urllib3.request import urlopen
from bs4 import BeautifulSoup

# READING FILE
year_end_music = 'https://en.wikipedia.org/wiki/List_of_Billboard_Year-End_number-one_singles_and_albums'
year_end_html = urllib3.urlopen(year_end_music)

print(year_end_html)
# with open()