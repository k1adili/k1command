import requests
from bs4 import BeautifulSoup


url = 'https://weather.com/weather/today/l/35.76,51.33?par=google&temp=c'
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempHiLoValue--3T1DG")
txt = data[0].text.strip().replace(',', '')

print (txt)
