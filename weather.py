import requests
import pandas as pd
from bs4 import BeautifulSoup

varos = input("Melyik város időjárására vagy kíváncsi : ")

page = requests.get(f'https://www.idokep.hu/30napos/{varos}')
soup = BeautifulSoup(page.content, 'html.parser')

weeks = soup.find(class_="kartya-full")

items = weeks.find_all(class_="oszlop")

date = [item.find(class_="buborek-fejlec").get_text() for item in items]

dayslist = []
datetime = []
days = []

for item in date:
    if "." in item:
        dayslist.extend(item.split("."))

index_of_item = 0
for item in dayslist:
    if index_of_item % 2 == 0:
        datetime.append(item)
        index_of_item +=1
    else:
        days.append(item)
        index_of_item +=1

maxdegree = weeks.find_all(class_="max-homerseklet-default max")
mindegree = weeks.find_all(class_="min-homerseklet-default max")

maximum = [item.find(class_="zivatar-text").get_text() for item in maxdegree]
minimum = [item.find(class_="zivatar-text").get_text() for item in mindegree]

s1 = pd.Series(datetime, name='Date')
s2 = pd.Series(days, name='Days')
s3 = pd.Series(maximum, name='Max')
s4 = pd.Series(minimum, name='Min')
df = pd.concat([s1,s2,s3,s4], axis=1)
print(df)
