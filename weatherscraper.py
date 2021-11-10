from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://forecast.weather.gov/MapClick.php?lat=40.8124&lon=-74.2128"

page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

temp_scr = soup.find("p", class_="myforecast-current-lrg")
temp = """Temperature
""" + temp_scr.string

print(temp)

condition_src = soup.find("div", id="current_conditions_detail")
for string in condition_src.stripped_strings:
    print(string)
