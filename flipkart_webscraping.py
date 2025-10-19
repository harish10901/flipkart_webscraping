import requests
import pandas
from bs4 import BeautifulSoup
import csv


response=requests.get("https://www.flipkart.com/tyy/4io/~cs-7udytyszj7/pr?sid=tyy%2C4io&collection-tab-name=realme+P4+5G&pageCriteria=default&param=8765&hpid=URax_5r1Q7zsXV8AZFejtap7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTE0LDk5OSoiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJNT0JIRVJYRjJSVUhRTVhFIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsicmVhbG1lIFA0IDVHIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D")
print(response)

soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
names=soup.find_all("div",class_='KzDlHZ')
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
print(name)

prices=soup.find_all("div",class_='Nx9bqj _4b5DiR')
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
print(str(price).encode('ascii','ignore').decode('ascii'))

bank_offer=soup.find_all("div",class_='cPHDOP col-12-12')
bank_off=[]
for i in bank_offer [0:10]:
    d=i.get_text()
    bank_off.append(d)
print(str(bank_off).encode('ascii','ignore').decode('ascii'))

exchanges=soup.find_all("div",class_='M4DNwV')
exchange=[]
for i in exchanges[0:10]:
    d=i.get_text()
    exchange.append(d)
print(str(exchange).encode('ascii','ignore').decode('ascii'))

images=soup.find_all("img",class_='DByuf4')
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
print(image)

ratings=soup.find_all("div",class_='XQDdHH')
rate=[]
for i in ratings[0:10]:
    d=i.get_text()
    rate.append(float(d))
print(rate)

ratings_and_reviews=soup.find_all("span",class_='Wphh3N')
RNR=[]
for i in ratings_and_reviews[0:10]:
    d=i.get_text()
    RNR.append(d)
print(RNR)

features=soup.find_all("ul",class_='G4BRas')
feature=[]
for i in features[0:10]:
    d=i.get_text()
    feature.append(d)
print(feature)

data={'Names':pandas.Series(name),
      "Prices":pandas.Series(price),
      "Bank_offer":pandas.Series(bank_off),
      "Exchanges":pandas.Series(exchange),
      "Images":pandas.Series(image),
      "Ratings":pandas.Series(rate),
      "Ratings_and_Reviews":pandas.Series(RNR),
      "Features":pandas.Series(feature)
      }

df = pandas.DataFrame(data)
df.to_csv("mobiles_data.csv")