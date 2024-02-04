from bs4 import BeautifulSoup
import requests
import csv

url= "https://www.fflogs.com/reports/CWhbrDfp781gtKzq#fight=16&type=damage-done&source=13"
html = requests.get(url)

s = BeautifulSoup(html.content, "html.parser")

results = s.find(id= "filter-type-tabs-wrapper")
Inhalt = results.find_all("div", class_= "report-bar-inset")

file = open("scraped_Inhalt.csv", "w")
print(Inhalt[0].text)
